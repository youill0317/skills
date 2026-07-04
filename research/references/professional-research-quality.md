# Professional Research Quality

Use this reference for professional, enterprise, high-stakes, externally
reviewed, board/executive, diligence, procurement, policy, litigation-support,
investment-style, OSINT, evidence-synthesis, or research-firm-replacement work.

This file does not replace domain references. It adds a quality management layer
that tests whether the research process and deliverable are good enough to rely
on outside casual analysis.

Load alongside:

- `quality-rubric.md` for scored pass/conditional/fail evaluation
- `acceptance-tests.md` for required completion tests
- `sample-scenarios.md` when benchmarking or improving the skill itself
- `qa-iteration-loop.md` when any gate or verification lane fails
- `final-deliverable-standards.md` before writing professional final output
- `high-stakes-domain-protocols.md` for clinical, financial, legal-support,
  OSINT, security, procurement, customer/UX, or regulated-domain research

## Standard

A research record is professional-grade only when it is:

- scoped to a real decision, question, or intelligence requirement
- explicit about assumptions, exclusions, source access, and confidence
- built from inspected source bodies or retrieved records, not snippets or AI
  summaries
- reproducible enough for another analyst to understand the search path
- robust to counterevidence, conflicting sources, and source-lineage failures
- clear about sensitivity, permissions, and redistribution limits
- delivered in a format the intended audience can act on
- independently reviewed against claim support, source quality, currentness,
  synthesis overreach, and record completeness

If the work fails any must-pass gate, label it `not professional-grade yet` and
state the blocking gap.

## Operating Model

For professional-grade research, run the work through stage gates. The main
agent may execute several gates in one sitting, but the record must show that
each gate was considered.

| Gate | Purpose | Required Record Evidence |
|---|---|---|
| G0 Intake | confirm decision, audience, scope, risk, deadline, allowed/forbidden sources, deliverable, and confidence threshold | visible framing, scope/exclusion notes, access boundaries |
| G1 Research Design Review | test whether evidence needs, source families, lanes, stop rule, and red-team plan can answer the question | search plan, source-family coverage plan, lane plan, stop gates |
| G2 Evidence Collection | gather and inspect sources while preserving provenance and rejected leads | source map, candidate table, query ledger, lead graph, rejection reasons |
| G3 Evidence Table Before Narrative | complete claim register and evidence table before writing persuasive synthesis | claim register, source-to-claim mapping, confidence labels |
| G4 Independent QA / Red Team | attack claim support, source quality, currentness, lineage, sensitivity, and overreach | verification lanes and red-team findings |
| G5 Delivery Acceptance | verify final deliverable answers the decision and meets quality thresholds | scorecard, acceptance gates, final label |
| G6 Post-Delivery Control | support correction, revalidation, and source-update handling | audit/change log, expiry/revalidation triggers, errata notes |

## RACI And Escalation

Use a lightweight role model:

| Role | Responsibility |
|---|---|
| Main agent / lead analyst | framing, lane design, source integration, claim register, synthesis, final label |
| Research subagent | bounded source discovery and lane rows only |
| Verification subagent | independent audit of claim support, source quality, currentness, gaps, and overreach |
| Red-team reviewer | adversarial review of the easiest ways the conclusion could be wrong |
| User / decision owner | clarifies decision criteria, allowed sources, risk tolerance, and acceptance of residual gaps |
| Domain owner / SME | reviews high-stakes, regulated, legally sensitive, security, clinical, financial, or specialized technical conclusions when required |

Escalate to owner/SME review, or mark `requires owner review`, when the research
would affect legal obligations, medical/clinical decisions, financial exposure,
security controls, regulatory compliance, employment decisions, public
statements, customer commitments, contractual obligations, or material
procurement.

## Time, Budget, And Depth Control

Professional research still needs bounded scope. Record constraints explicitly:

- deadline or timebox
- expected deliverable depth
- mandatory source families
- optional source families
- unavailable paid databases or proprietary sources
- acceptable confidence threshold
- what must be true to stop

If constraints prevent the professional standard from being met, do not silently
lower the bar. Label the result `decision-ready with caveats`, `research support
only`, or `not decision-ready`.

