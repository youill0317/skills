#!/usr/bin/env python3
"""Audit internal consistency of a compact research record."""

from __future__ import annotations

from pathlib import Path
import argparse
import re
import sys

from markdown_record import parse_markdown_rows, read_markdown, section_body
from markdown_record import strip_fenced_code_blocks
from script_io import force_utf8_stdio


force_utf8_stdio()


ID_RE = re.compile(r"\b(S|C|LD|L)\d+\b")


def normalize(value: str) -> str:
    return " ".join(value.strip().split()).lower()


def rows(text: str, heading: str) -> list[list[str]]:
    return parse_markdown_rows(section_body(text, heading))


def ids_in(value: str, prefix: str | None = None) -> set[str]:
    found = {match.group(0) for match in ID_RE.finditer(value)}
    if prefix:
        found = {item for item in found if item.startswith(prefix)}
    return found


def collect_ids(table_rows: list[list[str]], prefix: str) -> tuple[list[str], set[str]]:
    values = [
        row[0]
        for row in table_rows[1:]
        if row and re.fullmatch(rf"{re.escape(prefix)}\d+", row[0])
    ]
    return values, set(values)


def add_duplicate_failures(ids: list[str], label: str, failures: list[str]) -> None:
    seen: set[str] = set()
    duplicates: set[str] = set()
    for item in ids:
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    for item in sorted(duplicates):
        failures.append(f"duplicate {label} ID: {item}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("record")
    parser.add_argument(
        "--allow-placeholders",
        action="store_true",
        help="Allow draft scaffold statuses such as planned, open, and unresolved",
    )
    args = parser.parse_args()

    record = Path(args.record)
    if not record.exists():
        print(f"Research consistency audit failed:\n- missing record: {record}")
        return 1

    text = strip_fenced_code_blocks(read_markdown(record))
    failures: list[str] = []

    source_rows = rows(text, "Sources And Observations")
    claim_rows = rows(text, "Claim Ledger")
    lead_rows = rows(text, "Lead And Gap Log")
    lane_rows = rows(text, "Search Plan And Coverage")

    source_id_list, source_ids = collect_ids(source_rows, "S")
    claim_id_list, claim_ids = collect_ids(claim_rows, "C")
    lead_id_list, lead_ids = collect_ids(lead_rows, "LD")
    lane_id_list, lane_ids = collect_ids(lane_rows, "L")

    add_duplicate_failures(source_id_list, "source", failures)
    add_duplicate_failures(claim_id_list, "claim", failures)
    add_duplicate_failures(lead_id_list, "lead", failures)
    add_duplicate_failures(lane_id_list, "lane", failures)

    if not source_ids:
        failures.append("no source IDs found in Sources And Observations")
    if not claim_ids:
        failures.append("no claim IDs found in Claim Ledger")

    known = source_ids | claim_ids | lead_ids | lane_ids
    structured_reference_cells: list[str] = []
    for row in claim_rows[1:]:
        structured_reference_cells.extend(row[3:5])
    for row in lead_rows[1:]:
        structured_reference_cells.extend(row[1:3])
    for row in lane_rows[1:]:
        structured_reference_cells.extend(row[:1])
    for value in structured_reference_cells:
        for match in ID_RE.finditer(value):
            item = match.group(0)
            if item not in known:
                failures.append(f"unknown ID reference: {item}")

    for index, row in enumerate(claim_rows[1:], start=1):
        if len(row) < 8:
            continue
        support_ids = ids_in(row[3], "S")
        decision = normalize(row[7])
        confidence = normalize(row[6])
        if decision in {"use", "downgrade"} and not support_ids:
            failures.append(f"Claim Ledger row {index} has no source support for {decision}")
        missing_sources = support_ids - source_ids
        if missing_sources:
            failures.append(
                f"Claim Ledger row {index} references missing sources: {', '.join(sorted(missing_sources))}"
            )
        if decision == "use" and confidence == "insufficient":
            failures.append(f"Claim Ledger row {index} uses a claim with insufficient confidence")
        if decision == "unresolved" and not args.allow_placeholders:
            failures.append(f"Claim Ledger row {index} remains unresolved")

    for index, row in enumerate(lead_rows[1:], start=1):
        if (
            len(row) >= 4
            and normalize(row[3]) in {"open", "planned"}
            and not args.allow_placeholders
        ):
            failures.append(f"Lead And Gap Log row {index} remains open/planned")

    for index, row in enumerate(lane_rows[1:], start=1):
        if (
            len(row) >= 5
            and normalize(row[4]) == "planned"
            and not args.allow_placeholders
        ):
            failures.append(f"Search Plan And Coverage row {index} remains planned")

    if failures:
        print("Research consistency audit failed:")
        for failure in sorted(set(failures)):
            print(f"- {failure}")
        return 1

    print("Research consistency audit passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
