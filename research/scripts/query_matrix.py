#!/usr/bin/env python3
"""Generate high-yield query families for a research Search Matrix.

This script does not access the network. It creates query candidates that the
agent can use with whatever web/search/connectors are available.
"""

from __future__ import annotations

import argparse
from datetime import datetime
import re
import sys
import unicodedata


DEFAULT_FAMILIES = [
    "scout",
    "official-primary",
    "pdf-document",
    "scholarly",
    "dataset-method",
    "github-oss",
    "implementation-code",
    "standards-specs",
    "legal-regulatory",
    "market-competitive",
    "public-sentiment",
    "security-advisory",
    "currentness",
    "counterevidence",
    "source-lineage",
    "provenance-archive",
    "frontier-expansion",
    "blocked-source-recovery",
]


FAMILY_PATTERNS = {
    "scout": [
        "{topic}",
        "\"{topic}\" overview",
        "\"{topic}\" terminology OR definition",
        "\"{topic}\" landscape",
    ],
    "official-primary": [
        "\"{topic}\" official",
        "\"{topic}\" site:gov OR site:edu OR site:org",
        "\"{topic}\" filing OR report OR standard OR guidance",
        "\"{topic}\" documentation OR specification",
    ],
    "pdf-document": [
        "\"{topic}\" filetype:pdf",
        "\"{topic}\" report filetype:pdf",
        "\"{topic}\" methodology filetype:pdf",
        "\"{topic}\" white paper filetype:pdf",
    ],
    "scholarly": [
        "\"{topic}\" systematic review",
        "\"{topic}\" meta-analysis",
        "\"{topic}\" literature review",
        "\"{topic}\" DOI OR arXiv OR conference",
    ],
    "dataset-method": [
        "\"{topic}\" dataset",
        "\"{topic}\" methodology",
        "\"{topic}\" data dictionary OR codebook",
        "\"{topic}\" benchmark OR survey OR statistics",
    ],
    "github-oss": [
        "\"{topic}\" GitHub",
        "\"{topic}\" site:github.com",
        "\"{topic}\" issues OR discussions OR changelog",
        "\"{topic}\" package registry OR npm OR PyPI OR crates.io",
        "\"{topic}\" Papers with Code",
    ],
    "implementation-code": [
        "\"{topic}\" source code OR implementation",
        "\"{topic}\" API reference OR SDK",
        "\"{topic}\" migration guide OR deprecation",
        "\"{topic}\" example OR sample repository",
    ],
    "standards-specs": [
        "\"{topic}\" standard OR specification",
        "\"{topic}\" RFC OR ISO OR IEEE OR W3C",
        "\"{topic}\" interoperability OR conformance",
        "\"{topic}\" requirements OR normative",
    ],
    "legal-regulatory": [
        "\"{topic}\" regulation OR law OR statute",
        "\"{topic}\" guidance OR enforcement OR docket",
        "\"{topic}\" consultation OR public comment",
        "\"{topic}\" effective date OR superseded",
    ],
    "market-competitive": [
        "\"{topic}\" market share OR adoption",
        "\"{topic}\" competitor OR alternative",
        "\"{topic}\" pricing OR procurement",
        "\"{topic}\" customer reviews OR case study",
    ],
    "public-sentiment": [
        "\"{topic}\" forum OR discussion",
        "\"{topic}\" Reddit OR Hacker News",
        "\"{topic}\" reviews OR complaints",
        "\"{topic}\" support thread OR issue",
    ],
    "security-advisory": [
        "\"{topic}\" CVE OR vulnerability",
        "\"{topic}\" security advisory",
        "\"{topic}\" incident OR breach",
        "\"{topic}\" patch OR mitigation",
    ],
    "currentness": [
        "\"{topic}\" latest",
        "\"{topic}\" {current_year} OR {previous_year}",
        "\"{topic}\" changelog OR release notes",
        "\"{topic}\" update OR superseded OR deprecated",
        "\"{topic}\" advisory OR warning OR recall",
    ],
    "counterevidence": [
        "\"{topic}\" criticism OR critique",
        "\"{topic}\" rebuttal OR response",
        "\"{topic}\" failed replication OR negative result",
        "\"{topic}\" limitation OR caveat",
        "\"{topic}\" correction OR retraction OR erratum",
        "\"{topic}\" controversy OR dispute",
    ],
    "source-lineage": [
        "\"{topic}\" cited by OR references",
        "\"{topic}\" based on OR derived from",
        "\"{topic}\" press release OR syndicated",
        "\"{topic}\" duplicate OR mirror",
    ],
    "provenance-archive": [
        "\"{topic}\" source",
        "\"{topic}\" original",
        "\"{topic}\" archive OR archived",
        "\"{topic}\" earliest report OR first reported",
        "\"{topic}\" quote OR transcript",
    ],
    "frontier-expansion": [
        "\"{topic}\" references OR bibliography OR footnotes",
        "\"{topic}\" author OR institution OR dataset",
        "\"{topic}\" successor OR update OR correction",
        "\"{topic}\" issue OR docket OR standard OR repository",
        "\"{topic}\" related work OR cited sources OR co-citation",
    ],
    "blocked-source-recovery": [
        "\"{topic}\" mirror OR cached OR archived",
        "\"{topic}\" PDF OR transcript OR appendix",
        "\"{topic}\" API OR dataset OR repository history",
        "\"{topic}\" quoted by OR excerpt OR copy",
        "\"{topic}\" official mirror OR alternate source",
    ],
}