## Quality Scorecard

Before calling research professional-grade, score the work in `## Coverage Gates`:

```markdown
## Professional Quality Scorecard

| Dimension | Score | Evidence | Gap / Remediation |
|---|---|---|---|
| Scope and decision fit | 0-4 | ... | ... |
| Source authority and coverage | 0-4 | ... | ... |
| Provenance and auditability | 0-4 | ... | ... |
| Search reproducibility | 0-4 | ... | ... |
| Method and data quality | 0-4 | ... | ... |
| Counterevidence and alternatives | 0-4 | ... | ... |
| Currentness and supersession | 0-4 | ... | ... |
| Synthesis calibration | 0-4 | ... | ... |
| Privacy, compliance, and access control | 0-4 / N/A | ... | ... |
| Stakeholder deliverable quality | 0-4 | ... | ... |
```

Scoring:

- `4`: strong enough for professional external review
- `3`: usable with visible limitations
- `2`: material gap; decision use needs caveats or owner review
- `1`: weak; useful mainly as lead generation
- `0`: absent or failed

Minimum acceptance:

- no required dimension at `0`
- no decision-critical dimension below `3`
- all high-stakes/current/provenance-sensitive claims have direct inspected
  support or are labeled `insufficient`
- privacy/access gates pass or are explicitly not applicable
- independent verification lanes pass after any required gap pass

Do not average scores into a pass. A single failed must-pass dimension blocks a
professional-grade label.

## Must-Pass Acceptance Gates

Use this checklist in addition to `enterprise-research-operations.md`:

| Gate | Must Pass When | Pass Condition |
|---|---|---|
| Fit for purpose | always | answer maps to the requested decision, question, or deliverable |
| Claim traceability | always | every important claim maps to source IDs and evidence locations |
| Source-body inspection | always | every used source was inspected/retrieved; snippets and AI summaries are leads only |
| Source-family coverage | always | required primary, data/method, secondary/context, and counterevidence families are checked or justified unavailable |
| Search reproducibility | always | query ledger includes scout, target, snowball, gap-pass paths with dates/filters/source systems |
| Provenance and lineage | always | source lineage, original/mirror/archive/excerpt role, and duplicate lineages are recorded |
| Currentness | current-dependent claims | latest-update/supersession/as-of checks are recorded |
| Method appraisal | data, statistics, surveys, science, benchmarks, forecasts | denominator, definitions, sample/method, uncertainty, and comparability are checked |
| Conflict handling | any conflict or plausible alternative | contradictions are resolved, bounded, or carried as explicit uncertainty |
| Sensitivity and authorization | internal/sensitive sources | access basis, sensitivity, minimum necessary use, and redistribution limits are recorded |
| Independent review | professional-grade claim | fresh verification or red-team lane has passed |
| Decision readiness | enterprise action | decision-use status is `usable` or `usable with caveats`; owner review needs are explicit |

## Red-Team Review

For professional-grade work, add at least one independent red-team verification
lane after the provisional synthesis. Its job is to attack the result, not to
polish it.

Red-team prompt contract:

- identify the three most important claims
- find the easiest way each claim could be wrong
- look for missing source families, circular reporting, stale sources, weak
  methods, overbroad scope, and omitted counterevidence
- test whether the recommendation changes under reasonable alternative
  assumptions
- mark each issue as `blocking`, `material caveat`, `minor`, or `not an issue`
- return only audit findings; do not rewrite the record

Blocking red-team findings require one of:

- targeted gap pass and re-review
- claim downgrade to `low` or `insufficient`
- decision-use status changed to `not decision-ready`
- explicit user-facing unresolved-gap statement

## OSINT And Public-Claim Controls

Use these controls for public-claim verification, investigations, profiles,
screenshots, social posts, media, conflicts, fraud/scam checks, sanctions,
litigation, reputational risk, or adversarial information environments:

- preserve chain-of-custody metadata: original URL, archive URL, capture time,
  platform/account, media hash when available, and retrieval method
- separate observation from accusation; do not infer intent, identity, or guilt
  without direct evidence
