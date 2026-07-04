# Acceptance Tests

Run these tests before final synthesis for professional, enterprise,
externally-reviewed, high-stakes, or decision-ready research.

## Test Matrix

Record the result in the single research record under `## Coverage Gates`.

```markdown
## Acceptance Tests

| Test | Required? | Result | Evidence / Location | Remediation |
|---|---|---|---|---|
| Claim Support Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Snippet Leakage Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Source-Family Coverage Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Currentness Test | conditional | pass / fail / blocked / not applicable | ... | ... |
| Counterevidence Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Provenance / Lineage Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Method / Data Test | conditional | pass / fail / blocked / not applicable | ... | ... |
| Sensitivity / Access Test | conditional | pass / fail / blocked / not applicable | ... | ... |
| Synthesis Overreach Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Decision Usefulness Test | conditional | pass / fail / blocked / not applicable | ... | ... |
| Deliverable Readability Test | yes | pass / fail / blocked / not applicable | ... | ... |
```

## Test Definitions

- `Claim Support Test`: every important claim appears in the claim register and
  maps to inspected/retrieved sources or is labeled `insufficient`.
- `Snippet Leakage Test`: no source marked `used` relies only on snippets,
  generated overviews, AI summaries, abstracts when full text is needed, or
  unsupported secondary claims.
- `Source-Family Coverage Test`: required source families are checked,
  unavailable, or explicitly not applicable with reasons.
- `Currentness Test`: current-dependent claims have as-of timestamp,
  latest-update/supersession check, and source date/version.
- `Counterevidence Test`: the strongest plausible counterclaims, contradictions,
  negative cases, and limitations were searched and reflected in confidence.
- `Provenance / Lineage Test`: original/source-of-claim, duplicate lineage,
  mirror/archive/excerpt role, and mutable-source custody are recorded.
- `Method / Data Test`: quantitative, scientific, survey, benchmark, or
  forecast claims have denominator, method, uncertainty, vintage, and
  comparability checks.
- `Sensitivity / Access Test`: internal, confidential, personal, regulated, or
  privileged sources have access basis, sensitivity, minimum-necessary status,
  and redistribution limits.
- `Synthesis Overreach Test`: final synthesis does not say more than inspected
  evidence supports.
- `Decision Usefulness Test`: decision options, criteria, implications,
  residual risks, and what would change the conclusion are visible when relevant.
- `Deliverable Readability Test`: final output is readable as a brief or memo,
  not just a raw evidence dump.

## Failure Handling

Failed required tests trigger the loop in `qa-iteration-loop.md`. If a required
test remains failed after targeted remediation, downgrade the final label and
state the blocking gap in `## Answer`, `## Counterevidence / Uncertainty`, or
`## Open Questions` as appropriate.
