#!/usr/bin/env python3
"""Audit cross-section references inside one Markdown research record.

This script checks internal consistency only. It does not verify whether
sources or claims are true; it verifies that claim/source/observation/lineage
and debt IDs used across the record are defined somewhere in the same Markdown
record.

Expected dynamic messages include "unknown frontier reference",
"unknown source reference", and "unknown claim reference".
"""

from __future__ import annotations

from pathlib import Path
import argparse
import re
import sys


ID_PATTERN = re.compile(
    r"\b(?:EV|EM|EF|ST|AS|CF|CN|SB|MP|LD|AR|SR|AC|C|S|O|G|D|R|Q|A)\d+\b"
)
ID_PREFIX_PATTERN = re.compile(r"[A-Z]+")


def section_body(text: str, heading: str) -> str:
    pattern = re.compile(
        rf"^##\s+{re.escape(heading)}\s*$"
        rf"(?P<body>.*?)(?=^##\s+|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(text)
    return match.group("body") if match else ""


def parse_markdown_rows(section: str) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in section.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|") or not stripped.endswith("|"):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if cells and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
            continue
        rows.append(cells)
    return rows


def data_rows(text: str, heading: str) -> list[list[str]]:
    rows = parse_markdown_rows(section_body(text, heading))
    return rows[1:] if len(rows) > 1 else []


def ids_from_cell(cell: str, prefix: str | None = None) -> set[str]:
    ids = set(ID_PATTERN.findall(cell))
    if prefix is not None:
        ids = {value for value in ids if id_prefix(value) == prefix}
    return ids


def id_prefix(value: str) -> str:
    match = ID_PREFIX_PATTERN.match(value)
    return match.group(0) if match else ""


def collect_first_column_ids(rows: list[list[str]], prefix: str) -> set[str]:
    values: set[str] = set()
    for row in rows:
        if not row:
            continue
        values.update(ids_from_cell(row[0], prefix))
    return values


def check_refs(
    failures: list[str],
    label: str,
    refs: set[str],
    defined: set[str],
    defined_label: str,
) -> None:
    unknown = sorted(refs - defined)
    for value in unknown:
        failures.append(f"{label}: unknown {defined_label} reference {value}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("record", help="Path to one Markdown research record")
    parser.add_argument(
        "--allow-placeholders",
        action="store_true",
        help="Allow empty/placeholder scaffolds without failing missing reference checks",
    )
    args = parser.parse_args()

    record = Path(args.record)
    if not record.exists():
        print(f"- record does not exist: {record}")
        return 1

    text = record.read_text(encoding="utf-8").lstrip("\ufeff")
    failures: list[str] = []

    source_rows = data_rows(text, "Sources")
    observation_rows = data_rows(text, "Observation Manifest")
    claim_rows = data_rows(text, "Claim Ledger")
    question_rows = data_rows(text, "Question Coverage Audit")
    evaluation_rows = data_rows(text, "Comparison And Evaluation Audit")
    result_rows = data_rows(text, "Search Result Triage")
    lead_rows = data_rows(text, "Lead Ledger")
    frontier_rows = data_rows(text, "Expansion Frontier Audit")
    debt_rows = data_rows(text, "Coverage Debt")
    lineage_rows = data_rows(text, "Source Lineage Map")
    synthesis_rows = data_rows(text, "Synthesis Traceability Audit")

    sources = collect_first_column_ids(source_rows, "S")
    observations = collect_first_column_ids(observation_rows, "O")
    claims = collect_first_column_ids(claim_rows, "C")
    questions = collect_first_column_ids(question_rows, "Q")
    evaluations = collect_first_column_ids(evaluation_rows, "EV")
    results = collect_first_column_ids(result_rows, "R")
    leads = collect_first_column_ids(lead_rows, "LD")
    frontiers = collect_first_column_ids(frontier_rows, "EF")
    debts = collect_first_column_ids(debt_rows, "D")
    lineages = collect_first_column_ids(lineage_rows, "G")
    synthesis_items = collect_first_column_ids(synthesis_rows, "ST")

    if not args.allow_placeholders:
        for label, values in [
            ("Sources", sources),
            ("Observation Manifest", observations),
            ("Claim Ledger", claims),
            ("Lead Ledger", leads),
            ("Expansion Frontier Audit", frontiers),
            ("Coverage Debt", debts),
            ("Source Lineage Map", lineages),
        ]:
            if not values:
                failures.append(f"{label}: no IDs found")

    for row in data_rows(text, "Evidence Maturity Dashboard"):
        if len(row) >= 4:
            check_refs(
                failures,
                "Evidence Maturity Dashboard",
                ids_from_cell(row[3], "C"),
                claims,
                "claim",
            )
            check_refs(
                failures,
                "Evidence Maturity Dashboard",
                ids_from_cell(row[3], "Q"),
                questions,
                "question",
            )
            check_refs(
                failures,
                "Evidence Maturity Dashboard",
                ids_from_cell(row[3], "EV"),
                evaluations,
                "evaluation",
            )
            check_refs(
                failures,
                "Evidence Maturity Dashboard",
                ids_from_cell(row[3], "ST"),
                synthesis_items,
                "synthesis traceability item",
            )
        if len(row) >= 7:
            check_refs(
                failures,
                "Evidence Maturity Dashboard",
                ids_from_cell(row[6], "D"),
                debts,
                "debt",
            )

    for row in observation_rows:
        if len(row) >= 2:
            check_refs(
                failures,
                "Observation Manifest",
                ids_from_cell(row[1], "S"),
                sources,
                "source",
            )

    for row in lineage_rows:
        if len(row) >= 3:
            check_refs(
                failures,
                "Source Lineage Map",
                ids_from_cell(row[2], "S"),
                sources,
                "source",
            )
        if len(row) >= 5:
            check_refs(
                failures,
                "Source Lineage Map",
                ids_from_cell(row[4], "C"),
                claims,
                "claim",
            )

    for row in data_rows(text, "Source Quality Audit"):
        if row:
            check_refs(
                failures,
                "Source Quality Audit",
                ids_from_cell(row[0], "S"),
                sources,
                "source",
            )

    for row in data_rows(text, "Corroboration And Triangulation Audit"):
        if row:
            check_refs(
                failures,
                "Corroboration And Triangulation Audit",
                ids_from_cell(row[0], "C"),
                claims,
                "claim",
            )
        if len(row) >= 2:
            check_refs(
                failures,
                "Corroboration And Triangulation Audit",
                ids_from_cell(row[1], "S"),
                sources,
                "source",
            )
        if len(row) >= 3:
            check_refs(
                failures,
                "Corroboration And Triangulation Audit",
                ids_from_cell(row[2], "G"),
                lineages,
                "lineage",
            )
            check_refs(
                failures,
                "Corroboration And Triangulation Audit",
                ids_from_cell(row[2], "S"),
                sources,
                "source",
            )
        if len(row) >= 4:
            check_refs(
                failures,
                "Corroboration And Triangulation Audit",
                ids_from_cell(row[3], "O"),
                observations,
                "observation",
            )
            check_refs(
                failures,
                "Corroboration And Triangulation Audit",
                ids_from_cell(row[3], "D"),
                debts,
                "debt",
            )

    for row in data_rows(text, "Comparison And Evaluation Audit"):
        if len(row) >= 5:
            check_refs(
                failures,
                "Comparison And Evaluation Audit",
                ids_from_cell(row[4], "C"),
                claims,
                "claim",
            )
            check_refs(
                failures,
                "Comparison And Evaluation Audit",
                ids_from_cell(row[4], "S"),
                sources,
                "source",
            )
            check_refs(
                failures,
                "Comparison And Evaluation Audit",
                ids_from_cell(row[4], "O"),
                observations,
                "observation",
            )
            check_refs(
                failures,
                "Comparison And Evaluation Audit",
                ids_from_cell(row[4], "D"),
                debts,
                "debt",
            )

    for row in data_rows(text, "Consensus And Disagreement Audit"):
        if len(row) >= 6:
            check_refs(
                failures,
                "Consensus And Disagreement Audit",
                ids_from_cell(row[5], "C"),
                claims,
                "claim",
            )
            check_refs(
                failures,
                "Consensus And Disagreement Audit",
                ids_from_cell(row[5], "S"),
                sources,
                "source",
            )
            check_refs(
                failures,
                "Consensus And Disagreement Audit",
                ids_from_cell(row[5], "G"),
                lineages,
                "lineage",
            )
            check_refs(
                failures,
                "Consensus And Disagreement Audit",
                ids_from_cell(row[5], "O"),
                observations,
                "observation",
            )
            check_refs(
                failures,
                "Consensus And Disagreement Audit",
                ids_from_cell(row[5], "D"),
                debts,
                "debt",
            )

    for row in data_rows(text, "Source Incentive And Bias Audit"):
        if row:
            check_refs(
                failures,
                "Source Incentive And Bias Audit",
                ids_from_cell(row[0], "S"),
                sources,
                "source",
            )
            check_refs(
                failures,
                "Source Incentive And Bias Audit",
                ids_from_cell(row[0], "G"),
                lineages,
                "lineage",
            )

    for row in data_rows(text, "Source Manipulation And Adversarial Provenance Audit"):
        if len(row) >= 7:
            check_refs(
                failures,
                "Source Manipulation And Adversarial Provenance Audit",
                ids_from_cell(row[6], "S"),
                sources,
                "source",
            )
            check_refs(
                failures,
                "Source Manipulation And Adversarial Provenance Audit",
                ids_from_cell(row[6], "C"),
                claims,
                "claim",
            )
            check_refs(
                failures,
                "Source Manipulation And Adversarial Provenance Audit",
                ids_from_cell(row[6], "G"),
                lineages,
                "lineage",
            )
            check_refs(
                failures,
                "Source Manipulation And Adversarial Provenance Audit",
                ids_from_cell(row[6], "O"),
                observations,
                "observation",
            )
            check_refs(
                failures,
                "Source Manipulation And Adversarial Provenance Audit",
                ids_from_cell(row[6], "LD"),
                leads,
                "lead",
            )
            check_refs(
                failures,
                "Source Manipulation And Adversarial Provenance Audit",
                ids_from_cell(row[6], "D"),
                debts,
                "debt",
            )

    for row in data_rows(text, "Quantitative And Measurement Audit"):
        if row:
            check_refs(
                failures,
                "Quantitative And Measurement Audit",
                ids_from_cell(row[0], "C"),
                claims,
                "claim",
            )
        if len(row) >= 6:
            check_refs(
                failures,
                "Quantitative And Measurement Audit",
                ids_from_cell(row[5], "S"),
                sources,
                "source",
            )

    for row in data_rows(text, "Entity And Terminology Audit"):
        if len(row) >= 5:
            check_refs(
                failures,
                "Entity And Terminology Audit",
                ids_from_cell(row[4], "S"),
                sources,
                "source",
            )

    for row in data_rows(text, "Currentness And Version Audit"):
        if row:
            check_refs(
                failures,
                "Currentness And Version Audit",
                ids_from_cell(row[0], "C"),
                claims,
                "claim",
            )
            check_refs(
                failures,
                "Currentness And Version Audit",
                ids_from_cell(row[0], "S"),
                sources,
                "source",
            )

    for row in data_rows(text, "Reproducibility And Refresh Audit"):
        if row:
            check_refs(
                failures,
                "Reproducibility And Refresh Audit",
                ids_from_cell(row[0], "C"),
                claims,
                "claim",
            )
            check_refs(
                failures,
                "Reproducibility And Refresh Audit",
                ids_from_cell(row[0], "S"),
                sources,
                "source",
            )
        if len(row) >= 2:
            check_refs(
                failures,
                "Reproducibility And Refresh Audit",
                ids_from_cell(row[1], "S"),
                sources,
                "source",
            )
        if len(row) >= 3:
            check_refs(
                failures,
                "Reproducibility And Refresh Audit",
                ids_from_cell(row[2], "S"),
                sources,
                "source",
            )

    for row in data_rows(text, "Question Coverage Audit"):
        if len(row) >= 4:
            check_refs(
                failures,
                "Question Coverage Audit",
                ids_from_cell(row[3], "C"),
                claims,
                "claim",
            )
            check_refs(
                failures,
                "Question Coverage Audit",
                ids_from_cell(row[3], "O"),
                observations,
                "observation",
            )
            check_refs(
                failures,
                "Question Coverage Audit",
                ids_from_cell(row[3], "S"),
                sources,
                "source",
            )
            check_refs(
                failures,
                "Question Coverage Audit",
                ids_from_cell(row[3], "D"),
                debts,
                "debt",
            )

    for row in frontier_rows:
        if len(row) >= 2:
            check_refs(
                failures,
                "Expansion Frontier Audit",
                ids_from_cell(row[1], "S"),
                sources,
                "source",
            )
            check_refs(
                failures,
                "Expansion Frontier Audit",
                ids_from_cell(row[1], "R"),
                results,
                "search result",
            )
            check_refs(
                failures,
                "Expansion Frontier Audit",
                ids_from_cell(row[1], "LD"),
                leads,
                "lead",
            )
            check_refs(
                failures,
                "Expansion Frontier Audit",
                ids_from_cell(row[1], "EF"),
                frontiers,
                "frontier",
            )
        if len(row) >= 3:
            check_refs(
                failures,
                "Expansion Frontier Audit",
                ids_from_cell(row[2], "S"),
                sources,
                "source",
            )
        if len(row) >= 8:
            check_refs(
                failures,
                "Expansion Frontier Audit",
                ids_from_cell(row[7], "LD"),
                leads,
                "lead",
            )
            check_refs(
                failures,
                "Expansion Frontier Audit",
                ids_from_cell(row[7], "D"),
                debts,
                "debt",
            )

    for row in data_rows(text, "Quotation And Context Audit"):
        if row:
            check_refs(
                failures,
                "Quotation And Context Audit",
                ids_from_cell(row[0], "C"),
                claims,
                "claim",
            )
            check_refs(
                failures,
                "Quotation And Context Audit",
                ids_from_cell(row[0], "O"),
                observations,
                "observation",
            )
        if len(row) > 1:
            check_refs(
                failures,
                "Quotation And Context Audit",
                ids_from_cell(row[1], "S"),
                sources,
                "source",
            )

    for row in data_rows(text, "Absence Evidence Audit"):
        if row:
            check_refs(
                failures,
                "Absence Evidence Audit",
                ids_from_cell(row[0], "C"),
                claims,
                "claim",
            )

    for row in data_rows(text, "Claim Risk Triage"):
        if row:
            check_refs(
                failures,
                "Claim Risk Triage",
                ids_from_cell(row[0], "C"),
                claims,
                "claim",
            )

    for row in data_rows(text, "Claim Traceability Matrix"):
        if len(row) >= 1:
            check_refs(
                failures,
                "Claim Traceability Matrix",
                ids_from_cell(row[0], "C"),
                claims,
                "claim",
            )
        if len(row) >= 3:
            check_refs(
                failures,
                "Claim Traceability Matrix",
                ids_from_cell(row[2], "O"),
                observations,
                "observation",
            )
        if len(row) >= 4:
            check_refs(
                failures,
                "Claim Traceability Matrix",
                ids_from_cell(row[3], "S"),
                sources,
                "source",
            )
        if len(row) >= 5:
            check_refs(
                failures,
                "Claim Traceability Matrix",
                ids_from_cell(row[4], "G"),
                lineages,
                "lineage",
            )
        if len(row) >= 7:
            check_refs(
                failures,
                "Claim Traceability Matrix",
                ids_from_cell(row[6], "D"),
                debts,
                "debt",
            )

    for row in data_rows(text, "Inference Boundary Audit"):
        if len(row) >= 1:
            check_refs(
                failures,
                "Inference Boundary Audit",
                ids_from_cell(row[0], "C"),
                claims,
                "claim",
            )
        if len(row) >= 2:
            check_refs(
                failures,
                "Inference Boundary Audit",
                ids_from_cell(row[1], "O"),
                observations,
                "observation",
            )
            check_refs(
                failures,
                "Inference Boundary Audit",
                ids_from_cell(row[1], "S"),
                sources,
                "source",
            )

    for row in data_rows(text, "Assumption And Sensitivity Audit"):
        if len(row) >= 2:
            check_refs(
                failures,
                "Assumption And Sensitivity Audit",
                ids_from_cell(row[1], "C"),
                claims,
                "claim",
            )
        if len(row) >= 5:
            check_refs(
                failures,
                "Assumption And Sensitivity Audit",
                ids_from_cell(row[4], "S"),
                sources,
                "source",
            )
            check_refs(
                failures,
                "Assumption And Sensitivity Audit",
                ids_from_cell(row[4], "O"),
                observations,
                "observation",
            )
            check_refs(
                failures,
                "Assumption And Sensitivity Audit",
                ids_from_cell(row[4], "D"),
                debts,
                "debt",
            )

    for row in data_rows(text, "Conflict Resolution Matrix"):
        if len(row) >= 2:
            check_refs(
                failures,
                "Conflict Resolution Matrix",
                ids_from_cell(row[1], "C"),
                claims,
                "claim",
            )
            check_refs(
                failures,
                "Conflict Resolution Matrix",
                ids_from_cell(row[1], "O"),
                observations,
                "observation",
            )
        if len(row) >= 4:
            check_refs(
                failures,
                "Conflict Resolution Matrix",
                ids_from_cell(row[3], "S"),
                sources,
                "source",
            )

    for row in data_rows(text, "Confidence Calibration"):
        if row:
            check_refs(
                failures,
                "Confidence Calibration",
                ids_from_cell(row[0], "C"),
                claims,
                "claim",
            )

    for row in data_rows(text, "Synthesis Traceability Audit"):
        if len(row) >= 3:
            check_refs(
                failures,
                "Synthesis Traceability Audit",
                ids_from_cell(row[2], "C"),
                claims,
                "claim",
            )
        if len(row) >= 4:
            check_refs(
                failures,
                "Synthesis Traceability Audit",
                ids_from_cell(row[3], "S"),
                sources,
                "source",
            )
            check_refs(
                failures,
                "Synthesis Traceability Audit",
                ids_from_cell(row[3], "O"),
                observations,
                "observation",
            )
        if len(row) >= 6:
            check_refs(
                failures,
                "Synthesis Traceability Audit",
                ids_from_cell(row[5], "D"),
                debts,
                "debt",
            )

    for row in data_rows(text, "Adversarial Review"):
        if len(row) >= 2:
            check_refs(
                failures,
                "Adversarial Review",
                ids_from_cell(row[1], "C"),
                claims,
                "claim",
            )

    for row in data_rows(text, "Stop Rule Audit"):
        if len(row) >= 2:
            check_refs(
                failures,
                "Stop Rule Audit",
                ids_from_cell(row[1], "C"),
                claims,
                "claim",
            )
        if len(row) >= 5:
            check_refs(
                failures,
                "Stop Rule Audit",
                ids_from_cell(row[4], "D"),
                debts,
                "debt",
            )

    for row in data_rows(text, "Distortion Pattern Audit"):
        if row:
            check_refs(
                failures,
                "Distortion Pattern Audit",
                ids_from_cell(row[0], "C"),
                claims,
                "claim",
            )
            check_refs(
                failures,
                "Distortion Pattern Audit",
                ids_from_cell(row[0], "S"),
                sources,
                "source",
            )

    for row in data_rows(text, "Search Bias And Retrieval Trap Audit"):
        if len(row) >= 6:
            check_refs(
                failures,
                "Search Bias And Retrieval Trap Audit",
                ids_from_cell(row[5], "R"),
                results,
                "result",
            )
            check_refs(
                failures,
                "Search Bias And Retrieval Trap Audit",
                ids_from_cell(row[5], "S"),
                sources,
                "source",
            )
            check_refs(
                failures,
                "Search Bias And Retrieval Trap Audit",
                ids_from_cell(row[5], "LD"),
                leads,
                "lead",
            )
            check_refs(
                failures,
                "Search Bias And Retrieval Trap Audit",
                ids_from_cell(row[5], "D"),
                debts,
                "debt",
            )

    for row in data_rows(text, "Access And Retrieval Audit"):
        if len(row) >= 2:
            check_refs(
                failures,
                "Access And Retrieval Audit",
                ids_from_cell(row[1], "S"),
                sources,
                "source",
            )
            check_refs(
                failures,
                "Access And Retrieval Audit",
                ids_from_cell(row[1], "LD"),
                leads,
                "lead",
            )

    for row in data_rows(text, "Selection And Inclusion Audit"):
        if len(row) >= 4:
            check_refs(
                failures,
                "Selection And Inclusion Audit",
                ids_from_cell(row[3], "S"),
                sources,
                "source",
            )
        if len(row) >= 5:
            check_refs(
                failures,
                "Selection And Inclusion Audit",
                ids_from_cell(row[4], "S"),
                sources,
                "source",
            )
            check_refs(
                failures,
                "Selection And Inclusion Audit",
                ids_from_cell(row[4], "LD"),
                leads,
                "lead",
            )

    for row in data_rows(text, "Saturation Metrics"):
        if len(row) >= 5:
            for prefix, defined, defined_label in [
                ("R", results, "search result"),
                ("S", sources, "source"),
                ("LD", leads, "lead"),
                ("EF", frontiers, "frontier"),
                ("D", debts, "debt"),
            ]:
                check_refs(
                    failures,
                    "Saturation Metrics",
                    ids_from_cell(row[4], prefix),
                    defined,
                    defined_label,
                )
        if len(row) >= 6:
            check_refs(
                failures,
                "Saturation Metrics",
                ids_from_cell(row[5], "D"),
                debts,
                "debt",
            )

    if failures:
        print("Research record consistency audit failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Research record consistency audit passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