- check impersonation, handle reuse, account age, account takeover, parody,
  coordinated posting, bot/amplification risk, and platform moderation context
- for media, check original upload, metadata availability, crop/edit signs,
  reverse image/video search leads, geolocation/chronolocation leads, and
  whether specialist media forensics is required
- for person/entity profiles, disambiguate aliases, native-script names,
  identifiers, dates, affiliations, jurisdictions, and lookalikes before joining
  records
- for harmful or personal information, apply privacy minimization: collect only
  what is necessary, avoid publishing unnecessary personal details, and
  summarize sensitive findings at the least harmful granularity
- for legal or safety-sensitive findings, distinguish public allegation,
  official charge, judgment, sanction, settlement, denial, and unresolved claim

If media authentication, geolocation, identity proof, or platform manipulation
analysis is central and cannot be performed with authorized tools/sources, label
the relevant claim `insufficient` or `requires specialist review`.

## Benchmark Scenarios

Use benchmark scenarios to evaluate whether the skill can repeatedly produce
professional research. Pick scenarios that match the user's domain, or use these
defaults:

| Scenario | Required Capabilities |
|---|---|
| vendor selection | criteria definition, market scan, pricing/terms, security/compliance, customer evidence, total cost, recommendation caveats |
| regulatory landscape | jurisdiction matrix, governing text, pending rules, enforcement/guidance, effective dates, applicability, owner-review trigger |
| market sizing | market definition, source lineage, estimate methodology, base year, geography, forecast assumptions, conflicting estimates |
| technical/product due diligence | official docs, changelog, source/release tags, issues/security advisories, reproducibility inputs, migration risks |
| public claim/OSINT verification | source-of-claim tracing, archives, media/quote variants, independent corroboration, contradiction handling |
| scholarly evidence review | database coverage, inclusion logic, full-text method extraction, quality appraisal, citation snowballing, retraction/preprint status |
| internal decision audit | canonical docs, implementation reality, decision history, owner/team, stale-doc conflicts, access/sensitivity controls |

For each benchmark, evaluate:

- Did the framing ask only necessary clarifying questions?
- Did the search plan cover expected source families?
- Did the record include source map, candidate table, claim register, query
  ledger, lead queue, verification lanes, and scorecard?
- Did the final synthesis answer the decision without overstating evidence?
- Would a reviewer be able to reproduce the reasoning from the record?

## Failure Mode Checklist

Actively search for these failures before final synthesis:

- objective drift from the user's actual decision or question
- treating search results, snippets, or AI summaries as evidence
- circular reporting or repeated copies of one source lineage
- overreliance on a single convenient source
- missing original-language or jurisdiction-local sources
- stale sources presented as current
- uninspected methods behind statistics, surveys, or benchmarks
- denominator, geography, date, version, or unit mismatch
- untested counterevidence or alternative explanations
- hidden conflicts of interest or stakeholder incentives
- inaccessible source family treated as `not found`
- private or sensitive content over-collected or over-quoted
- subagent hallucinated source metadata or unsupported confidence
- final answer stronger than source support
- decision recommendation without decision criteria

## Iterative Improvement Loop

When improving the skill itself, repeat:

1. independent evaluator audits current skill against this reference
2. main agent patches the smallest set of research skill files that address
   blocking and material findings
3. fresh independent evaluator re-audits the changed skill
4. continue until there are no blocking findings and no material findings that
   can be resolved in the current workspace

Do not mark the skill itself as professional-grade merely because references are
comprehensive. It must include operational instructions, record templates,
verification gates, and acceptance criteria that make professional behavior
repeatable.

## Final Labeling

Use these labels for completed research:

- `professional-grade`: all must-pass gates pass; scorecard meets minimums;
  red-team review passed or all findings resolved
- `decision-ready with caveats`: usable for the scoped decision with stated
  limits, assumptions, owner-review needs, or confidence constraints
- `research support only`: useful evidence summary but not sufficient for a
  decision
- `not decision-ready`: blocked by missing source families, weak provenance,
  unresolved conflicts, currentness gaps, or sensitivity/access constraints
