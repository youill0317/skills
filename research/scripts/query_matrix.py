#!/usr/bin/env python3
"""Generate query seeds for maximum-saturation research.

The output is a seed, not a mandatory template. Integrate useful rows into the
single Markdown research record under Search Plan And Coverage, Lead And Gap
Log, Sources And Observations, Claim Ledger, and Verification And Counterevidence.
"""

from __future__ import annotations

import argparse
from datetime import datetime

from script_io import force_utf8_stdio
from research_taxonomy import FAMILY_PATTERNS, selected_families, split_values


force_utf8_stdio()


def quote_or_group(values: list[str]) -> str:
    if not values:
        return ""
    quoted = [f'"{value}"' for value in values]
    return quoted[0] if len(quoted) == 1 else "(" + " OR ".join(quoted) + ")"


def extra_clause(args: argparse.Namespace, consumed: set[str] | None = None) -> str:
    consumed = consumed or set()
    groups = []
    if "entities" not in consumed:
        groups.append(quote_or_group(split_values(args.entities)))
    if "jurisdictions" not in consumed:
        groups.append(quote_or_group(split_values(args.jurisdictions)))
    if "languages" not in consumed:
        groups.append(quote_or_group(split_values(args.languages)))
    return " ".join(group for group in groups if group)


def expand_pattern(pattern: str, args: argparse.Namespace) -> list[str]:
    if "{languages}" in pattern and split_values(args.languages):
        return [pattern.replace("{languages}", value) for value in split_values(args.languages)]
    if "{languages}" in pattern:
        return []
    if "{jurisdictions}" in pattern and split_values(args.jurisdictions):
        return [
            pattern.replace("{jurisdictions}", value)
            for value in split_values(args.jurisdictions)
        ]
    if "{jurisdictions}" in pattern:
        return []
    return [pattern]


def render_query(
    pattern: str, args: argparse.Namespace, consumed: set[str] | None = None
) -> str:
    query = pattern.format(
        topic=args.topic,
        entities=args.entities or "",
        jurisdictions=args.jurisdictions or "",
        languages=args.languages or "",
        current_year=args.as_of_year,
        prior_year=args.as_of_year - 1,
    )
    extras = extra_clause(args, consumed)
    if extras:
        query = f"{query} {extras}"
    if args.exclude:
        exclusions = " ".join(f'-"{term}"' for term in split_values(args.exclude))
        query = f"{query} {exclusions}"
    return " ".join(query.split())


def build_queries(args: argparse.Namespace) -> list[tuple[str, str, str]]:
    rows: list[tuple[str, str, str]] = []
    for family in selected_families(args.families):
        patterns = FAMILY_PATTERNS.get(family, [f"{{topic}} {family}"])
        for pattern in patterns:
            for expanded_pattern in expand_pattern(pattern, args):
                consumed: set[str] = set()
                if "{languages}" in pattern:
                    consumed.add("languages")
                if "{jurisdictions}" in pattern:
                    consumed.add("jurisdictions")
                rows.append(
                    (
                        family,
                        render_query(expanded_pattern, args, consumed),
                        "lead or evidence route",
                    )
                )
    if args.max_rows:
        rows = rows[: args.max_rows]
    return rows


def print_queries(args: argparse.Namespace) -> None:
    print("| Source Family | Query Seed | Record Integration |")
    print("|---|---|---|")
    for family, query, purpose in build_queries(args):
        print(
            f"| {family} | {query} | Search Plan And Coverage; Lead And Gap Log; {purpose} |"
        )


def print_batches(args: argparse.Namespace) -> None:
    rows = build_queries(args)
    batch_size = max(args.batch_size, 1)
    print("| Batch | Query Purpose | Queries | Record Integration |")
    print("|---|---|---|---|")
    for batch_index, start in enumerate(range(0, len(rows), batch_size), start=1):
        chunk = rows[start : start + batch_size]
        families = ", ".join(sorted({family for family, _, _ in chunk}))
        queries = "<br>".join(query for _, query, _ in chunk)
        print(
            f"| B{batch_index} | {families} | {queries} | Search Plan And Coverage; Sources And Observations; Lead And Gap Log; Verification And Counterevidence |"
        )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", required=True)
    parser.add_argument("--entities")
    parser.add_argument("--jurisdictions")
    parser.add_argument("--languages")
    parser.add_argument("--exclude")
    parser.add_argument("--families")
    parser.add_argument(
        "--as-of-year",
        type=int,
        default=datetime.now().year,
        help="Current year for currentness query seeds",
    )
    parser.add_argument("--format", choices=["queries", "batches"], default="queries")
    parser.add_argument("--batch-size", type=int, default=4)
    parser.add_argument("--max-rows", type=int)
    args = parser.parse_args()

    if args.format == "batches":
        print_batches(args)
    else:
        print_queries(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
