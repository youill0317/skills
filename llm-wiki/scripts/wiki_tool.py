#!/usr/bin/env python3
"""Deterministic filesystem operations for the llm-wiki skill."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import stat
import sys
import tempfile
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit, urlunsplit


PAGE_STATUSES = {"draft", "reviewed", "stable"}
MANIFEST_STATES = {"processed", "versioned"}
SKIP_DIRS = {".git", ".obsidian", "node_modules", ".trash"}
SKIP_DIRS_CASEFOLD = {name.casefold() for name in SKIP_DIRS}
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
WIKI_ID_RE = re.compile(r"^[a-z0-9][a-z0-9_-]*$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
WINDOWS_RESERVED = {
    "CON",
    "PRN",
    "AUX",
    "NUL",
    *(f"COM{i}" for i in range(1, 10)),
    *(f"LPT{i}" for i in range(1, 10)),
}


class WikiError(RuntimeError):
    pass


def emit(value: Any) -> None:
    print(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True))


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def resolve_existing_dir(value: str | Path, label: str) -> Path:
    raw = Path(value).expanduser()
    if is_reparse_point(raw):
        raise WikiError(f"{label} must not be a symlink, junction, or reparse point: {raw}")
    resolved = raw.resolve(strict=True)
    if not resolved.is_dir():
        raise WikiError(f"{label} is not a directory: {resolved}")
    return resolved


def ensure_within(path: Path, root: Path, label: str) -> None:
    try:
        path.relative_to(root)
    except ValueError as exc:
        raise WikiError(f"{label} escapes {root}: {path}") from exc


def is_reparse_point(path: Path) -> bool:
    try:
        metadata = os.lstat(path)
    except (FileNotFoundError, OSError):
        return False
    if stat.S_ISLNK(metadata.st_mode):
        return True
    is_junction = getattr(os.path, "isjunction", None)
    if is_junction is not None:
        try:
            if is_junction(path):
                return True
        except OSError:
            pass
    tag = getattr(metadata, "st_reparse_tag", 0)
    dangerous_tags = {
        getattr(stat, "IO_REPARSE_TAG_SYMLINK", 0xA000000C),
        getattr(stat, "IO_REPARSE_TAG_MOUNT_POINT", 0xA0000003),
    }
    return bool(tag and tag in dangerous_tags)


def lexical_absolute(path: Path) -> Path:
    return Path(os.path.abspath(path))


def ensure_no_reparse(path: Path, root: Path, label: str) -> None:
    """Reject existing reparse components below a trusted, resolved root."""
    lexical = lexical_absolute(path)
    root = lexical_absolute(root)
    ensure_within(lexical, root, label)
    current = root
    for part in lexical.relative_to(root).parts:
        current = current / part
        if is_reparse_point(current):
            raise WikiError(f"{label} crosses a symlink, junction, or reparse point: {current}")


def resolve_contained(path: Path, root: Path, label: str) -> Path:
    lexical = lexical_absolute(path)
    ensure_within(lexical, root, label)
    ensure_no_reparse(lexical, root, label)
    resolved = lexical.resolve(strict=False)
    ensure_within(resolved, root, label)
    return resolved


def relative_posix(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def strip_markdown_code(text: str) -> str:
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    visible: list[str] = []
    fence_char: str | None = None
    fence_length = 0
    for line in text.splitlines():
        indented = line.startswith("\t") or line.startswith("    ")
        nested_list = bool(re.match(r"^\s*(?:[-*+]\s+|\d+[.)]\s+)", line))
        if indented and not nested_list and (not visible or not visible[-1].strip()):
            visible.append("")
            continue
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if fence_char is not None:
            closes = re.fullmatch(rf"\s*{re.escape(fence_char)}{{{fence_length},}}\s*", line)
            if closes:
                fence_char = None
                fence_length = 0
            visible.append("")
            continue
        if marker:
            fence_char = marker.group(1)[0]
            fence_length = len(marker.group(1))
            visible.append("")
            continue
        visible.append(re.sub(r"`+[^`\n]*`+", "", line))
    return "\n".join(visible)


def strip_yaml_comment(value: str) -> str:
    quote: str | None = None
    escaped = False
    for index, char in enumerate(value):
        if escaped:
            escaped = False
            continue
        if quote == '"' and char == "\\":
            escaped = True
            continue
        if char in {"'", '"'}:
            quote = None if quote == char else char if quote is None else quote
            continue
        if char == "#" and quote is None and index > 0 and value[index - 1].isspace():
            return value[:index].rstrip()
    return value.rstrip()


def parse_scalar(value: str) -> Any:
    value = strip_yaml_comment(value.strip())
    if len(value) >= 2 and value[0] == value[-1] == "'":
        return value[1:-1].replace("''", "'")
    if len(value) >= 2 and value[0] == value[-1] == '"':
        try:
            parsed = json.loads(value)
        except json.JSONDecodeError as exc:
            raise WikiError(f"unsupported quoted YAML scalar: {value}") from exc
        if not isinstance(parsed, str):
            raise WikiError(f"quoted YAML scalar must be text: {value}")
        return parsed
    if value.startswith("[") and value.endswith("]"):
        try:
            parsed = json.loads(value.replace("'", '"'))
        except json.JSONDecodeError as exc:
            raise WikiError(f"unsupported inline YAML list: {value}") from exc
        if not isinstance(parsed, list) or any(not isinstance(item, str) for item in parsed):
            raise WikiError(f"inline YAML list must contain only text: {value}")
        return parsed
    lowered = value.lower()
    if lowered == "true":
        return True
    if lowered == "false":
        return False
    return value


def parse_frontmatter_text(text: str) -> dict[str, Any]:
    lines = text.lstrip("\ufeff").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        return {}

    data: dict[str, Any] = {}
    current: str | None = None
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        indent = len(line) - len(line.lstrip(" "))
        stripped = line.strip()
        if indent == 0:
            match = re.match(r"^([A-Za-z0-9_-]+):(?:\s*(.*))?$", stripped)
            if not match:
                current = None
                continue
            key, raw_value = match.group(1), match.group(2) or ""
            current = key
            if raw_value:
                data[key] = parse_scalar(raw_value)
            elif key == "sources":
                data[key] = []
            else:
                data[key] = {}
            continue
        if current is None:
            continue
        if stripped.startswith("- "):
            if not isinstance(data.get(current), list):
                data[current] = []
            data[current].append(parse_scalar(stripped[2:]))
            continue
        match = re.match(r"^([A-Za-z0-9_-]+):(?:\s*(.*))?$", stripped)
        if match:
            if not isinstance(data.get(current), dict):
                data[current] = {}
            data[current][match.group(1)] = parse_scalar(match.group(2) or "")
    return data


def read_frontmatter(path: Path) -> dict[str, Any]:
    try:
        return parse_frontmatter_text(path.read_text(encoding="utf-8"))
    except UnicodeDecodeError as exc:
        raise WikiError(f"Markdown is not valid UTF-8: {path}") from exc


def yaml_quote(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


def normalize_url(value: str | None) -> str | None:
    if not isinstance(value, str) or not value:
        return None
    value = value.strip()
    try:
        parts = urlsplit(value)
    except ValueError:
        return value
    if not parts.scheme or not parts.netloc:
        return value
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), parts.path, parts.query, ""))


def source_metadata(path: Path) -> dict[str, Any]:
    metadata: dict[str, Any] = {"source_type": path.suffix.lower().lstrip(".") or "file"}
    if path.suffix.lower() not in {".md", ".markdown", ".txt"}:
        return metadata
    try:
        frontmatter = read_frontmatter(path)
    except WikiError:
        return metadata
    source_url = frontmatter.get("source_url") or frontmatter.get("source") or frontmatter.get("url")
    if isinstance(source_url, str) and source_url.strip():
        metadata["source_url"] = source_url.strip()
        metadata["normalized_url"] = normalize_url(source_url)
    for source_key, manifest_key in (
        ("captured_at", "captured_at"),
        ("published", "published_at"),
        ("author", "author"),
    ):
        value = frontmatter.get(source_key)
        if isinstance(value, str) and value.strip():
            metadata[manifest_key] = value.strip()
    return metadata


def is_definition(frontmatter: dict[str, Any]) -> bool:
    return frontmatter.get("llm_wiki") is True


def definition_errors(frontmatter: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for key in ("wiki_id", "name", "root", "raws", "files", "index", "log", "manifest", "outputs"):
        value = frontmatter.get(key)
        if key not in frontmatter or value == "" or value is None:
            errors.append(f"missing definition field: {key}")
    wiki_id = frontmatter.get("wiki_id")
    if not isinstance(wiki_id, str) or not WIKI_ID_RE.fullmatch(wiki_id):
        errors.append("wiki_id must use lowercase letters, digits, hyphens, or underscores")
    if not isinstance(frontmatter.get("name"), str) or not frontmatter.get("name").strip():
        errors.append("name must be non-empty text")
    for key in ("root", "raws", "index", "log", "manifest", "outputs"):
        if not isinstance(frontmatter.get(key), str) or not frontmatter.get(key).strip():
            errors.append(f"{key} must be a non-empty vault-relative path")
    files = frontmatter.get("files")
    if not isinstance(files, dict) or not files:
        errors.append("files must be a non-empty mapping")
    elif any(
        not isinstance(key, str)
        or not re.fullmatch(r"[A-Za-z0-9_-]+", key)
        or not isinstance(value, str)
        or not value.strip()
        for key, value in files.items()
    ):
        errors.append("files keys and paths must be non-empty text")
    elif any(key in {"root", "raws", "index", "log", "manifest", "outputs"} for key in files):
        errors.append("files keys must not reuse reserved definition path names")
    page_types = frontmatter.get("page_types")
    if page_types is not None and (
        not isinstance(page_types, dict)
        or any(
            not isinstance(key, str)
            or not isinstance(value, str)
            or not key.strip()
            or not value.strip()
            for key, value in page_types.items()
        )
    ):
        errors.append("page_types must map folder keys to non-empty type names")
    elif isinstance(files, dict):
        folder_keys = set(files) | {"outputs"}
        default_keys = {"concepts", "entities", "decisions", "outputs"}
        if page_types is None and not folder_keys.issubset(default_keys):
            errors.append("custom files keys require an explicit page_types mapping")
        elif isinstance(page_types, dict) and set(page_types) != folder_keys:
            errors.append("page_types keys must exactly match files keys plus outputs")
    page_statuses = frontmatter.get("page_statuses")
    if page_statuses is not None and (
        not isinstance(page_statuses, list)
        or not page_statuses
        or any(not isinstance(value, str) or not value.strip() for value in page_statuses)
    ):
        errors.append("page_statuses must be a non-empty text list")
    evidence_wikis = frontmatter.get("evidence_wikis")
    if evidence_wikis is not None and (
        not isinstance(evidence_wikis, list)
        or any(not isinstance(value, str) or not WIKI_ID_RE.fullmatch(value) for value in evidence_wikis)
        or len(evidence_wikis) != len(set(evidence_wikis))
    ):
        errors.append("evidence_wikis must be a unique list of valid wiki IDs")
    page_fields = frontmatter.get("page_fields")
    semantic_fields = {"wiki_id", "page_type", "status", "sources"}
    if page_fields is not None and (
        not isinstance(page_fields, dict)
        or set(page_fields) != semantic_fields
        or any(
            not isinstance(value, str) or not re.fullmatch(r"[A-Za-z0-9_-]+", value)
            for value in page_fields.values()
        )
        or len(set(page_fields.values())) != len(semantic_fields)
    ):
        errors.append("page_fields must uniquely map wiki_id, page_type, status, and sources to field names")
    return errors


def configured_path(frontmatter: dict[str, Any], key: str, vault: Path, default: Path | None = None) -> Path:
    value = frontmatter.get(key)
    if not isinstance(value, str) or not value.strip():
        if default is None:
            raise WikiError(f"missing configured path: {key}")
        candidate_path = default
    else:
        candidate = Path(value)
        if candidate.is_absolute():
            raise WikiError(f"configured path must be vault-relative ({key}): {value}")
        candidate_path = vault / candidate
    return resolve_contained(candidate_path, vault, f"configured path {key}")


def wiki_owned_path(
    frontmatter: dict[str, Any],
    key: str,
    vault: Path,
    wiki: Path,
    default: Path | None = None,
) -> Path:
    path = configured_path(frontmatter, key, vault, default)
    ensure_within(path, wiki, f"configured wiki-owned path {key}")
    return path


def manifest_path_for(wiki: Path, frontmatter: dict[str, Any], vault: Path) -> Path:
    return wiki_owned_path(frontmatter, "manifest", vault, wiki, wiki / "manifest.jsonl")


def validated_wiki_layout(frontmatter: dict[str, Any], vault: Path, wiki: Path) -> dict[str, Path]:
    required: dict[str, Path] = {"root": configured_path(frontmatter, "root", vault)}
    if required["root"] != wiki:
        raise WikiError(f"configured root does not match definition folder: {required['root']} != {wiki}")
    for key in ("raws", "index", "log", "manifest", "outputs"):
        required[key] = wiki_owned_path(frontmatter, key, vault, wiki)
    for key, value in frontmatter.get("files", {}).items():
        path = resolve_contained(vault / value, vault, f"configured path files.{key}")
        ensure_within(path, wiki, f"configured wiki-owned path files.{key}")
        required[key] = path

    directory_keys = {"root", "raws", "outputs", *frontmatter.get("files", {}).keys()}
    for key, path in required.items():
        if is_reparse_point(path):
            raise WikiError(f"configured path is a symlink or junction ({key}): {path}")
        if key in directory_keys and not path.is_dir():
            raise WikiError(f"missing configured directory ({key}): {path}")
        if key not in directory_keys and not path.is_file():
            raise WikiError(f"missing configured file ({key}): {path}")

    owned_directories = [("raws", required["raws"]), ("outputs", required["outputs"])] + [
        (key, required[key]) for key in frontmatter.get("files", {})
    ]
    for index, (left_key, left_path) in enumerate(owned_directories):
        for right_key, right_path in owned_directories[index + 1 :]:
            try:
                left_path.relative_to(right_path)
                overlaps = True
            except ValueError:
                try:
                    right_path.relative_to(left_path)
                    overlaps = True
                except ValueError:
                    overlaps = False
            if overlaps:
                raise WikiError(f"configured directories overlap: {left_key} and {right_key}")

    special_files = {
        "Wiki.md": wiki / "Wiki.md",
        "index": required["index"],
        "log": required["log"],
        "manifest": required["manifest"],
    }
    if len(set(special_files.values())) != len(special_files):
        raise WikiError("Wiki.md, index, log, and manifest must be distinct files")
    for file_key, file_path in special_files.items():
        for directory_key, directory in owned_directories:
            try:
                file_path.relative_to(directory)
            except ValueError:
                continue
            raise WikiError(f"configured file {file_key} must not be inside {directory_key}")
    return required


def load_manifest(path: Path) -> tuple[list[dict[str, Any]], list[str]]:
    if not path.exists():
        return [], []
    records: list[dict[str, Any]] = []
    errors: list[str] = []
    try:
        with path.open("r", encoding="utf-8") as handle:
            for line_number, line in enumerate(handle, 1):
                if not line.strip():
                    continue
                try:
                    value = json.loads(line)
                except json.JSONDecodeError as exc:
                    errors.append(f"line {line_number}: invalid JSON ({exc.msg})")
                    continue
                if not isinstance(value, dict):
                    errors.append(f"line {line_number}: record is not an object")
                    continue
                records.append(value)
    except UnicodeDecodeError as exc:
        raise WikiError(f"manifest is not valid UTF-8: {path}") from exc
    return records, errors


def root_wiki_candidates(vault: Path) -> list[Path]:
    candidates: list[Path] = []
    for child in sorted(vault.iterdir(), key=lambda item: item.name.casefold()):
        if (
            is_reparse_point(child)
            or not child.is_dir()
            or child.name.casefold() in SKIP_DIRS_CASEFOLD
            or child.name.casefold() == "_ingest"
        ):
            continue
        if (child / "Wiki.md").is_file() or ((child / "raws").is_dir() and (child / "index.md").is_file()):
            candidates.append(child)
    return candidates


def discover_payload(vault: Path) -> dict[str, Any]:
    definitions: list[dict[str, Any]] = []
    candidates: list[str] = []
    for wiki in root_wiki_candidates(vault):
        note = wiki / "Wiki.md"
        if not note.is_file():
            candidates.append(relative_posix(wiki, vault))
            continue
        try:
            frontmatter = read_frontmatter(note)
        except WikiError as exc:
            definitions.append({"path": relative_posix(note, vault), "valid": False, "errors": [str(exc)]})
            continue
        if not is_definition(frontmatter):
            candidates.append(relative_posix(wiki, vault))
            continue
        errors = definition_errors(frontmatter)
        definitions.append(
            {
                "path": relative_posix(note, vault),
                "root": relative_posix(wiki, vault),
                "wiki_id": frontmatter.get("wiki_id"),
                "name": frontmatter.get("name"),
                "valid": not errors,
                "errors": errors,
            }
        )
    ingest = vault / "_ingest"
    queued = []
    if is_reparse_point(ingest):
        raise WikiError(f"_ingest must not be a symlink, junction, or reparse point: {ingest}")
    if ingest.is_dir():
        inventory_issues: list[dict[str, str]] = []
        intake_files = scan_tree_files(ingest, inventory_issues, vault)
        for path in intake_files:
            if path.stat().st_nlink != 1:
                inventory_issues.append(
                    {
                        "severity": "error",
                        "path": relative_posix(path, vault),
                        "message": "intake file has multiple hard links",
                    }
                )
        queued = [relative_posix(path, vault) for path in intake_files]
        inventory_errors = [issue for issue in inventory_issues if issue["severity"] == "error"]
        if inventory_errors:
            raise WikiError(f"unsafe _ingest entry: {inventory_errors[0]['path']} ({inventory_errors[0]['message']})")
    return {
        "vault": str(vault),
        "definitions": definitions,
        "candidates": candidates,
        "ingest_exists": ingest.is_dir(),
        "ingest_entries": queued,
    }


def command_discover(args: argparse.Namespace) -> int:
    vault = resolve_existing_dir(args.vault, "vault")
    emit(discover_payload(vault))
    return 0


def validate_folder_name(value: str) -> None:
    if (
        not value
        or value in {".", ".."}
        or any(char in value for char in '<>:"/\\|?*')
        or any(ord(char) < 32 for char in value)
    ):
        raise WikiError("wiki folder must be one non-empty vault-root folder name")
    if value.endswith((" ", ".")) or value.upper().split(".")[0] in WINDOWS_RESERVED:
        raise WikiError(f"wiki folder is not portable on Windows: {value}")
    forbidden_roots = {name.casefold() for name in SKIP_DIRS} | {
        "_ingest",
        ".llm-wiki.lock",
        ".llm-wiki-transaction.json",
    }
    if value.casefold() in forbidden_roots:
        raise WikiError(f"wiki folder is reserved by the vault or llm-wiki runtime: {value}")


def write_exclusive(path: Path, text: str) -> None:
    with path.open("x", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


def command_scaffold(args: argparse.Namespace) -> int:
    vault = resolve_existing_dir(args.vault, "vault")
    validate_folder_name(args.folder)
    if not WIKI_ID_RE.fullmatch(args.wiki_id):
        raise WikiError("wiki_id must use lowercase letters, digits, hyphens, or underscores")
    wiki = (vault / args.folder).resolve(strict=False)
    ensure_within(wiki, vault, "wiki root")
    if wiki.exists():
        raise WikiError(f"target wiki already exists: {wiki}")
    display_name = args.name or args.folder
    if not display_name.strip() or any(char in "\r\n" or ord(char) < 32 for char in display_name):
        raise WikiError("display name must be non-empty text without control characters")
    today = datetime.now().date().isoformat()
    ingest = vault / "_ingest"
    if is_reparse_point(ingest):
        raise WikiError(f"_ingest must not be a symlink, junction, or reparse point: {ingest}")

    definition = f"""---