BATCH_FAMILY_ORDER = [
    "scout",
    "official-primary",
    "pdf-document",
    "scholarly",
    "dataset-method",
    "currentness",
    "counterevidence",
    "source-lineage",
    "provenance-archive",
    "frontier-expansion",
    "blocked-source-recovery",
    "github-oss",
    "implementation-code",
    "standards-specs",
    "legal-regulatory",
    "market-competitive",
    "public-sentiment",
    "security-advisory",
]


BATCH_PURPOSES = {
    "scout": "vocabulary and landscape",
    "official-primary": "source-of-truth discovery",
    "pdf-document": "document and report recovery",
    "scholarly": "academic or expert synthesis",
    "dataset-method": "data and method evidence",
    "github-oss": "repository and package evidence",
    "implementation-code": "implementation surface evidence",
    "standards-specs": "standards and specification evidence",
    "legal-regulatory": "legal, policy, or docket evidence",
    "market-competitive": "market, product, or competitor evidence",
    "public-sentiment": "review, forum, or behavior traces",
    "security-advisory": "risk, incident, and advisory evidence",
    "currentness": "latest state and supersession",
    "counterevidence": "disconfirmation and limitations",
    "source-lineage": "duplicate-lineage and upstream tracing",
    "provenance-archive": "original, archive, and quote provenance",
    "frontier-expansion": "lead expansion and snowballing",
    "blocked-source-recovery": "alternate retrieval for blocked sources",
}


BATCH_INTEGRATION_TARGETS = {
    "scout": ["Search Craft Log", "Search Result Triage", "Saturation Metrics"],
    "official-primary": ["Search Result Triage", "Source Coverage", "Claim Ledger"],
    "pdf-document": ["Access And Retrieval Audit", "Evidence Location Audit"],
    "scholarly": ["Source Quality Audit", "Corroboration And Triangulation Audit"],
    "dataset-method": ["Quantitative And Measurement Audit", "Claim Ledger"],
    "github-oss": ["Access And Retrieval Audit", "Source Lineage Map"],
    "implementation-code": ["Source Coverage", "Evidence"],
    "standards-specs": ["Source Coverage", "Claim Ledger"],
    "legal-regulatory": ["Currentness And Version Audit", "Claim Ledger"],
    "market-competitive": ["Comparison And Evaluation Audit", "Decision Usefulness Matrix"],
    "public-sentiment": ["Selection And Inclusion Audit", "Source Manipulation And Adversarial Provenance Audit"],
    "security-advisory": ["Currentness And Version Audit", "Source Quality Audit"],
    "currentness": ["Currentness And Version Audit", "Reproducibility And Refresh Audit"],
    "counterevidence": ["Corroboration And Triangulation Audit", "Counterevidence / Uncertainty"],
    "source-lineage": ["Source Lineage Map", "Source Quality Audit"],
    "provenance-archive": ["Source Lineage Map", "Source Manipulation And Adversarial Provenance Audit"],
    "frontier-expansion": ["Lead Ledger", "Expansion Frontier Audit"],
    "blocked-source-recovery": ["Access And Retrieval Audit", "Coverage Debt"],
}


