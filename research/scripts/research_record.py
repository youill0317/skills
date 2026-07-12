#!/usr/bin/env python3
"""Create and validate a compact, auditable Markdown research record."""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
import re
import sys
import unicodedata


sys.dont_write_bytecode = True
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")


FINAL_STATUSES = {"complete", "complete-with-gaps", "insufficient"}
CONFIDENCE_VALUES = {"high", "medium", "low", "insufficient"}
REQUIRED_METADATA = ("Created", "As of", "Question", "Scope", "Access", "Status")
REQUIRED_AUDIT_FIELDS = (
    "Evidence coverage",
    "Counterevidence and conflicts",
    "Currentness and provenance",
    "Gaps",
    "Confidence",
    "Stop decision",
)
SOURCE_HEADER = [
    "id",
    "source / locator",
    "inspected location",
    "accessed / version",
    "key observation",
]
PLACEHOLDER_RE = re.compile(r"\b(?:FILLME|TODO|TBD)\b", re.IGNORECASE)
SOURCE_ID_RE = re.compile(r"S[1-9]\d*")
VALID_CITATION_RE = re.compile(
    r"\[(?P<ids>S[1-9]\d*(?:\s*,\s*S[1-9]\d*)*)\]"
)
ANY_SOURCE_MARK_RE = re.compile(r"\[S\d|(?<![\[\w])S\d+\b")


class RecordError(Exception):
    """CLI or filesystem error."""


def normalize(value: str) -> str:
    return " ".join(value.strip().split()).lower()


def slugify(topic: str) -> str:
    normalized = unicodedata.normalize("NFKC", topic).lower()
    pieces: list[str] = []
    previous_dash = False
    for char in normalized:
        if char.isalnum():
            pieces.append(char)
            previous_dash = False
        elif not previous_dash:
            pieces.append("-")
            previous_dash = True
    return re.sub(r"-{2,}", "-", "".join(pieces)).strip("-")[:60] or "research"


def strip_fenced_code(text: str) -> str:
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    return text


def section_body(text: str, heading: str) -> str:
    match = re.search(
        rf"^##\s+{re.escape(heading)}\s*$\n(?P<body>.*?)(?=^##\s+|\Z)",
        text,
        flags=re.MULTILINE | re.DOTALL,
    )
    return match.group("body").strip() if match else ""


def metadata_value(text: str, key: str) -> str | None:
    match = re.search(rf"^{re.escape(key)}:\s*(?P<value>.+?)\s*$", text, re.MULTILINE)
    return match.group("value").strip() if match else None


def audit_value(text: str, key: str) -> str | None:
    match = re.search(rf"^-\s+{re.escape(key)}:\s*(?P<value>.+?)\s*$", text, re.MULTILINE)
    return match.group("value").strip() if match else None


def confidence_label(value: str) -> str:
    match = re.match(r"^(high|medium|low|insufficient)\b", normalize(value))
    return match.group(1) if match else normalize(value)


def states_no_material_gap(value: str) -> bool:
    normalized = normalize(value).strip(" .;:")
    return normalized == "none" or normalized.startswith(
        ("none —", "none -", "no material gap", "no unresolved material gap")
    )


