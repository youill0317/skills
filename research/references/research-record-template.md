# Research Record Template

Use this reference when writing workspace-local research records under:

```text
gigantum-humeris/research/<NNN-topic>.md
```

Use the next available 3-digit prefix by scanning existing
`gigantum-humeris/research/<NNN>-*.md` files, then append a short ASCII slug from
the research question.

## File Shape

```text
gigantum-humeris/research/
  001-short-topic.md
  002-another-topic.md
```

Do not create a topic folder, `brief.md`, `sources.md`, or `notes.md`.

## Principle

The record exists to preserve the evidence trail, not to satisfy a large report
format. Keep one readable file that shows the question, answer, source support,
counterevidence, uncertainty, search path, verification work, coverage gates,
and stop-rule reasoning.

## Template

```markdown
# Research: <Topic>

Date: YYYY-MM-DD
User request: ...
Scope: ...
As of: YYYY-MM-DD HH:MM timezone, when current facts matter

## Answer

Short decision-ready answer or synthesis.

## Key Findings

- Finding with source IDs, such as S1 or S2.

## Evidence

For each important claim, name the supporting source IDs and the evidence
location inside those sources.

## Sources

| ID | Source | Type | Accessed / As Of | Why Used | Key Evidence | Limits |
|---|---|---|---|---|---|---|
| S1 | Title and URL/path | official / primary / dataset / expert / secondary / contextual | YYYY-MM-DD | why this source matters | section, page, table, line, timestamp, or field | limits, bias, stale risk, access limits |

## Counterevidence / Uncertainty

Conflicting evidence, weak spots, source limits, and what would change the
answer.

## What I Checked

Source families, query paths, documents, datasets, or connectors inspected.

## What I Did Not Check

Relevant source families, leads, or checks not completed, with reasons.

## Search Path

What searches, source families, databases, connectors, or documents were used.
Include enough detail that a future agent can reconstruct the investigation.
Record scout, target, snowball, and gap-pass work.

## Leads Followed

Important citations, datasets, authors, laws, standards, product pages,
counterclaims, or related terms followed during the research.

## Dead Ends

Searches or leads that failed, repeated known evidence, were inaccessible, or
were rejected as low quality.

## Verification Notes

Claim checks, source-quality checks, currentness checks, counterevidence checks,
source-lineage checks, and synthesis-overreach checks performed before
finalizing.

### Evidence Ledger

| Claim | Support | Counterevidence | Source Quality / Lineage | Currentness | Confidence | Decision |
|---|---|---|---|---|---|---|
| Claim text | S1 section/page | none found / S2 conflicts | primary / independent / same lineage | checked YYYY-MM-DD | high / medium / low / insufficient | use / downgrade / exclude / unresolved |

## Coverage Gates

State which gates passed, failed, were blocked, or were not applicable:

- scout
- target
- snowball
- gap pass
- source audit
- claim verification audit
- currentness audit
- contradiction and gap audit
- synthesis-overreach audit
- method/data audit, when applicable

Explain why the stop rule was reached, or list unresolved gaps and affected
claims.

## Confidence

Confidence by important claim or subquestion: high / medium / low /
insufficient.

## Open Questions

Unresolved issues, pending leads, or checks that would matter for a later
refresh.
```

Use source IDs from `## Sources` throughout the file. A used source must have an
inspected body or retrieved record; snippets, AI summaries, generated summaries,
and search result previews are leads, not evidence.

## Optional Additions

Add a compact decision matrix, claim table, timeline, or domain-specific table
only when it clarifies the answer. Do not create large tables merely to satisfy
format. For professional or enterprise work, record any extra quality gates in
`## Coverage Gates`, but keep them proportional to the decision risk.
