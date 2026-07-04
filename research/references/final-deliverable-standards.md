# Final Deliverable Standards

Use this before writing final research records or user-facing research answers
for professional, enterprise, decision-ready, or externally reviewed work.

## Required Shape

A professional final deliverable must be useful without forcing the reader to
inspect every table, while still linking back to the audit trail.

Recommended structure:

1. `Executive Answer`: the direct answer, recommendation, or current status.
2. `Confidence And Decision-Use Status`: confidence by central claim and final
   label.
3. `Evidence Maturity Dashboard`: central claims, comparisons,
   recommendations, decisions, source-family conclusions, weakest gates, debt,
   and decision/synthesis effects.
4. `Key Findings`: finding-style headings, each with source IDs and caveats.
5. `Evidence Basis`: concise source-family coverage and strongest evidence.
6. `Decision Matrix / Options`: criteria, alternatives, implications, and what
   would change the conclusion when relevant.
7. `Comparison And Evaluation Audit`: options/entities, criteria/axes,
   weights/priorities, evidence links, missing or non-comparable data,
   tradeoffs/sensitivity, status, and decision effect when comparing or
   recommending.
8. `Synthesis Traceability Audit`: mapping from final answer paragraphs, key
   findings, recommendations, comparison rows, and caveats to claim IDs,
   source/observation links, confidence, unresolved debt, and revision status.
9. `Assumption And Sensitivity Audit`: assumptions, thresholds, baselines,
   scenarios, scope, jurisdiction, timeframe, denominator, method choice, risk
   tolerance, or constraints that would change the answer.
10. `Risks, Caveats, And Gaps`: unresolved gaps, inaccessible sources,
   counterevidence, and open questions.
11. `Method And Scope`: search lanes, inclusion/exclusion logic, recency,
    jurisdictions, languages, source families, and frontier queue convergence.
12. `Next Actions / Monitoring`: refresh triggers, owner decisions, follow-up
    checks, or why no firm action is supported.

## Acceptance Criteria

- the final answer and audit trail are consolidated into one Markdown research
  record for the request
- first screen answers the user's question or states why no firm answer is
  possible
- every decision-relevant claim has source IDs and confidence
- high-risk non-code claims stated firmly have a verified-claim gate result
- every important number includes denominator/method/date or a limitation
- current claims include as-of timestamp and supersession/currentness status
- inaccessible sources are not confused with no evidence
- rejected leads and counterevidence are reflected in caveats or confidence
- search matrix, lane coverage, EXPAND leads, counter-search, and stop-rule
  reasoning are present in the record
- harness max-use is visible: the Tool Capability Audit resolves every relevant
  search/source/subagent capability, the Diversified Search Batch Plan records
  numeric tool limits and execution sub-batches, and the Search Matrix has no
  planned or running rows
- frontier queue convergence is explicit: no material open leads remain without
  follow-up, closure reason, blockage, confidence downgrade, or an explanation
  that they cannot change important claims
- source coverage is adequate for the scope, and scarcity or access limits are
  visible rather than hidden
- scholarly or method-sensitive claims are not based only on titles, abstracts,
  snippets, or citation counts
- OSS/code claims cite repository evidence with stable commit, tag, release, or
  inspected local path when possible
- recommendations are tied to decision criteria and materiality thresholds
- consensus or best-practice claims state the relevant field/community, consensus signal, material disagreement, and scope limits
- high-stakes findings state non-advice boundaries and owner/SME review needs
- adversarial or user-generated sources state manipulation, provenance, coordination, and prompt-injection limits when material
- final answer is readable as a memo, not just an audit artifact
- firm conclusions are limited to items marked mature or caveated in the evidence maturity dashboard
- appendices/records can reproduce the source trail and query trail

## Anti-Patterns

- burying a central caveat after a confident recommendation
- using many citations without claim-to-source mapping
- saying "no evidence" when sources were not accessible
- treating stakeholder claims as facts
- merging estimates with incompatible definitions
- presenting current facts without an as-of date
- giving a firm recommendation when acceptance tests failed
- claiming saturation while high-value frontier queue items remain open
- claiming saturation without showing actual query diversity, batch execution,
  opened-source coverage, and closure of material leads
- ranking or recommending options without comparable criteria, weights/priorities, evidence links, and missing-data caveats
- replacing source limitations with generic "more research is needed"