def split_table_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def is_separator_row(cells: list[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells)


def table_rows(body: str) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in body.splitlines():
        stripped = line.strip()
        if not (stripped.startswith("|") and stripped.endswith("|")):
            continue
        cells = split_table_row(stripped)
        if not is_separator_row(cells):
            rows.append(cells)
    return rows


def citation_ids(text: str) -> set[str]:
    found: set[str] = set()
    for match in VALID_CITATION_RE.finditer(text):
        found.update(part.strip() for part in match.group("ids").split(","))
    return found


def answer_blocks(answer: str) -> list[str]:
    lines = strip_fenced_code(answer).splitlines()
    blocks: list[str] = []
    paragraph: list[str] = []
    in_table = False
    table_row_index = 0

    def flush() -> None:
        if paragraph:
            blocks.append(" ".join(part.strip() for part in paragraph).strip())
            paragraph.clear()

    for index, line in enumerate(lines):
        stripped = line.strip()
        if not stripped:
            flush()
            in_table = False
            table_row_index = 0
            continue
        if stripped.startswith("|") and stripped.endswith("|"):
            flush()
            cells = split_table_row(stripped)
            if is_separator_row(cells):
                in_table = True
                continue
            if not in_table and index + 1 < len(lines):
                next_cells = split_table_row(lines[index + 1].strip()) if lines[index + 1].strip().startswith("|") else []
                if is_separator_row(next_cells):
                    in_table = True
                    table_row_index = 0
                    continue
            table_row_index += 1
            blocks.append(stripped)
            continue
        if re.match(r"^(?:[-*+]\s+|\d+[.)]\s+)", stripped):
            flush()
            blocks.append(stripped)
            continue
        paragraph.append(stripped)
    flush()
    return [block for block in blocks if block]


def parse_sources(text: str, failures: list[str], allow_draft: bool) -> dict[str, list[str]]:
    heading_count = len(re.findall(r"^##\s+Sources\s*$", text, re.MULTILINE))
    if heading_count > 1:
        failures.append("Sources section must appear at most once")
        return {}
    if heading_count == 0:
        return {}

    rows = table_rows(section_body(text, "Sources"))
    if not rows:
        if not allow_draft:
            failures.append("Sources section must contain a header and at least one source row")
        return {}
    if [normalize(cell) for cell in rows[0]] != SOURCE_HEADER:
        failures.append("Sources table header does not match the required schema")
        return {}

    if len(rows) == 1 and not allow_draft:
        failures.append("Sources section must contain at least one inspected source row")

    sources: dict[str, list[str]] = {}
    for index, row in enumerate(rows[1:], start=1):
        if len(row) != len(SOURCE_HEADER):
            failures.append(f"Sources row {index} must have {len(SOURCE_HEADER)} columns")
            continue
        source_id = row[0]
        if not SOURCE_ID_RE.fullmatch(source_id):
            failures.append(f"Sources row {index} has invalid ID {source_id!r}")
            continue
        if source_id in sources:
            failures.append(f"duplicate source ID: {source_id}")
        if any(not cell.strip() for cell in row[1:]):
            failures.append(f"Sources row {index} has an empty required field")
        sources[source_id] = row
    return sources


def validate_text(text: str, allow_draft: bool = False) -> list[str]:
    failures: list[str] = []
    structure = strip_fenced_code(text)

    if not re.match(r"\A#\s+Research:\s+\S+", structure):
        failures.append("record must start with '# Research: <Topic>'")
    if len(re.findall(r"^#\s+Research:\s+\S+", structure, re.MULTILINE)) != 1:
        failures.append("record must contain exactly one research title")

    for key in REQUIRED_METADATA:
        matches = re.findall(rf"^{re.escape(key)}:\s*(.+?)\s*$", structure, re.MULTILINE)
        value = matches[0].strip() if matches else None
        if not value:
            failures.append(f"missing or empty metadata: {key}")
        if len(matches) > 1:
            failures.append(f"metadata must appear exactly once: {key}")

    status = normalize(metadata_value(structure, "Status") or "")
    allowed_statuses = FINAL_STATUSES | ({"draft"} if allow_draft else set())
    if status not in allowed_statuses:
        failures.append(f"unsupported Status: {status!r}")

    for heading in ("Answer", "Audit"):
        count = len(re.findall(rf"^##\s+{heading}\s*$", structure, re.MULTILINE))
        if count != 1:
            failures.append(f"{heading} section must appear exactly once")
        elif not section_body(structure, heading):
            failures.append(f"{heading} section must not be empty")

    if not allow_draft and PLACEHOLDER_RE.search(structure):
        failures.append("final record contains a draft placeholder")

    audit = section_body(structure, "Audit")
    audit_fields: dict[str, str] = {}
    for key in REQUIRED_AUDIT_FIELDS:
        value = audit_value(audit, key)
        if not value:
            failures.append(f"missing or empty Audit field: {key}")
        else:
            audit_fields[key] = value

    confidence = confidence_label(audit_fields.get("Confidence", ""))
    if confidence and confidence not in CONFIDENCE_VALUES and not (allow_draft and status == "draft"):
        failures.append(f"unsupported confidence: {confidence!r}")

    gaps = normalize(audit_fields.get("Gaps", ""))
    no_material_gap = states_no_material_gap(gaps)
    if status == "complete":
        if not no_material_gap:
            failures.append("complete records must state that no material gap remains")
        if confidence == "insufficient":
            failures.append("complete records cannot have insufficient confidence")
    elif status == "complete-with-gaps":
        if not gaps or no_material_gap:
            failures.append("complete-with-gaps records must name a material gap")
        if confidence == "insufficient":
            failures.append("complete-with-gaps records cannot have insufficient confidence")
    elif status == "insufficient":
        if not gaps or no_material_gap:
            failures.append("insufficient records must name the missing core evidence")
        if confidence and confidence != "insufficient":
            failures.append("insufficient records must use insufficient confidence")

    sources = parse_sources(structure, failures, allow_draft)
    answer = section_body(structure, "Answer")
    answer_citations = citation_ids(answer)
    all_citations = citation_ids(answer + "\n" + audit)

    answer_without_valid_citations = VALID_CITATION_RE.sub("", answer)
    if ANY_SOURCE_MARK_RE.search(answer_without_valid_citations):
        failures.append("Answer contains malformed or bare source references; use [S#]")

    unknown = all_citations - set(sources)
    for source_id in sorted(unknown):
        failures.append(f"citation references unknown source: {source_id}")

    unused = set(sources) - all_citations
    for source_id in sorted(unused):
        failures.append(f"source is not cited in Answer or Audit: {source_id}")

    if status in {"complete", "complete-with-gaps"} and not sources:
        failures.append(f"{status} records require at least one inspected source")

    blocks = answer_blocks(answer)
    if status in {"complete", "complete-with-gaps"}:
        for index, block in enumerate(blocks, start=1):
            if not citation_ids(block):
                failures.append(f"Answer claim block {index} lacks a claim-local [S#] citation")
    elif status == "insufficient":
        if not blocks or not normalize(blocks[0]).startswith("insufficient:"):
            failures.append("insufficient Answer must begin with 'Insufficient:'")
        for index, block in enumerate(blocks, start=1):
            if sources and not citation_ids(block) and not normalize(block).startswith("insufficient:"):
                failures.append(f"Answer claim block {index} lacks a claim-local [S#] citation")

    if answer_citations and not sources:
        failures.append("Answer cites sources but no Sources registry is present")
    return sorted(set(failures))


def build_record(topic: str, request: str, scope: str, access: str, as_of: str) -> str:
    created = datetime.now().astimezone().strftime("%Y-%m-%d")
    return f"""# Research: {topic}

Created: {created}
As of: {as_of}
Question: {request}
Scope: {scope}
Access: {access}
Status: draft

## Answer

FILLME

## Sources

| ID | Source / Locator | Inspected Location | Accessed / Version | Key Observation |
|---|---|---|---|---|

## Audit

- Evidence coverage: FILLME
- Counterevidence and conflicts: FILLME
- Currentness and provenance: FILLME
- Gaps: FILLME
- Confidence: FILLME
- Stop decision: FILLME
"""


def resolve_record_dir(root_value: str, record_dir_value: str) -> tuple[Path, Path]:
    root = Path(root_value).resolve()
    if not root.is_dir():
        raise RecordError(f"workspace root does not exist or is not a directory: {root}")
    requested = Path(record_dir_value)
    if requested.is_absolute():
        raise RecordError("--record-dir must be relative to --root")
    record_dir = (root / requested).resolve()
    try:
        record_dir.relative_to(root)
    except ValueError as exc:
        raise RecordError("--record-dir resolves outside --root") from exc
    return root, record_dir


def next_record_path(record_dir: Path, topic: str) -> Path:
    highest = 0
    if record_dir.exists():
        for path in record_dir.glob("*.md"):
            match = re.match(r"^(\d+)-", path.name)
            if match:
                highest = max(highest, int(match.group(1)))
    return record_dir / f"{highest + 1:03d}-{slugify(topic)}.md"


def command_scaffold(args: argparse.Namespace) -> int:
    _, record_dir = resolve_record_dir(args.root, args.record_dir)
    path = next_record_path(record_dir, args.topic)
    if args.dry_run:
        print(path)
        return 0

    record_dir.mkdir(parents=True, exist_ok=True)
    record = build_record(
        args.topic,
        args.request,
        args.scope,
        args.access,
        args.as_of or datetime.now().astimezone().isoformat(timespec="minutes"),
    )
    try:
        with path.open("x", encoding="utf-8", newline="\n") as handle:
            handle.write(record)
    except FileExistsError as exc:
        raise RecordError(f"record already exists: {path}") from exc
    print(path)
    return 0


def command_validate(args: argparse.Namespace) -> int:
    record = Path(args.record)
    if record.suffix.lower() != ".md":
        print("Research record validation failed:\n- record must be Markdown", file=sys.stderr)
        return 1
    try:
        text = record.read_text(encoding="utf-8")
    except OSError as exc:
        raise RecordError(f"cannot read record: {exc}") from exc
    failures = validate_text(text, allow_draft=args.allow_draft)
    if failures:
        print("Research record validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print(
        "Structural, citation, and status consistency validation passed. "
        "Source truth and claim entailment still require evidence review."
    )
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Create or validate one compact Markdown research record."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    scaffold = subparsers.add_parser(
        "scaffold",
        help="Create the next workspace-contained draft record and print its path.",
    )
    scaffold.add_argument("--topic", required=True, help="Short record title and filename seed.")
    scaffold.add_argument("--request", required=True, help="Exact research question or request.")
    scaffold.add_argument("--scope", required=True, help="Included boundary and material exclusions.")
    scaffold.add_argument("--root", required=True, help="Existing workspace root that contains the record.")
    scaffold.add_argument(
        "--record-dir",
        default="research",
        help="Relative directory under --root; absolute and escaping paths are rejected.",
    )
    scaffold.add_argument(
        "--access",
        default="Authorized read sources; workspace-local record; disclose blocked access",
        help="Authorized and blocked source boundary recorded in metadata.",
    )
    scaffold.add_argument("--as-of", help="Evidence cutoff timestamp; defaults to local current time.")
    scaffold.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the resolved output path without creating directories or files.",
    )
    scaffold.set_defaults(handler=command_scaffold)

    validate = subparsers.add_parser(
        "validate",
        help="Check structure, claim-local citations, source IDs, and status consistency.",
    )
    validate.add_argument("record", help="Markdown record path. Missing or unreadable files return exit 2.")
    validate.add_argument(
        "--allow-draft",
        action="store_true",
        help="Allow Status: draft and scaffold placeholders during editing.",
    )
    validate.set_defaults(handler=command_validate)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        return args.handler(args)
    except RecordError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    except OSError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