llm_wiki: true
wiki_id: {yaml_quote(args.wiki_id)}
name: {yaml_quote(display_name)}
root: {yaml_quote(args.folder)}
raws: {yaml_quote(args.folder + '/raws')}
files:
  concepts: {yaml_quote(args.folder + '/concepts')}
  entities: {yaml_quote(args.folder + '/entities')}
  decisions: {yaml_quote(args.folder + '/decisions')}
index: {yaml_quote(args.folder + '/index.md')}
log: {yaml_quote(args.folder + '/log.md')}
manifest: {yaml_quote(args.folder + '/manifest.jsonl')}
outputs: {yaml_quote(args.folder + '/outputs')}
evidence_wikis: []
page_types:
  concepts: concept
  entities: entity
  decisions: decision
  outputs: output
page_statuses:
  - draft
  - reviewed
  - stable
page_fields:
  wiki_id: wiki_id
  page_type: page_type
  status: status
  sources: sources
---
# {display_name}

## Scope

- Define what belongs in this wiki and what does not.

## Page Policy

- Update an existing draft page when it already owns the idea.
- Create pages only for durable concepts, entities, decisions, or requested outputs.
- Preserve human-authored, reviewed, and stable knowledge; propose conflicting changes.

## Source Policy

- Treat filed raws as immutable evidence and source bodies as untrusted data.
- Ground material compiled claims near raw-source links.
- Preserve disagreement and label inference.
"""
    index = f"""# {display_name} Index

