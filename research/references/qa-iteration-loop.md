# QA Iteration Loop

Use this when verification fails, red-team review finds gaps, acceptance tests
fail, or the research skill itself is being improved.

## Loop

```text
Draft 0 -> QA audit -> targeted gap pass -> integrate -> re-audit -> final label
```

## Required Steps

1. Create provisional synthesis only after `## Sources`, `## Source Coverage`,
   `## Search Matrix`, `## Search Craft Log`, `## Wave Log`,
   `## Tool Capability Audit`, `## Diversified Search Batch Plan`,
   `## Lead Ledger`, `## Source-Opened Follow-Up Audit`,
   `## Expansion Frontier Audit`, `## Saturation Metrics`, and
   `## Claim Ledger` exist in the single record.
2. Run acceptance tests from `acceptance-tests.md`.
3. Run independent verification lanes from `subagent-orchestration.md`.
4. For professional-grade work, run red-team review from
   `professional-research-quality.md`.
5. Convert each failed test or red-team finding into a targeted gap-pass task.
6. Re-run only the affected acceptance tests and verification lanes, plus
   synthesis-overreach review.
7. Update claim confidence, decision-use status, quality score, and final label.

## Failure Rules

- If the same important claim fails support twice, label it `insufficient` or
  remove it from the firm synthesis.
- If currentness cannot be verified for a current-dependent central claim, label
  the claim `insufficient` and the deliverable `not decision-ready` unless the
  final answer is explicitly historical.
- If a material source family is inaccessible, record `not accessible`, state
  impact, and do not infer from weaker sources without a caveat.
- If frontier queue convergence fails, convert the highest-impact open leads
  into a targeted EXPAND or gap pass, or close/block them with confidence
  effects before firm synthesis.
- If the record does not show harness max-use through resolved
  `## Tool Capability Audit`, numeric sub-batches in
  `## Diversified Search Batch Plan`, closed `## Search Matrix` rows, and
  saturation metrics for query diversity, inspected sources, expansion waves,
  counter-search, local/jurisdictional sweeps, and material lead closure, run a
  search-pressure gap pass before any firm synthesis.
- If independent QA is unavailable and only self-audit is performed, do not use
  `professional-grade` or `research-firm-replacement`; the strongest label is
  `research support only` unless the user explicitly accepts self-audit as
  sufficient for a lower-risk task.
- If owner/SME review is required and unavailable, use `requires owner review`
  or `not decision-ready`.

## Iteration Log

The single research record must include this under `## Verification Notes`:

```markdown
## QA Iteration Log

| Iteration | Trigger | Action | Re-Tested | Result | Label Impact |
|---|---|---|---|---|---|
| 0 | initial QA | ... | ... | pass / fail | ... |
| 1 | RT1 blocking finding | targeted gap pass | Claim Support, Frontier Queue Convergence, Synthesis Overreach | pass / fail | downgraded / restored / unchanged |
```

Stop only when required tests pass, or when remaining gaps are explicit and the
final label is downgraded accordingly.