STRATEGIC_BATCH_PHASES = [
    [
        "scout",
        "official-primary",
        "pdf-document",
        "dataset-method",
    ],
    [
        "currentness",
        "counterevidence",
        "source-lineage",
        "provenance-archive",
    ],
    [
        "frontier-expansion",
        "blocked-source-recovery",
        "scholarly",
        "github-oss",
        "implementation-code",
    ],
    [
        "standards-specs",
        "legal-regulatory",
        "market-competitive",
        "public-sentiment",
        "security-advisory",
    ],
]


def split_csv(value: str | None) -> list[str]:
    if not value:
        return []
    return [part.strip() for part in value.split(",") if part.strip()]


def safe_topic(value: str) -> str:
    return " ".join(value.split())


def slug(value: str) -> str:
    ascii_text = (
        unicodedata.normalize("NFKD", value)
        .encode("ascii", "ignore")
        .decode("ascii")
        .lower()
    )
    return re.sub(r"[^a-z0-9]+", "-", ascii_text).strip("-") or "topic"


def expand_query(
    pattern: str,
    topic: str,
    entity: str | None,
    jurisdiction: str | None,
    language: str | None,
    exclude: list[str],
    current_year: int,
) -> str:
    query = pattern.format(
        topic=topic,
        current_year=current_year,
        previous_year=current_year - 1,
    )
    if entity:
        query = f"{query} \"{entity}\""
    if jurisdiction:
        query = f"{query} \"{jurisdiction}\""
    if language:
        query = f"{query} {language}"
    for term in exclude:
        query = f"{query} -\"{term}\""
    return query


def diversified_batches(
    rows: list[tuple[str, str, str, str]],
    batch_size: int,
) -> list[list[tuple[str, str, str, str]]]:
    if batch_size <= 0:
        batch_size = 4

    family_rows: dict[str, list[tuple[str, str, str, str]]] = {}
    for row in rows:
        family_rows.setdefault(row[1], []).append(row)

    ordered_families = [
        family for family in BATCH_FAMILY_ORDER if family in family_rows
    ]
    ordered_families.extend(
        family for family in family_rows if family not in ordered_families
    )

    batches: list[list[tuple[str, str, str, str]]] = []
    while any(family_rows.values()):
        batch: list[tuple[str, str, str, str]] = []
        for family in ordered_families:
            if len(batch) >= batch_size:
                break
            if family_rows.get(family):
                batch.append(family_rows[family].pop(0))
        if not batch:
            break
        batches.append(batch)
    return batches


