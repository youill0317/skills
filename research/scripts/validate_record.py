#!/usr/bin/env python3
"""Validate the compact Markdown research record shape.

This checks whether a record preserves the research contract. It does not judge
whether the cited sources are true or sufficient; the researcher must still
inspect, verify, and synthesize the evidence.
"""

from __future__ import annotations

from pathlib import Path
import argparse
import re
import sys

from markdown_record import parse_markdown_rows, read_markdown, section_body
from markdown_record import strip_fenced_code_blocks
from script_io import force_utf8_stdio


force_utf8_stdio()


REQUIRED_SECTIONS = [
    "Answer",
    "Scope And Success Criteria",
    "Search Plan And Coverage",
    "Sources And Observations",
    "Lead And Gap Log",
    "Claim Ledger",
    "Verification And Counterevidence",
    "Confidence And Limits",
    "Refresh Triggers",
]


REQUIRED_METADATA = [
    r"^Date:\s+\S+",
    r"^User request:\s+\S+",
    r"^Scope:\s+\S+",
    r"^Status:\s+\S+",
]


PLACEHOLDER_PATTERNS = [
    r"\bFILLME\b",
    r"\bTODO\b",
    r"\bTBD\b",
]


ALLOWED_CONFIDENCE = {"high", "medium", "low", "insufficient"}
ALLOWED_CLAIM_DECISIONS = {"use", "downgrade", "exclude", "insufficient"}
ALLOWED_LANE_STATUS = {
    "searched",
    "blocked",
    "not applicable",
    "not-applicable",
    "planned",
    "complete",
    "closed",
}
ALLOWED_LEAD_ACTIONS = {
    "followed",
    "closed",
    "blocked",
    "downgraded",
    "duplicate",
    "duplicate-lineage",
    "out of scope",
    "out-of-scope",
    "low quality",
    "low-quality",
    "open",
    "planned",
    "not applicable",
    "not-applicable",
}
ALLOWED_RECORD_STATUSES = {
    "saturated",
    "saturated with blocked gaps",
    "insufficient",
}
DRAFT_RECORD_STATUSES = {
    "draft",
    "insufficient draft",
    "planned",
}
FORBIDDEN_STATUS_WORDS = {
    "quick",
    "deep",
    "lightweight",
}


def normalize(value: str) -> str:
    return " ".join(value.strip().split()).lower()


def metadata_value(text: str, key: str) -> str | None:
    match = re.search(rf"^{re.escape(key)}:\s*(?P<value>.+?)\s*$", text, re.MULTILINE)
    return match.group("value") if match else None


def has_data_rows(body: str) -> bool:
    return len(parse_markdown_rows(body)) > 1


def contains_source_id(value: str) -> bool:
    return bool(re.search(r"\bS\d+\b", value))


def validate_claim_rows(text: str, failures: list[str], allow_placeholders: bool) -> None:
    rows = parse_markdown_rows(section_body(text, "Claim Ledger"))
    if len(rows) <= 1:
        failures.append("Claim Ledger must include at least one claim row")
        return

    header = [normalize(cell) for cell in rows[0]]
    expected = [
        "claim id",
        "claim",
        "type",
        "supporting evidence",
        "counterevidence / limits",
        "currentness / version",
        "confidence",
        "decision",
    ]
    if header[: len(expected)] != expected:
        failures.append("Claim Ledger header does not match the compact template")

    for index, row in enumerate(rows[1:], start=1):
        if len(row) < 8:
            failures.append(f"Claim Ledger row {index} has too few columns")
            continue

        confidence = normalize(row[6])
        decision = normalize(row[7])
        if confidence not in ALLOWED_CONFIDENCE:
            failures.append(f"Claim Ledger row {index} has invalid confidence {row[6]!r}")
        if allow_placeholders and decision == "unresolved":
            continue
        if decision not in ALLOWED_CLAIM_DECISIONS:
            failures.append(f"Claim Ledger row {index} has invalid decision {row[7]!r}")
        if decision in {"use", "downgrade"} and not contains_source_id(row[3]):
            failures.append(
                f"Claim Ledger row {index} uses or downgrades a claim without source ID support"
            )
        if decision == "use" and confidence == "insufficient":
            failures.append(
                f"Claim Ledger row {index} cannot use a claim with insufficient confidence"
            )