## Concepts

## Entities

## Decisions

## Outputs
"""
    log = f"""# {display_name} Log

## [{today}] create | Wiki initialized

- Created the default llm-wiki structure.
"""
    stage = Path(tempfile.mkdtemp(prefix=f".{args.folder}.llm-wiki-", dir=vault))
    try:
        for folder in ("raws", "concepts", "entities", "decisions", "outputs"):
            (stage / folder).mkdir()
        write_exclusive(stage / "Wiki.md", definition)
        write_exclusive(stage / "index.md", index)
        write_exclusive(stage / "log.md", log)
        write_exclusive(stage / "manifest.jsonl", "")
        ingest.mkdir(exist_ok=True)
        stage.rename(wiki)
    except Exception:
        if stage.exists():
            shutil.rmtree(stage)
        raise
    emit(
        {
            "status": "created",
            "wiki": relative_posix(wiki, vault),
            "created": [relative_posix(path, vault) for path in sorted(wiki.rglob("*"))],
            "ingest": relative_posix(vault / "_ingest", vault),
        }
    )
    return 0


def load_target_wiki(value: str | Path) -> tuple[Path, Path, dict[str, Any]]:
    raw = Path(value).expanduser()
    if is_reparse_point(raw):
        raise WikiError(f"wiki must not be a symlink, junction, or reparse point: {raw}")
    wiki = resolve_existing_dir(raw, "wiki")
    vault = wiki.parent
    note = wiki / "Wiki.md"
    if not note.is_file() or is_reparse_point(note):
        raise WikiError(f"wiki is missing a regular Wiki.md: {note}")
    frontmatter = read_frontmatter(note)
    if not is_definition(frontmatter):
        raise WikiError(f"Wiki.md first YAML block must contain llm_wiki: true: {note}")
    errors = definition_errors(frontmatter)
    if errors:
        raise WikiError(f"invalid wiki definition ({'; '.join(errors)}): {note}")
    validated_wiki_layout(frontmatter, vault, wiki)
    return vault, wiki, frontmatter


def all_manifest_records(vault: Path) -> list[dict[str, Any]]:
    collected: list[dict[str, Any]] = []
    seen_paths: set[str] = set()
    seen_hashes: set[str] = set()
    for wiki in root_wiki_candidates(vault):
        note = wiki / "Wiki.md"
        if not note.is_file():
            continue
        if is_reparse_point(note):
            raise WikiError(f"definition note is a symlink, junction, or reparse point: {note}")
        try:
            frontmatter = read_frontmatter(note)
        except WikiError as exc:
            raise WikiError(f"cannot verify wiki definition before deduplication: {exc}") from exc
        if not is_definition(frontmatter):
            continue
        errors = definition_errors(frontmatter)
        if errors:
            raise WikiError(f"invalid wiki definition before deduplication ({'; '.join(errors)}): {note}")
        layout = validated_wiki_layout(frontmatter, vault, wiki)
        raws = layout["raws"]
        manifest = layout["manifest"]
        records, manifest_errors = load_manifest(manifest)
        if manifest_errors:
            raise WikiError(f"manifest is invalid ({'; '.join(manifest_errors)}): {manifest}")
        lineage_errors = manifest_lineage_errors(records)
        if lineage_errors:
            raise WikiError(f"manifest lineage is invalid ({'; '.join(lineage_errors)}): {manifest}")
        for record in records:
            record_errors, raw_path = manifest_record_errors(record, vault, wiki, raws, verify_bytes=True)
            if record_errors:
                raise WikiError(f"manifest record is invalid ({'; '.join(record_errors)}): {manifest}")
            assert raw_path is not None
            raw_key = relative_posix(raw_path, vault)
            digest = record["sha256"]
            if raw_key in seen_paths:
                raise WikiError(f"duplicate manifest raw_path blocks safe deduplication: {raw_key}")
            if digest in seen_hashes:
                raise WikiError(f"duplicate manifest SHA-256 blocks safe deduplication: {digest}")
            seen_paths.add(raw_key)
            seen_hashes.add(digest)
            enriched = dict(record)
            enriched["_wiki"] = relative_posix(wiki, vault)
            enriched["_wiki_id"] = frontmatter.get("wiki_id")
            collected.append(enriched)
    return collected


def manifest_record_errors(
    record: dict[str, Any],
    vault: Path,
    wiki: Path,
    raws: Path,
    *,
    verify_bytes: bool,
) -> tuple[list[str], Path | None]:
    errors: list[str] = []
    raw_path: Path | None = None
    required = ("schema", "state", "raw_path", "original_path", "sha256", "bytes", "recorded_at", "source_type")
    for key in required:
        if key not in record:
            errors.append(f"missing {key}")
    if isinstance(record.get("schema"), bool) or record.get("schema") != 1:
        errors.append("schema must be 1")
    if record.get("state") not in MANIFEST_STATES:
        errors.append("state must be processed or versioned")
    digest = record.get("sha256")
    if not isinstance(digest, str) or not SHA256_RE.fullmatch(digest):
        errors.append("sha256 must be 64 lowercase hexadecimal characters")
    size = record.get("bytes")
    if isinstance(size, bool) or not isinstance(size, int) or size < 0:
        errors.append("bytes must be a non-negative integer")
    recorded_at = record.get("recorded_at")
    if not isinstance(recorded_at, str) or not recorded_at.strip():
        errors.append("recorded_at must be non-empty ISO-8601 text")
    else:
        try:
            parsed_time = datetime.fromisoformat(recorded_at.replace("Z", "+00:00"))
            if parsed_time.tzinfo is None:
                raise ValueError("timezone is missing")
        except ValueError:
            errors.append("recorded_at must be a timezone-aware ISO-8601 timestamp")
    source_type = record.get("source_type")
    if not isinstance(source_type, str) or not source_type.strip():
        errors.append("source_type must be non-empty text")
    if "source_url" in record and not isinstance(record.get("source_url"), str):
        errors.append("source_url must be text when present")

    raw_value = record.get("raw_path")
    if not isinstance(raw_value, str) or not raw_value:
        errors.append("raw_path must be non-empty text")
    else:
        candidate = Path(raw_value)
        if candidate.is_absolute():
            errors.append("raw_path must be vault-relative")
        else:
            try:
                raw_path = resolve_contained(vault / candidate, vault, "manifest raw_path")
                ensure_within(raw_path, raws, "manifest raw_path")
            except WikiError as exc:
                errors.append(str(exc))
                raw_path = None

    original_value = record.get("original_path")
    if not isinstance(original_value, str) or not original_value:
        errors.append("original_path must be non-empty text")
    else:
        candidate = Path(original_value)
        if candidate.is_absolute():
            errors.append("original_path must be vault-relative")
        else:
            try:
                original = resolve_contained(vault / candidate, vault, "manifest original_path")
                ensure_within(original, resolve_contained(vault / "_ingest", vault, "_ingest"), "manifest original_path")
            except WikiError as exc:
                errors.append(str(exc))

    if raw_path is not None and verify_bytes:
        if not raw_path.is_file() or is_reparse_point(raw_path):
            errors.append(f"raw is missing or unsafe: {relative_posix(raw_path, vault)}")
        else:
            if raw_path.stat().st_nlink != 1:
                errors.append(f"raw has multiple hard links: {relative_posix(raw_path, vault)}")
            actual_size = raw_path.stat().st_size
            if isinstance(size, int) and not isinstance(size, bool) and actual_size != size:
                errors.append(f"raw byte size differs: {relative_posix(raw_path, vault)}")
            if isinstance(digest, str) and SHA256_RE.fullmatch(digest) and sha256_file(raw_path) != digest:
                errors.append(f"raw SHA-256 differs: {relative_posix(raw_path, vault)}")
    return errors, raw_path


def manifest_lineage_errors(records: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    prior: dict[str, dict[str, Any]] = {}
    for index, record in enumerate(records, 1):
        raw_path = record.get("raw_path")
        if record.get("state") == "versioned":
            current_url = normalize_url(record.get("source_url"))
            previous = record.get("previous_raws")
            if not current_url:
                errors.append(f"record {index}: versioned state requires source_url")
            if not isinstance(previous, list) or not previous:
                errors.append(f"record {index}: versioned state requires previous_raws")
            else:
                for predecessor_path in previous:
                    predecessor = prior.get(predecessor_path) if isinstance(predecessor_path, str) else None
                    if predecessor is None:
                        errors.append(f"record {index}: predecessor is not an earlier raw: {predecessor_path}")
                    elif normalize_url(predecessor.get("source_url")) != current_url:
                        errors.append(f"record {index}: predecessor belongs to a different source URL: {predecessor_path}")
        if isinstance(raw_path, str) and raw_path:
            prior[raw_path] = record
    return errors


def collision_safe_path(directory: Path, source: Path) -> tuple[Path, bool]:
    candidate = directory / source.name
    if not os.path.lexists(candidate):
        return candidate, False
    suffix = source.suffix
    stem = source.name[: -len(suffix)] if suffix else source.name
    counter = 2
    while True:
        candidate = directory / f"{stem}-{counter}{suffix}"
        if not os.path.lexists(candidate):
            return candidate, True
        counter += 1


def append_manifest(path: Path, record: dict[str, Any]) -> None:
    if is_reparse_point(path):
        raise WikiError(f"manifest must not be a symlink, junction, or reparse point: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    previous = path.read_bytes() if path.exists() else b""
    if previous and not previous.endswith(b"\n"):
        raise WikiError(f"manifest does not end with a newline: {path}")
    payload = previous + (json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n").encode("utf-8")
    descriptor, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


def write_json_atomic(path: Path, value: dict[str, Any]) -> None:
    if is_reparse_point(path):
        raise WikiError(f"transaction journal must not be a symlink or junction: {path}")
    descriptor, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            json.dump(value, handle, ensure_ascii=False, indent=2, sort_keys=True)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


@contextmanager
def exclusive_vault_lock(vault: Path):
    lock = vault / ".llm-wiki.lock"
    try:
        descriptor = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError as exc:
        raise WikiError(f"another llm-wiki write may be active; inspect stale lock before removing it: {lock}") from exc
    try:
        os.write(descriptor, f"pid={os.getpid()} recorded_at={utc_now()}\n".encode("utf-8"))
        os.fsync(descriptor)
        yield
    finally:
        os.close(descriptor)
        try:
            lock.unlink()
        except FileNotFoundError:
            pass


def move_raw_once(args: argparse.Namespace, prepared: tuple[Path, Path, dict[str, Any]]) -> int:
    vault, wiki, definition = prepared
    raw_source = Path(args.source).expanduser()
    ingest_candidate = vault / "_ingest"
    if is_reparse_point(ingest_candidate) or not ingest_candidate.is_dir():
        raise WikiError(f"_ingest is missing or unsafe: {ingest_candidate}")
    ingest = resolve_contained(ingest_candidate, vault, "_ingest")
    source_candidate = lexical_absolute(raw_source)
    ensure_within(source_candidate, ingest, "source")
    ensure_no_reparse(source_candidate, ingest, "source")
    source = source_candidate.resolve(strict=True)
    if not source.is_file():
        raise WikiError(f"source is not a regular file: {source}")
    if source.stat().st_nlink != 1:
        raise WikiError(f"source must not have multiple hard links: {source}")
    ensure_within(source, ingest, "source")
    journal = vault / ".llm-wiki-transaction.json"
    if journal.exists() or is_reparse_point(journal):
        raise WikiError(f"unfinished transaction journal requires recovery before planning or writing: {journal}")

    digest = sha256_file(source)
    size = source.stat().st_size
    metadata = source_metadata(source)
    normalized_url = metadata.get("normalized_url")
    records = all_manifest_records(vault)
    target_rel = relative_posix(wiki, vault)
    exact = [record for record in records if record.get("sha256") == digest]
    if exact:
        same_owner = any(record.get("_wiki") == target_rel for record in exact)
        dependencies = definition.get("evidence_wikis")
        approved_owner = isinstance(dependencies, list) and any(
            record.get("_wiki_id") in dependencies for record in exact
        )
        emit(
            {
                "status": "already_processed",
                "source": relative_posix(source, vault),
                "sha256": digest,
                "matches": [
                    {"wiki": r.get("_wiki"), "wiki_id": r.get("_wiki_id"), "raw_path": r.get("raw_path")}
                    for r in exact
                ],
                "action": (
                    "cite the existing canonical raw in this wiki; source removal requires authorization"
                    if same_owner
                    else (
                        "cite the canonical raw through the existing evidence_wikis dependency; source removal "
                        "requires authorization"
                        if approved_owner
                        else "source left in _ingest; removal requires authorization, or approve an evidence_wikis "
                        "dependency on the canonical owner's wiki_id"
                    )
                ),
            }
        )
        return 0

    url_matches = [
        record
        for record in records
        if normalized_url and normalize_url(record.get("source_url")) == normalized_url
    ]
    target_versions = [record for record in url_matches if record.get("_wiki") == target_rel]
    raws = wiki_owned_path(definition, "raws", vault, wiki)
    ensure_within(raws, wiki, "raws path")
    destination, collision = collision_safe_path(raws, source)
    status = "versioned" if target_versions else "processed"
    planned = {
        "status": status,
        "source": relative_posix(source, vault),
        "raw_path": relative_posix(destination, vault),
        "sha256": digest,
        "bytes": size,
        "collision_resolved": collision,
        "previous_raws": [record.get("raw_path") for record in target_versions],
        "metadata": {key: value for key, value in metadata.items() if key != "normalized_url"},
    }
    if args.dry_run:
        planned["dry_run"] = True
        emit(planned)
        return 0

    original_path = relative_posix(source, vault)
    record: dict[str, Any] = {
        "schema": 1,
        "state": status,
        "raw_path": relative_posix(destination, vault),
        "original_path": original_path,
        "sha256": digest,
        "bytes": size,
        "recorded_at": utc_now(),
        "source_type": metadata.get("source_type"),
    }
    for key in ("source_url", "captured_at", "published_at", "author"):
        if metadata.get(key):
            record[key] = metadata[key]
    if target_versions:
        record["previous_raws"] = [value for value in planned["previous_raws"] if value]
    manifest = manifest_path_for(wiki, definition, vault)
    transaction = {
        "schema": 1,
        "operation": "move-raw",
        "phase": "prepared",
        "source": original_path,
        "destination": relative_posix(destination, vault),
        "manifest": relative_posix(manifest, vault),
        "sha256": digest,
        "record": record,
        "recorded_at": utc_now(),
    }
    write_json_atomic(journal, transaction)
    try:
        source.rename(destination)
        transaction["phase"] = "raw_moved"
        write_json_atomic(journal, transaction)
        moved_digest = sha256_file(destination)
        if moved_digest != digest:
            raise WikiError(f"moved raw failed byte verification: {destination}")
        append_manifest(manifest, record)
    except Exception as exc:
        try:
            if destination.exists() and not source.exists():
                destination.rename(source)
        except OSError as rollback_exc:
            raise WikiError(
                f"raw move failed and rollback also failed; recover {destination} manually: {rollback_exc}"
            ) from exc
        try:
            journal.unlink()
        except OSError as journal_exc:
            raise WikiError(f"raw rollback succeeded but transaction journal cleanup failed: {journal}") from journal_exc
        raise
    try:
        journal.unlink()
    except OSError as exc:
        raise WikiError(f"raw and manifest committed; inspect and remove completed transaction journal: {journal}") from exc
    planned["manifest"] = relative_posix(manifest, vault)
    planned["byte_verified"] = True
    emit(planned)
    return 0


def command_move_raw(args: argparse.Namespace) -> int:
    prepared = load_target_wiki(args.wiki)
    if args.dry_run:
        lock = prepared[0] / ".llm-wiki.lock"
        if lock.exists() or is_reparse_point(lock):
            raise WikiError(f"write lock is active or stale; dry-run cannot inspect a stable snapshot: {lock}")
        return move_raw_once(args, prepared)
    vault = prepared[0]
    with exclusive_vault_lock(vault):
        return move_raw_once(args, load_target_wiki(args.wiki))


def add_issue(issues: list[dict[str, str]], severity: str, path: Path, vault: Path, message: str) -> None:
    try:
        display_path = relative_posix(path, vault)
    except ValueError:
        display_path = str(path)
    issues.append({"severity": severity, "path": display_path, "message": message})


def scan_tree_files(root: Path, issues: list[dict[str, str]], vault: Path) -> list[Path]:
    files: list[Path] = []
    if is_reparse_point(root):
        add_issue(issues, "error", root, vault, "directory is a symlink, junction, or reparse point")
        return files
    stack = [root]
    while stack:
        directory = stack.pop()
        try:
            with os.scandir(directory) as iterator:
                entries = sorted(iterator, key=lambda entry: entry.name.casefold())
        except OSError as exc:
            add_issue(issues, "error", directory, vault, f"cannot scan directory: {exc}")
            continue
        for entry in entries:
            path = Path(entry.path)
            if entry.name.casefold() in SKIP_DIRS_CASEFOLD:
                continue
            if is_reparse_point(path):
                add_issue(issues, "error", path, vault, "entry is a symlink, junction, or reparse point")
                continue
            try:
                if entry.is_dir(follow_symlinks=False):
                    stack.append(path)
                elif entry.is_file(follow_symlinks=False):
                    files.append(path)
            except OSError as exc:
                add_issue(issues, "error", path, vault, f"cannot inspect entry: {exc}")
    return sorted(files)


def resolve_note_target(
    target: str,
    wiki: Path,
    allowed: set[Path],
    by_stem: dict[str, list[Path]],
) -> tuple[str, Path | None]:
    cleaned = target.strip().replace("\\", "/")
    candidate = Path(cleaned)
    if candidate.is_absolute() or ".." in candidate.parts:
        return "escape", None
    variants = [candidate, Path(str(candidate) + ".md")] if candidate.suffix and candidate.suffix.lower() != ".md" else [candidate]
    if not candidate.suffix:
        variants = [candidate.with_suffix(".md"), candidate]
    for variant in variants:
        candidates = [wiki.parent / variant] if variant.parts and variant.parts[0].casefold() == wiki.name.casefold() else [wiki / variant, wiki.parent / variant]
        for lexical in candidates:
            try:
                exact = resolve_contained(lexical, wiki.parent, "wikilink")
            except WikiError:
                return "escape", None
            if exact in allowed:
                return "ok", exact
    if candidate.suffix and candidate.suffix.lower() != ".md":
        return "missing", None
    matches = by_stem.get(candidate.stem.casefold(), [])
    if len(matches) == 1:
        return "ok", matches[0]
    if len(matches) > 1:
        return "ambiguous", None
    return "missing", None


def evidence_dependency_paths(
    vault: Path,
    wiki: Path,
    definition: dict[str, Any],
    issues: list[dict[str, str]],
) -> set[Path]:
    requested = definition.get("evidence_wikis")
    if not isinstance(requested, list) or not requested:
        return set()
    current_id = definition.get("wiki_id")
    candidates: dict[str, list[tuple[Path, dict[str, Any]]]] = {}
    for root in root_wiki_candidates(vault):
        note = root / "Wiki.md"
        if not note.is_file() or is_reparse_point(note):
            continue
        try:
            candidate_definition = read_frontmatter(note)
        except (OSError, WikiError):
            continue
        candidate_id = candidate_definition.get("wiki_id")
        if is_definition(candidate_definition) and isinstance(candidate_id, str):
            candidates.setdefault(candidate_id, []).append((root, candidate_definition))

    allowed: set[Path] = set()
    for dependency_id in requested:
        if dependency_id == current_id:
            add_issue(issues, "error", wiki / "Wiki.md", vault, f"evidence_wikis contains its own wiki_id: {dependency_id}")
            continue
        matches = candidates.get(dependency_id, [])
        if len(matches) != 1:
            reason = "missing" if not matches else "ambiguous duplicate"
            add_issue(issues, "error", wiki / "Wiki.md", vault, f"{reason} evidence_wikis dependency: {dependency_id}")
            continue
        owner, owner_definition = matches[0]
        owner_problems = definition_errors(owner_definition)
        if owner_problems:
            add_issue(
                issues,
                "error",
                owner / "Wiki.md",
                vault,
                f"invalid evidence dependency {dependency_id}: {'; '.join(owner_problems)}",
            )
            continue
        try:
            if configured_path(owner_definition, "root", vault) != owner:
                raise WikiError("dependency definition root does not match its folder")
            owner_raws = wiki_owned_path(owner_definition, "raws", vault, owner)
            owner_manifest = manifest_path_for(owner, owner_definition, vault)
            if not owner_manifest.is_file() or is_reparse_point(owner_manifest):
                raise WikiError(f"dependency manifest is missing or unsafe: {owner_manifest}")
            records, manifest_problems = load_manifest(owner_manifest)
        except (OSError, UnicodeDecodeError, WikiError) as exc:
            add_issue(issues, "error", owner / "Wiki.md", vault, f"cannot load evidence dependency {dependency_id}: {exc}")
            continue
        for message in manifest_problems:
            add_issue(issues, "error", owner_manifest, vault, f"dependency {dependency_id}: {message}")
        if manifest_problems:
            continue
        for record in records:
            record_problems, raw_path = manifest_record_errors(
                record, vault, owner, owner_raws, verify_bytes=True
            )
            for message in record_problems:
                add_issue(issues, "error", owner_manifest, vault, f"dependency {dependency_id}: {message}")
            if raw_path is not None and not record_problems:
                allowed.add(raw_path)
    return allowed


def audit_wiki(vault: Path, wiki: Path, issues: list[dict[str, str]]) -> None:
    note = wiki / "Wiki.md"
    if is_reparse_point(note):
        add_issue(issues, "error", note, vault, "definition note is a symlink, junction, or reparse point")
        return
    try:
        definition = read_frontmatter(note)
    except (OSError, WikiError) as exc:
        add_issue(issues, "error", note, vault, str(exc))
        return
    if not is_definition(definition):
        add_issue(issues, "error", note, vault, "first YAML block is missing llm_wiki: true")
        return
    definition_problems = definition_errors(definition)
    for message in definition_problems:
        add_issue(issues, "error", note, vault, message)
    if definition_problems:
        return

    try:
        required = validated_wiki_layout(definition, vault, wiki)
    except WikiError as exc:
        add_issue(issues, "error", note, vault, str(exc))
        return

    raws = required["raws"]
    manifest = required["manifest"]
    try:
        records, manifest_errors = load_manifest(manifest)
    except (OSError, UnicodeDecodeError) as exc:
        add_issue(issues, "error", manifest, vault, f"cannot read manifest: {exc}")
        records, manifest_errors = [], []
    for message in manifest_errors:
        add_issue(issues, "error", manifest, vault, message)
    for message in manifest_lineage_errors(records):
        add_issue(issues, "error", manifest, vault, message)

    registered: dict[str, dict[str, Any]] = {}
    seen_hashes: set[str] = set()
    for record in records:
        record_problems, raw_path = manifest_record_errors(record, vault, wiki, raws, verify_bytes=True)
        for message in record_problems:
            add_issue(issues, "error", manifest, vault, message)
        if raw_path is None:
            continue
        raw_key = relative_posix(raw_path, vault)
        digest = record.get("sha256")
        if raw_key in registered:
            add_issue(issues, "error", manifest, vault, f"duplicate raw_path: {raw_key}")
        if isinstance(digest, str) and digest in seen_hashes:
            add_issue(issues, "error", manifest, vault, f"duplicate SHA-256: {digest}")
        registered[raw_key] = record
        if isinstance(digest, str):
            seen_hashes.add(digest)

    for raw in scan_tree_files(raws, issues, vault):
        raw_key = relative_posix(raw, vault)
        if raw_key not in registered:
            add_issue(issues, "error", raw, vault, "raw is not registered in manifest.jsonl")

    page_folders: dict[str, Path] = {
        key: required[key] for key in definition.get("files", {}) if key in required
    }
    page_folders["outputs"] = required["outputs"]
    compiled: list[Path] = []
    folder_for_page: dict[Path, str] = {}
    for key, folder in page_folders.items():
        for page in scan_tree_files(folder, issues, vault):
            if page.suffix.lower() == ".md":
                compiled.append(page)
                folder_for_page[page] = key
    compiled = sorted(set(compiled))

    page_types = definition.get("page_types")
    if not isinstance(page_types, dict):
        page_types = {"concepts": "concept", "entities": "entity", "decisions": "decision", "outputs": "output"}
    statuses_value = definition.get("page_statuses")
    statuses = set(statuses_value) if isinstance(statuses_value, list) and statuses_value else PAGE_STATUSES
    page_fields = definition.get("page_fields")
    if not isinstance(page_fields, dict):
        page_fields = {key: key for key in ("wiki_id", "page_type", "status", "sources")}

    registered_paths = {resolve_contained(vault / path, vault, "registered raw") for path in registered}
    evidence_paths = registered_paths | evidence_dependency_paths(vault, wiki, definition, issues)
    static_notes = {note, required["index"], required["log"]}
    allowed = set(compiled) | static_notes | evidence_paths
    by_stem: dict[str, list[Path]] = {}
    for path in set(compiled) | static_notes:
        by_stem.setdefault(path.stem.casefold(), []).append(path)

    page_text: dict[Path, str] = {}
    for page in compiled:
        try:
            frontmatter = read_frontmatter(page)
            text = page.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError, WikiError) as exc:
            add_issue(issues, "error", page, vault, f"cannot read compiled page: {exc}")
            continue
        page_text[page] = strip_markdown_code(text)
        for semantic_key, field_name in page_fields.items():
            if field_name not in frontmatter:
                add_issue(issues, "error", page, vault, f"missing {semantic_key} field: {field_name}")
        if frontmatter.get(page_fields["wiki_id"]) != definition.get("wiki_id"):
            add_issue(issues, "error", page, vault, f"{page_fields['wiki_id']} does not match Wiki.md")
        expected_type = page_types.get(folder_for_page[page])
        actual_type = frontmatter.get(page_fields["page_type"])
        if not isinstance(actual_type, str) or not actual_type:
            add_issue(issues, "error", page, vault, f"{page_fields['page_type']} must be non-empty text")
        elif expected_type and actual_type != expected_type:
            add_issue(issues, "error", page, vault, f"{page_fields['page_type']} must be {expected_type}")
        if frontmatter.get(page_fields["status"]) not in statuses:
            add_issue(
                issues,
                "error",
                page,
                vault,
                f"{page_fields['status']} must be one of: {', '.join(sorted(statuses))}",
            )
        sources = frontmatter.get(page_fields["sources"])
        if not isinstance(sources, list) or not sources:
            add_issue(issues, "error", page, vault, f"{page_fields['sources']} must be a non-empty list")
        else:
            for source_value in sources:
                if not isinstance(source_value, str) or not source_value:
                    add_issue(issues, "error", page, vault, "source path must be non-empty text")
                    continue
                try:
                    source_path = resolve_contained(vault / source_value, vault, "page source")
                except WikiError as exc:
                    add_issue(issues, "error", page, vault, str(exc))
                    continue
                if source_path not in evidence_paths:
                    add_issue(
                        issues,
                        "error",
                        page,
                        vault,
                        f"source is not registered locally or by an approved evidence_wikis dependency: {source_value}",
                    )

    try:
        index_text = required["index"].read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        add_issue(issues, "error", required["index"], vault, f"cannot read index: {exc}")
        index_text = ""
    try:
        log_text = required["log"].read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        add_issue(issues, "error", required["log"], vault, f"cannot read log: {exc}")
        log_text = ""

    indexed: set[Path] = set()
    for target in WIKILINK_RE.findall(strip_markdown_code(index_text)):
        state, resolved = resolve_note_target(target, wiki, allowed, by_stem)
        if state == "ok" and resolved is not None:
            if resolved in compiled:
                indexed.add(resolved)
        else:
            severity = "error" if state == "escape" else "warning"
            add_issue(issues, severity, required["index"], vault, f"{state} wikilink: {target}")
    for page in compiled:
        if page not in indexed:
            add_issue(issues, "warning", page, vault, "compiled page is not linked from index.md")

    inbound = {page: 0 for page in compiled}
    outbound = {page: 0 for page in compiled}
    for page, text in page_text.items():
        for target in WIKILINK_RE.findall(text):
            state, resolved = resolve_note_target(target, wiki, allowed, by_stem)
            if state == "ok" and resolved is not None:
                if resolved in inbound and resolved != page:
                    inbound[resolved] += 1
                    outbound[page] += 1
            else:
                severity = "error" if state == "escape" else "warning"
                add_issue(issues, severity, page, vault, f"{state} wikilink: {target}")
    for page in compiled:
        if inbound[page] == 0 and outbound[page] == 0:
            add_issue(issues, "info", page, vault, "compiled page has no cross-page links; inspect for an orphan or missed concept")

    duplicate_stems: dict[str, list[Path]] = {}
    for page in compiled:
        duplicate_stems.setdefault(page.stem.casefold(), []).append(page)
    for pages in duplicate_stems.values():
        if len(pages) > 1:
            for page in pages:
                add_issue(issues, "warning", page, vault, "duplicate compiled page basename")

    for raw_key, record in registered.items():
        digest = record.get("sha256")
        if raw_key not in log_text or not isinstance(digest, str) or digest not in log_text:
            add_issue(issues, "warning", required["log"], vault, f"manifest record is not fully represented in log: {raw_key}")


def command_audit(args: argparse.Namespace) -> int:
    vault = resolve_existing_dir(args.vault, "vault")
    issues: list[dict[str, str]] = []
    lock = vault / ".llm-wiki.lock"
    if lock.exists() or is_reparse_point(lock):
        add_issue(
            issues,
            "error",
            lock,
            vault,
            "write lock is active or stale; retry after the writer finishes or inspect it before removal",
        )
    journal = vault / ".llm-wiki-transaction.json"
    if journal.exists() or is_reparse_point(journal):
        add_issue(
            issues,
            "error",
            journal,
            vault,
            "unfinished move transaction requires recovery; compare its source, destination, manifest, and digest",
        )

    definitions: list[tuple[Path, dict[str, Any]]] = []
    for wiki in root_wiki_candidates(vault):
        note = wiki / "Wiki.md"
        if not note.is_file():
            add_issue(issues, "warning", wiki, vault, "candidate wiki has no Wiki.md")
            continue
        if is_reparse_point(note):
            add_issue(issues, "error", note, vault, "candidate Wiki.md is a reparse point")
            continue
        try:
            frontmatter = read_frontmatter(note)
        except (OSError, WikiError) as exc:
            add_issue(issues, "error", note, vault, f"cannot read definition: {exc}")
            continue
        if not is_definition(frontmatter):
            add_issue(issues, "warning", note, vault, "candidate Wiki.md is not an llm-wiki definition")
            continue
        definitions.append((wiki, frontmatter))
        audit_wiki(vault, wiki, issues)
    if not definitions:
        add_issue(issues, "error", vault, vault, "no valid root-level llm-wiki definition found")

    wiki_ids: dict[str, list[Path]] = {}
    for wiki, definition in definitions:
        wiki_id = definition.get("wiki_id")
        if isinstance(wiki_id, str):
            wiki_ids.setdefault(wiki_id, []).append(wiki)
    for wiki_id, roots in wiki_ids.items():
        if len(roots) > 1:
            for root in roots:
                add_issue(issues, "error", root / "Wiki.md", vault, f"duplicate wiki_id: {wiki_id}")

    hash_owners: dict[str, list[tuple[str, Path, str]]] = {}
    path_owners: dict[str, list[tuple[str, Path]]] = {}
    for wiki, definition in definitions:
        if definition_errors(definition):
            continue
        try:
            layout = validated_wiki_layout(definition, vault, wiki)
            records, manifest_errors = load_manifest(layout["manifest"])
        except (OSError, WikiError):
            continue
        if manifest_errors:
            continue
        wiki_id = definition.get("wiki_id")
        if not isinstance(wiki_id, str):
            continue
        for record in records:
            digest = record.get("sha256")
            raw_path = record.get("raw_path")
            if isinstance(digest, str) and isinstance(raw_path, str):
                hash_owners.setdefault(digest, []).append((wiki_id, layout["manifest"], raw_path))
                path_owners.setdefault(raw_path, []).append((wiki_id, layout["manifest"]))
    for digest, owners in hash_owners.items():
        if len({owner[0] for owner in owners}) > 1:
            for wiki_id, manifest, raw_path in owners:
                add_issue(
                    issues,
                    "error",
                    manifest,
                    vault,
                    f"SHA-256 has multiple manifest owners; keep one canonical raw: {digest} ({wiki_id}:{raw_path})",
                )
    for raw_path, owners in path_owners.items():
        if len({owner[0] for owner in owners}) > 1:
            for wiki_id, manifest in owners:
                add_issue(
                    issues,
                    "error",
                    manifest,
                    vault,
                    f"raw_path has multiple manifest owners: {raw_path} ({wiki_id})",
                )

    ingest = vault / "_ingest"
    if is_reparse_point(ingest):
        add_issue(issues, "error", ingest, vault, "_ingest is a symlink, junction, or reparse point")
    elif not ingest.is_dir():
        add_issue(issues, "warning", ingest, vault, "vault-root _ingest directory is missing")
    else:
        for path in scan_tree_files(ingest, issues, vault):
            if path.stat().st_nlink != 1:
                add_issue(issues, "error", path, vault, "intake file has multiple hard links")

    counts = {severity: sum(issue["severity"] == severity for issue in issues) for severity in ("error", "warning", "info")}
    emit(
        {
            "vault": str(vault),
            "wiki_count": len(definitions),
            "counts": counts,
            "issues": sorted(
                issues,
                key=lambda item: (
                    {"error": 0, "warning": 1, "info": 2}[item["severity"]],
                    item["path"],
                    item["message"],
                ),
            ),
        }
    )
    return 1 if counts["error"] else 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    discover = subparsers.add_parser("discover", help="List root-level llm-wiki definitions and ingest entries")
    discover.add_argument("vault")
    discover.set_defaults(handler=command_discover)

    scaffold = subparsers.add_parser("scaffold", help="Create an explicitly requested default wiki")
    scaffold.add_argument("vault")
    scaffold.add_argument("folder")
    scaffold.add_argument("wiki_id")
    scaffold.add_argument("--name", help="Display name; defaults to folder")
    scaffold.set_defaults(handler=command_scaffold)

    move_raw = subparsers.add_parser("move-raw", help="File one _ingest source into a configured wiki")
    move_raw.add_argument("source")
    move_raw.add_argument("wiki")
    move_raw.add_argument("--dry-run", action="store_true")
    move_raw.set_defaults(handler=command_move_raw)

    audit = subparsers.add_parser("audit", help="Run deterministic structural and provenance checks")
    audit.add_argument("vault")
    audit.set_defaults(handler=command_audit)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        return int(args.handler(args))
    except (OSError, WikiError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
