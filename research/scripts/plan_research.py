#!/usr/bin/env python3
"""Seed a compact maximum-saturation research plan."""

from __future__ import annotations

import argparse

from script_io import force_utf8_stdio
from research_taxonomy import BASE_LANES, DOMAIN_LANES, domain_keys


force_utf8_stdio()


def print_scope(args: argparse.Namespace) -> None:
    print("## Scope And Success Criteria")
    print()
    print(f"- Research question: {args.topic}")
    print(f"- User request: {args.request or args.topic}")
    print(f"- Scope: {args.scope or 'state explicit assumptions before search'}")
    print(f"- Entities: {args.entities or 'discover aliases and disambiguate'}")
    print(f"- Jurisdictions: {args.jurisdictions or 'discover and bound'}")
    print(f"- Languages: {args.languages or 'search English and relevant local terms'}")
    print("- Evidence rules: inspect source bodies before using them as evidence")
    print("- Success criteria: answer all material subquestions, close or downgrade material leads, verify important claims")
    print()


def print_lanes(args: argparse.Namespace) -> None:
    lanes = list(BASE_LANES)
    for key in domain_keys(args.domains):
        need, sources, path = DOMAIN_LANES[key]
        lane_id = f"L{len(lanes) + 1}"
        lanes.append((lane_id, need, sources, path))

    print("## Search Plan And Coverage")
    print()
    print("| Lane | Evidence Need | Source Families / Tools | Search Or Retrieval Path | Status | Notes |")
    print("|---|---|---|---|---|---|")
    for lane_id, need, sources, path in lanes:
        print(f"| {lane_id} | {need} | {sources} | {path} | planned | convert to searched, blocked, or not applicable in the record |")
    print()


def print_leads_and_verification(args: argparse.Namespace) -> None:
    print("## Lead And Gap Log")
    print()
    print("| Lead ID | Raised From | Lead Or Gap | Action Taken | Outcome | Confidence Effect |")
    print("|---|---|---|---|---|---|")
    print("| LD1 | initial plan | source families, aliases, native terms, citations, datasets, standards, counterclaims | open | follow during scout and target passes | insufficient until closed or downgraded |")
    print()
    print("## Verification And Counterevidence")
    print()
    print("- Primary or authoritative sources checked: planned")
    print("- Independent corroboration: planned")
    print("- Counter-search and disagreement: planned")
    print("- Currentness, version, supersession, or retraction checks: planned")
    print("- Provenance, incentives, funding, authorship, or manipulation risk: planned")
    print("- Quantitative method, denominator, unit, geography, and date checks: planned when applicable")
    print("- Comparison criteria, tradeoffs, and sensitivity: planned when applicable")
    print("- Absence-claim search boundary: define before making absence claims")
    print("- Inference boundaries and unsupported possibilities: planned")
    print()


def print_query_hint(args: argparse.Namespace) -> None:
    pieces = [f'--topic "{args.topic}"']
    if args.entities:
        pieces.append(f'--entities "{args.entities}"')
    if args.jurisdictions:
        pieces.append(f'--jurisdictions "{args.jurisdictions}"')
    if args.languages:
        pieces.append(f'--languages "{args.languages}"')
    if args.domains:
        pieces.append(f'--families "{args.domains}"')
    print("## Query Seed Command")
    print()
    print("```bash")
    print("python <skill-dir>/scripts/query_matrix.py " + " ".join(pieces))
    print("python <skill-dir>/scripts/query_matrix.py " + " ".join(pieces) + " --format batches --batch-size <tool-limit>")
    print("```")
    print()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", required=True)
    parser.add_argument("--request", default="")
    parser.add_argument("--scope", default="")
    parser.add_argument("--domains", default="")
    parser.add_argument("--entities", default="")
    parser.add_argument("--jurisdictions", default="")
    parser.add_argument("--languages", default="")
    args = parser.parse_args()

    print_scope(args)
    print_lanes(args)
    print_leads_and_verification(args)
    print_query_hint(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
