#!/usr/bin/env python3
"""Verify research skill packaging and deterministic record behavior."""

from __future__ import annotations

from pathlib import Path
import re
import subprocess
import sys
import tempfile


sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
RECORD_SCRIPT = ROOT / "scripts" / "research_record.py"
MAX_SKILL_BODY_WORDS = 600  # Token-budget guard, not a behavior-quality score.


def run_record(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-B", str(RECORD_SCRIPT), *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )


def write_record(path: Path, text: str) -> None:
    path.write_text(text.strip() + "\n", encoding="utf-8")


def record_text(
    *,
    status: str,
    answer: str,
    sources: str,
    gaps: str,
    confidence: str,
) -> str:
    source_section = f"\n## Sources\n\n{sources.strip()}\n" if sources.strip() else ""
    return f"""# Research: Contract Case

Created: 2026-07-13
As of: 2026-07-13T00:00+09:00
Question: Verify a material claim
Scope: Synthetic local evidence only
Access: Local read-only corpus and one workspace record
Status: {status}

## Answer

{answer}
{source_section}
## Audit

- Evidence coverage: governing source and material counterevidence checked [S1]
- Counterevidence and conflicts: no unresolved conflict
- Currentness and provenance: effective version and source authority checked [S1]
- Gaps: {gaps}
- Confidence: {confidence}
- Stop decision: no reachable material evidence need could change the result
"""


SOURCE_TABLE = """| ID | Source / Locator | Inspected Location | Accessed / Version | Key Observation |
|---|---|---|---|---|
| S1 | Governing record / local fixture | section 2 | 2026-07-13 / v2 | The operative requirement is confirmed |"""


def check_frontmatter_and_resources(failures: list[str]) -> int:
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    parts = skill.split("---", 2)
    if len(parts) != 3 or parts[0].strip():
        failures.append("SKILL.md must start with YAML frontmatter")
        return 0
    frontmatter, body = parts[1], parts[2]
    keys = set(re.findall(r"^([A-Za-z0-9_-]+):", frontmatter, re.MULTILINE))
    if keys != {"name", "description"}:
        failures.append(f"SKILL.md frontmatter keys must be name and description only: {sorted(keys)}")
    if not re.search(r"^name:\s*research\s*$", frontmatter, re.MULTILINE):
        failures.append("SKILL.md must declare name: research")
    if "maximum-strength" not in frontmatter.lower() or "research-grade" not in frontmatter.lower():
        failures.append("SKILL.md description must state maximum-strength research-grade scope")

    invariant = "Always run maximum-strength research when this skill triggers."
    if body.count(invariant) != 1:
        failures.append("SKILL.md must state the maximum-strength effort invariant exactly once")
    body_words = len(re.findall(r"\S+", body))
    if body_words > MAX_SKILL_BODY_WORDS:
        failures.append(
            f"SKILL.md body exceeds the {MAX_SKILL_BODY_WORDS}-word token-budget guard"
        )

    resource_re = re.compile(r"(?<![A-Za-z0-9_.-])((?:references|scripts)/[A-Za-z0-9_.\-/]+\.(?:md|py))")
    referenced = set(resource_re.findall(skill))
    for relative in sorted(referenced):
        if not (ROOT / relative).is_file():
            failures.append(f"SKILL.md references missing resource: {relative}")
    for path in sorted((ROOT / "references").glob("*.md")):
        relative = path.relative_to(ROOT).as_posix()
        if relative not in referenced:
            failures.append(f"unlisted reference file: {relative}")
    for path in sorted((ROOT / "scripts").glob("*.py")):
        relative = path.relative_to(ROOT).as_posix()
        if path.name != "verify_package.py" and relative not in referenced:
            failures.append(f"unlisted runtime script: {relative}")

    agent = (ROOT / "agents" / "openai.yaml").read_text(encoding="utf-8")
    for key in ("display_name", "short_description", "default_prompt"):
        if not re.search(rf'^\s+{key}:\s+"[^"]+"\s*$', agent, re.MULTILINE):
            failures.append(f"agents/openai.yaml must contain quoted {key}")
    short_match = re.search(r'^\s+short_description:\s+"([^"]+)"\s*$', agent, re.MULTILINE)
    if short_match and not 25 <= len(short_match.group(1)) <= 64:
        failures.append("agents/openai.yaml short_description must contain 25-64 characters")
    prompt_match = re.search(r'^\s+default_prompt:\s+"([^"]+)"\s*$', agent, re.MULTILINE)
    if prompt_match and "$research" not in prompt_match.group(1):
        failures.append("agents/openai.yaml default_prompt must mention $research")
    return body_words


def expect_validation(
    directory: Path,
    name: str,
    text: str,
    expected_code: int,
    failures: list[str],
) -> None:
    path = directory / f"{name}.md"
    write_record(path, text)
    result = run_record("validate", str(path))
    if result.returncode != expected_code:
        output = (result.stdout + result.stderr).strip()
        failures.append(
            f"validation case {name} returned {result.returncode}, expected {expected_code}: {output}"
        )


def check_record_behavior(failures: list[str]) -> int:
    case_count = 0
    with tempfile.TemporaryDirectory(prefix="research-skill-eval-") as temp_value:
        temp = Path(temp_value)

        valid_complete = record_text(
            status="complete",
            answer="The operative requirement is confirmed. [S1]",
            sources=SOURCE_TABLE,
            gaps="No material gap remains inside the authorized boundary; external authentication is excluded.",
            confidence="High within the authorized corpus — direct governing evidence",
        )
        expect_validation(temp, "valid-complete", valid_complete, 0, failures)
        case_count += 1

        valid_gap = record_text(
            status="complete-with-gaps",
            answer="The core requirement is established, while one secondary measure remains unavailable. [S1]",
            sources=SOURCE_TABLE,
            gaps="the non-core raw measurement archive was inaccessible after distinct fallbacks",
            confidence="medium — core authority is direct; the secondary measure is blocked",
        )
        expect_validation(temp, "valid-gap", valid_gap, 0, failures)
        case_count += 1

        valid_insufficient = record_text(
            status="insufficient",
            answer="Insufficient: no source body was reachable for the decisive claim.",
            sources="",
            gaps="the decisive governing record and distinct fallback routes were inaccessible",
            confidence="insufficient — no inspected evidence supports a firm answer",
        ).replace("governing source and material counterevidence checked [S1]", "no source body was reachable").replace(
            "effective version and source authority checked [S1]", "not assessable without the source body"
        )
        expect_validation(temp, "valid-insufficient", valid_insufficient, 0, failures)
        case_count += 1

        missing_local_citation = record_text(
            status="complete",
            answer="The operative requirement is confirmed.",
            sources=SOURCE_TABLE,
            gaps="none",
            confidence="high — direct governing evidence",
        )
        expect_validation(temp, "invalid-uncited", missing_local_citation, 1, failures)
        case_count += 1

        unknown_citation = record_text(
            status="complete",
            answer="The operative requirement is confirmed. [S2]",
            sources=SOURCE_TABLE,
            gaps="none",
            confidence="high — direct governing evidence",
        )
        expect_validation(temp, "invalid-unknown", unknown_citation, 1, failures)
        case_count += 1

        malformed_citation = record_text(
            status="complete",
            answer="The operative requirement is confirmed. [S01]",
            sources=SOURCE_TABLE,
            gaps="none",
            confidence="high — direct governing evidence",
        )
        expect_validation(temp, "invalid-malformed", malformed_citation, 1, failures)
        case_count += 1

        source_table_two = SOURCE_TABLE + "\n| S2 | Independent record / local fixture | section 7 | 2026-07-13 / v1 | Independent corroboration |"
        valid_multiple = record_text(
            status="complete",
            answer="The governing record establishes the requirement. [S1]\n\nIndependent evidence corroborates it. [S2]",
            sources=source_table_two,
            gaps="none",
            confidence="high — direct and independent evidence",
        )
        expect_validation(temp, "valid-multiple-blocks", valid_multiple, 0, failures)
        case_count += 1

        duplicate_source = valid_complete.replace(
            "| S1 | Governing record / local fixture | section 2 | 2026-07-13 / v2 | The operative requirement is confirmed |",
            "| S1 | Governing record / local fixture | section 2 | 2026-07-13 / v2 | The operative requirement is confirmed |\n| S1 | Duplicate record | section 3 | 2026-07-13 / v2 | Duplicate ID |",
        )
        expect_validation(temp, "invalid-duplicate-source", duplicate_source, 1, failures)
        case_count += 1

        unused_source = valid_complete.replace(SOURCE_TABLE, source_table_two)
        expect_validation(temp, "invalid-unused-source", unused_source, 1, failures)
        case_count += 1

        complete_with_named_gap = record_text(
            status="complete",
            answer="The operative requirement is confirmed. [S1]",
            sources=SOURCE_TABLE,
            gaps="a material governing appendix remains inaccessible",
            confidence="medium — one material gap remains",
        )
        expect_validation(temp, "invalid-complete-gap", complete_with_named_gap, 1, failures)
        case_count += 1

        insufficient_high = valid_insufficient.replace(
            "- Confidence: insufficient — no inspected evidence supports a firm answer",
            "- Confidence: high — unsupported confidence",
        )
        expect_validation(temp, "invalid-insufficient-confidence", insufficient_high, 1, failures)
        case_count += 1

        bare_source = record_text(
            status="complete",
            answer="The operative requirement is confirmed by S1.",
            sources=SOURCE_TABLE,
            gaps="none",
            confidence="high — direct governing evidence",
        )
        expect_validation(temp, "invalid-bare-source", bare_source, 1, failures)
        case_count += 1

        code_only_citation = record_text(
            status="complete",
            answer="The operative requirement is confirmed.\n\n```text\n[S1]\n```",
            sources=SOURCE_TABLE,
            gaps="none",
            confidence="high — direct governing evidence",
        )
        expect_validation(temp, "invalid-code-only-citation", code_only_citation, 1, failures)
        case_count += 1

        empty_source_field = valid_complete.replace(
            "| S1 | Governing record / local fixture | section 2 | 2026-07-13 / v2 | The operative requirement is confirmed |",
            "| S1 | Governing record / local fixture |  | 2026-07-13 / v2 | The operative requirement is confirmed |",
        )
        expect_validation(temp, "invalid-empty-source-field", empty_source_field, 1, failures)
        case_count += 1

        empty_sources = valid_insufficient.replace(
            "\n## Audit\n",
            "\n## Sources\n\n| ID | Source / Locator | Inspected Location | Accessed / Version | Key Observation |\n|---|---|---|---|---|\n\n## Audit\n",
        )
        expect_validation(temp, "invalid-empty-sources", empty_sources, 1, failures)
        case_count += 1

        scaffold = run_record(
            "scaffold",
            "--topic",
            "Unicode 경계",
            "--request",
            "Create a draft",
            "--scope",
            "Local fixture",
            "--root",
            str(temp),
        )
        if scaffold.returncode != 0:
            failures.append(f"scaffold smoke test failed: {(scaffold.stdout + scaffold.stderr).strip()}")
        else:
            created = Path(scaffold.stdout.strip())
            if not created.is_file():
                failures.append("scaffold did not create the reported record path")
            draft_check = run_record("validate", str(created), "--allow-draft")
            if draft_check.returncode != 0:
                failures.append(
                    f"scaffold draft did not validate with --allow-draft: {(draft_check.stdout + draft_check.stderr).strip()}"
                )
            final_check = run_record("validate", str(created))
            if final_check.returncode == 0:
                failures.append("scaffold draft passed final validation without --allow-draft")
        case_count += 1

        escape = run_record(
            "scaffold",
            "--topic",
            "escape",
            "--request",
            "escape",
            "--scope",
            "local",
            "--root",
            str(temp),
            "--record-dir",
            "../outside",
            "--dry-run",
        )
        if escape.returncode == 0:
            failures.append("scaffold accepted a record directory outside the workspace root")
        absolute = run_record(
            "scaffold",
            "--topic",
            "absolute",
            "--request",
            "absolute",
            "--scope",
            "local",
            "--root",
            str(temp),
            "--record-dir",
            str(temp.parent),
            "--dry-run",
        )
        if absolute.returncode == 0:
            failures.append("scaffold accepted an absolute record directory")
        case_count += 2
    return case_count


def main() -> int:
    failures: list[str] = []
    body_words = check_frontmatter_and_resources(failures)
    case_count = check_record_behavior(failures)
    if failures:
        print("Research skill package verification failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("Research skill package verification passed.")
    print(f"SKILL.md body words: {body_words}; deterministic cases: {case_count}.")
    print("Behavioral research quality still requires representative GPT-5.6 Sol forward evals.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
