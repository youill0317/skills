# Quality Rubric

Use this rubric for professional, enterprise, externally reviewed, high-stakes,
decision-ready, or research-firm-replacement work.

## Rating Labels

- `Pass`: all hard blockers clear, total score meets threshold, no
  decision-critical dimension below threshold
- `Conditional Pass`: usable only with explicit caveats, owner review, or
  bounded decision-use status
- `Fail`: hard blocker present, important claims unsupported, or final synthesis
  cannot support the requested decision

## Hard Blockers

Any hard blocker prevents `professional-grade`:

- a decision-relevant claim lacks inspected/retrieved source support
- a used source is based only on snippet, AI summary, generated overview, or
  uninspected citation
- current-dependent claim lacks as-of/latest-update/supersession check
- material source-family gap is hidden or mislabeled as `not found`
- material conflict is unresolved but final answer gives a firm conclusion
- high-stakes claim lacks governing/primary source or required owner/SME review
- internal/sensitive source lacks access basis and sensitivity handling
- red-team or required verification lane has blocking unresolved findings
- final deliverable does not answer the user's decision/question

## 100-Point Rubric

Score each dimension with evidence from the single research record, including
`## Evidence`, `## Sources`, `## Search Path`, `## Verification Notes`, and
`## Coverage Gates`.

| Dimension | Points | Full-Credit Standard |
|---|---:|---|
| Scope and decision fit | 10 | question, audience, scope, exclusions, materiality, and decision/output are explicit |
| Source authority and directness | 12 | strongest source families used; central claims supported by direct primary/original/governing evidence where needed |
| Source-family coverage | 10 | primary, empirical/method, secondary/context, counterevidence, and domain-specific families checked or justified unavailable |
| Claim traceability | 10 | every important claim maps to source IDs, evidence location, confidence, and disposition |
| Provenance and lineage control | 8 | original/mirror/archive/excerpt roles, duplicate lineages, source-of-claim, and mutable-source custody are tracked |
| Search reproducibility | 8 | scout, target, snowball, gap-pass queries/paths, filters, source systems, and dates are recorded |
| Method and data appraisal | 8 | denominators, definitions, samples, uncertainty, comparability, data vintage, and limitations checked where relevant |
| Counterevidence and alternatives | 8 | contradiction, negative cases, rebuttals, and plausible alternatives searched and reflected |
| Currentness and supersession | 6 | current claims have as-of timestamp, newest-source check, and supersession status |
| Privacy, ethics, and access control | 6 | sensitive data minimized; access basis, redistribution, and owner-review triggers recorded |
| Synthesis calibration | 8 | final answer does not exceed evidence; uncertainty and gaps change claim strength |
| Deliverable usefulness | 6 | answer, implications, caveats, next actions, and audience-specific format are clear |

Thresholds:

- `Professional-grade`: 90+ points, no hard blocker, no decision-critical
  dimension below 8/10 equivalent, independent QA passed
- `Decision-ready with caveats`: 80-89 points, no hard blocker, caveats do not
  undermine the scoped decision
- `Research support only`: 65-79 points or missing independent QA
- `Fail / not decision-ready`: below 65 points, any hard blocker, or unsupported
  central conclusion

Do not use a total score to override a hard blocker.

## Required Record Row

```markdown
## Quality Rubric Result

| Dimension | Points Earned | Max | Evidence | Gap / Action |
|---|---:|---:|---|---|
| Scope and decision fit | ... | 10 | ... | ... |

Total: ... / 100
Label: professional-grade / decision-ready with caveats / research support only / not decision-ready
Hard blockers: none
```
