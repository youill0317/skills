#!/usr/bin/env python3
"""Create one compact Markdown research record scaffold."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
import argparse
import re
import sys
import unicodedata

from script_io import force_utf8_stdio


force_utf8_stdio()


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
    slug = "".join(pieces).strip("-")
    slug = re.sub(r"-{2,}", "-", slug)
    return slug[:60].strip("-") or "research"


def next_prefix(record_dir: Path) -> int:
    highest = 0
    if record_dir.exists():
        for path in record_dir.glob("[0-9][0-9][0-9]-*.md"):
            try:
                highest = max(highest, int(path.name[:3]))
            except ValueError:
                continue
    if highest >= 999:
        raise ValueError("record prefix limit reached: 999")
    return highest + 1


def build_record(topic: str, request: str, scope: str, as_of: str) -> str:
    today = datetime.now().astimezone().strftime("%Y-%m-%d")
    return f"""# Research: {topic}

Date: {today}
As of: {as_of}
User request: {request}
Scope: {scope}
Status: insufficient draft

## Answer

FILLME

## Scope And Success Criteria

- Research question: FILLME
- Intended use or decision: FILLME
- Included: FILLME
- Excluded: FILLME
- Entity, term, jurisdiction, and language assumptions: FILLME
- Evidence rules: FILLME
- Success criteria: FILLME

## Search Plan And Coverage

| Lane | Evidence Need | Source Families / Tools | Search Or Retrieval Path | Status | Notes |
|---|---|---|---|---|---|
| L1 | FILLME | FILLME | FILLME | planned | FILLME |

## Sources And Observations

| Source ID | Source / Locator | Type | Accessed Evidence Location | Why It Matters | Key Observations |
|---|---|---|---|---|---|
| S1 | FILLME | FILLME | FILLME | FILLME | FILLME |

## Lead And Gap Log

| Lead ID | Raised From | Lead Or Gap | Action Taken | Outcome | Confidence Effect |
|---|---|---|---|---|---|
| LD1 | FILLME | FILLME | open | FILLME | FILLME |

## Claim Ledger

| Claim ID | Claim | Type | Supporting Evidence | Counterevidence / Limits | Currentness / Version | Confidence | Decision |
|---|---|---|---|---|---|---|---|
| C1 | FILLME | factual | S1 | FILLME | FILLME | insufficient | unresolved |

## Verification And Counterevidence

- Primary or authoritative sources checked: FILLME
- Independent corroboration: FILLME
- Counter-search and disagreement: FILLME
- Currentness, version, supersession, or retraction checks: FILLME
- Provenance, incentives, funding, authorship, or manipulation risk: FILLME
- Quantitative method, denominator, unit, geography, and date checks: FILLME
- Comparison criteria, tradeoffs, and sensitivity: FILLME
- Absence-claim search boundary, if any: FILLME
- Inference boundaries and unsupported possibilities: FILLME

## Confidence And Limits

| Item | Confidence | Why | What Would Change It |
|---|---|---|---|
| C1 | insufficient | FILLME | FILLME |

## Refresh Triggers

- FILLME
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", required=True)
    parser.add_argument("--request", required=True)
    parser.add_argument("--scope", required=True)
    parser.add_argument("--root", required=True, help="Workspace root")
    parser.add_argument(
        "--record-dir",
        default="research",
        help="Directory under --root where records are stored",
    )
    parser.add_argument("--as-of", default=None)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    record_dir = root / args.record_dir
    try:
        prefix = next_prefix(record_dir)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    path = record_dir / f"{prefix:03d}-{slugify(args.topic)}.md"
    as_of = args.as_of or datetime.now().astimezone().strftime("%Y-%m-%d %H:%M %Z")
    record = build_record(args.topic, args.request, args.scope, as_of)

    if args.dry_run:
        print(path)
        return 0

    record_dir.mkdir(parents=True, exist_ok=True)
    if path.exists():
        print(f"record already exists: {path}", file=sys.stderr)
        return 1
    path.write_text(record, encoding="utf-8")
    print(path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