def unique_in_order(values: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result


def batch_record_integration(families: list[str]) -> str:
    targets: list[str] = []
    for family in families:
        targets.extend(
            BATCH_INTEGRATION_TARGETS.get(
                family,
                ["Search Craft Log", "Search Result Triage"],
            )
        )
    return " / ".join(unique_in_order(targets))


def strategic_record_batches(
    rows: list[tuple[str, str, str, str]],
) -> list[list[tuple[str, str, str, str]]]:
    family_rows: dict[str, list[tuple[str, str, str, str]]] = {}
    for row in rows:
        family_rows.setdefault(row[1], []).append(row)

    batches: list[list[tuple[str, str, str, str]]] = []
    scheduled_families: set[str] = set()
    for phase in STRATEGIC_BATCH_PHASES:
        batch: list[tuple[str, str, str, str]] = []
        for family in phase:
            family_batch = family_rows.get(family, [])
            if family_batch:
                batch.extend(family_batch)
                scheduled_families.add(family)
        if batch:
            batches.append(batch)

    remaining_rows = [
        row
        for family, family_batch in family_rows.items()
        if family not in scheduled_families and family_batch
        for row in family_batch
    ]
    if remaining_rows:
        batches.append(remaining_rows)
    return batches


def execution_sub_batches(
    rows: list[tuple[str, str, str, str]],
    batch_size: int,
) -> list[list[tuple[str, str, str, str]]]:
    effective_batch_size = batch_size if batch_size > 0 else max(len(rows), 1)
    return [
        rows[index : index + effective_batch_size]
        for index in range(0, len(rows), effective_batch_size)
    ]


def batch_purpose_with_sub_batches(
    rows: list[tuple[str, str, str, str]],
    batch_size: int,
) -> str:
    effective_batch_size = batch_size if batch_size > 0 else max(len(rows), 1)
    sub_batches = execution_sub_batches(rows, batch_size)
    parts = [
        f"execute {len(rows)} queries as {len(sub_batches)} sub-batches of up to {effective_batch_size}"
    ]
    query_number = 1
    for sub_batch_index, sub_batch in enumerate(sub_batches, start=1):
        query_parts: list[str] = []
        for _, family, query, _ in sub_batch:
            purpose = BATCH_PURPOSES.get(family, "independent evidence path")
            query_parts.append(f"Q{query_number} {family}: {purpose}; {query}")
            query_number += 1
        parts.append(f"SB{sub_batch_index}: " + " ; ".join(query_parts))
    return " | ".join(parts).replace("|", "\\|")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", required=True)
    parser.add_argument("--entities", default="", help="Comma-separated entities")
    parser.add_argument("--jurisdictions", default="", help="Comma-separated jurisdictions")
    parser.add_argument("--languages", default="", help="Comma-separated language/native terms")
    parser.add_argument("--exclude", default="", help="Comma-separated false-positive terms to exclude")
    parser.add_argument("--current-year", type=int, default=datetime.now().year)
    parser.add_argument(
        "--max-rows",
        type=int,
        default=0,
        help="Optional cap for extremely large matrices; 0 means no cap",
    )
    parser.add_argument(
        "--families",
        default=",".join(DEFAULT_FAMILIES),
        help="Comma-separated query families",
    )
    parser.add_argument(
        "--format",
        choices=["markdown", "queries", "batches"],
        default="markdown",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=4,
        help="Active search-tool query limit; strategic record batches stay separate and can be executed as sub-batches if needed",
    )
    args = parser.parse_args()

    topic = safe_topic(args.topic)
    families = split_csv(args.families) or DEFAULT_FAMILIES
    entities = split_csv(args.entities) or [None]
    jurisdictions = split_csv(args.jurisdictions) or [None]
    languages = split_csv(args.languages) or [None]
    exclude = split_csv(args.exclude)

    rows: list[tuple[str, str, str, str]] = []
    lane_index = 1
    for family in families:
        patterns = FAMILY_PATTERNS.get(family)
        if not patterns:
            print(f"unknown query family: {family}", file=sys.stderr)
            return 1
        for pattern in patterns:
            for entity in entities:
                for jurisdiction in jurisdictions:
                    for language in languages:
                        query = expand_query(
                            pattern,
                            topic,
                            entity,
                            jurisdiction,
                            language,
                            exclude,
                            args.current_year,
                        )
                        lane = f"L{lane_index:02d}-{slug(family)}"
                        rows.append((lane, family, query, "planned"))
                        lane_index += 1
                        if args.max_rows and len(rows) >= args.max_rows:
                            break
                    if args.max_rows and len(rows) >= args.max_rows:
                        break
                if args.max_rows and len(rows) >= args.max_rows:
                    break
            if args.max_rows and len(rows) >= args.max_rows:
                break

    if args.format == "queries":
        for _, _, query, _ in rows:
            print(query)
        return 0

    if args.format == "batches":
        print("| Batch | Source Families To Mix | Purpose | Record Integration |")
        print("|---|---|---|---|")
        for batch_index, batch in enumerate(strategic_record_batches(rows), start=1):
            families = [family for _, family, _, _ in batch]
            source_families = " / ".join(unique_in_order(families))
            print(
                f"| B{batch_index} | {source_families} | {batch_purpose_with_sub_batches(batch, args.batch_size)} | {batch_record_integration(families)} |"
            )
        return 0

    print("| Lane | Source Family / Pass | Query / Path Pattern | Status |")
    print("|---|---|---|---|")
    for lane, family, query, status in rows:
        escaped_query = query.replace("|", "\\|")
        print(f"| {lane} | {family} | {escaped_query} | {status} |")
    return 0


if __name__ == "__main__":
    sys.exit(main())