def validate_search_rows(text: str, failures: list[str], allow_placeholders: bool) -> None:
    rows = parse_markdown_rows(section_body(text, "Search Plan And Coverage"))
    if len(rows) <= 1:
        failures.append("Search Plan And Coverage must include at least one lane row")
        return
    for index, row in enumerate(rows[1:], start=1):
        if len(row) < 5:
            failures.append(f"Search Plan And Coverage row {index} has too few columns")
            continue
        status = normalize(row[4])
        if status not in ALLOWED_LANE_STATUS:
            failures.append(
                f"Search Plan And Coverage row {index} has invalid status {row[4]!r}"
            )
        if not allow_placeholders and status == "planned":
            failures.append(
                f"Search Plan And Coverage row {index} remains planned in final record"
            )


def validate_lead_rows(text: str, failures: list[str], allow_placeholders: bool) -> None:
    rows = parse_markdown_rows(section_body(text, "Lead And Gap Log"))
    if len(rows) <= 1:
        failures.append("Lead And Gap Log must include at least one lead/gap row")
        return
    for index, row in enumerate(rows[1:], start=1):
        if len(row) < 4:
            failures.append(f"Lead And Gap Log row {index} has too few columns")
            continue
        action = normalize(row[3])
        if action not in ALLOWED_LEAD_ACTIONS:
            failures.append(f"Lead And Gap Log row {index} has invalid action {row[3]!r}")
        if not allow_placeholders and action in {"open", "planned"}:
            failures.append(
                f"Lead And Gap Log row {index} remains open/planned in final record"
            )


def validate_record_header(text: str, failures: list[str]) -> None:
    if not re.match(r"\A#\s+Research:\s+\S+", text):
        failures.append("record must start with '# Research: <Topic>'")

    headings = re.findall(r"^#\s+Research:\s+\S+", text, re.MULTILINE)
    if len(headings) != 1:
        failures.append("record must contain exactly one '# Research: <Topic>' heading")


def validate_record_status(
    text: str, failures: list[str], allow_placeholders: bool
) -> None:
    status = metadata_value(text, "Status")
    if not status:
        return

    normalized = normalize(status)
    for word in FORBIDDEN_STATUS_WORDS:
        if re.search(rf"\b{re.escape(word)}\b", normalized):
            failures.append(f"Status must not use mode vocabulary: {status!r}")
            return

    allowed = set(ALLOWED_RECORD_STATUSES)
    if allow_placeholders:
        allowed |= DRAFT_RECORD_STATUSES
    if normalized not in allowed:
        failures.append(f"Status has unsupported value {status!r}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("record")
    parser.add_argument(
        "--allow-placeholders",
        action="store_true",
        help="Allow draft scaffold placeholders",
    )
    args = parser.parse_args()

    record = Path(args.record)
    failures: list[str] = []

    if record.suffix.lower() != ".md":
        failures.append("record must be a Markdown file")
    if not record.exists():
        print(f"Research record validation failed:\n- missing record: {record}")
        return 1

    text = read_markdown(record)
    structure_text = strip_fenced_code_blocks(text)

    validate_record_header(structure_text, failures)

    for pattern in REQUIRED_METADATA:
        if not re.search(pattern, structure_text, re.MULTILINE):
            failures.append(f"missing metadata matching {pattern!r}")
    for as_of_line in re.findall(r"^As of:.*$", structure_text, re.MULTILINE):
        if not re.match(r"^As of:\s+\S+", as_of_line):
            failures.append("As of metadata is present but empty")

    validate_record_status(structure_text, failures, args.allow_placeholders)

    for section in REQUIRED_SECTIONS:
        body = section_body(structure_text, section)
        if not body:
            failures.append(f"missing or empty section: {section}")

    if not args.allow_placeholders:
        for pattern in PLACEHOLDER_PATTERNS:
            if re.search(pattern, structure_text, flags=re.IGNORECASE):
                failures.append(f"placeholder remains: {pattern}")

        for section in [
            "Answer",
            "Scope And Success Criteria",
            "Verification And Counterevidence",
            "Confidence And Limits",
            "Refresh Triggers",
        ]:
            if len(section_body(structure_text, section)) < 40:
                failures.append(f"section too thin for final record: {section}")

        for section in [
            "Search Plan And Coverage",
            "Sources And Observations",
            "Lead And Gap Log",
            "Claim Ledger",
        ]:
            if not has_data_rows(section_body(structure_text, section)):
                failures.append(f"section must include at least one table data row: {section}")

    validate_search_rows(structure_text, failures, args.allow_placeholders)
    validate_lead_rows(structure_text, failures, args.allow_placeholders)
    validate_claim_rows(structure_text, failures, args.allow_placeholders)

    if failures:
        print("Research record validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Research record validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
