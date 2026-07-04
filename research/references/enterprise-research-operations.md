# Enterprise Research Operations

Use this reference when research is meant to support a business, policy,
procurement, diligence, risk, executive, customer, or other organizational
decision. It turns the general research process into a decision-grade operating
standard.

## Enterprise Research Standard

Enterprise-ready research must be:

- decision-linked: the output says what decision, recommendation, risk, or next
  action the evidence can support
- auditable: important claims can be traced to inspected sources, search paths,
  provenance, and verification results
- reproducible enough: another analyst can see what was searched, what was not
  searched, and why the stop rule was reached
- converged: material leads from internal, connected, public, and blocked
  source families are followed, closed, blocked with confidence effect, or
  shown unable to change the decision
- permission-aware: sensitive, internal, proprietary, personal, or regulated
  sources are only used when authorized and necessary
- calibrated: confidence reflects evidence quality, not polish or source count
- stakeholder-usable: findings are shaped for the audience without hiding caveats

Do not convert research into confident advice when the evidence only supports a
bounded evidence summary, risk register, option comparison, or unresolved issue
map.

## Intake And Decision Framing

Before collecting evidence, define the decision context when available:

| Field | Record |
|---|---|
| Decision / output | recommendation, briefing, memo, landscape, vendor comparison, risk assessment, diligence note, literature review, source coverage table, data table |
| Decision owner / audience | executive, product, legal, policy, finance, sales, customer team, researcher, individual user |
| Decision deadline | hard date, soft date, or not specified |
| Decision criteria | cost, risk, compliance, feasibility, performance, evidence strength, market timing, strategic fit, user impact |
| Materiality threshold | what size, probability, severity, cost, or confidence difference would change the decision |
| Scope boundaries | geography, jurisdiction, segment, population, entity list, product/version, time horizon, source types |
| Exclusions | sources, jurisdictions, time periods, entities, claims, or sensitive records intentionally out of scope |
| Currentness requirement | historical, as-of timestamp, latest status, ongoing monitoring, or living review |

If the user does not provide criteria and they materially change the research
path, ask a narrow clarifying question. Otherwise state working criteria in
`## What I Checked` and test them against the evidence.

## Governance And Access Boundaries

Apply least-privilege research collection:

- use only authorized connectors, files, systems, and source families
- avoid collecting personal data, confidential data, customer records, employee
  records, secrets, credentials, payment data, health data, or legally sensitive
  material unless it is necessary for the stated purpose and explicitly
  authorized
- prefer aggregate, redacted, or de-identified evidence when it answers the
  question
- distinguish `not found`, `not searched`, `not accessible`, and `not collected
  due to sensitivity`
- record source-system access boundaries in `## What I Checked` or
  `## What I Did Not Check`
- do not export, copy, or persist sensitive source content into research records
  when a pointer, redacted summary, or metadata row is sufficient
- for legal, medical, financial, clinical, safety, employment, or regulated
  decisions, frame outputs as research support unless the user has explicitly
  asked for a different professional work product and the environment supports
  it

Classify enterprise source sensitivity before using internal or connected
sources:

| Data Class | Examples | Handling Rule |
|---|---|---|
| public | public web, official filings, public docs | cite normally after source checks |
| internal | internal wiki, tickets, project docs | use only when authorized; cite path or record pointer |
| confidential | customer names, contracts, pricing, strategy, nonpublic financials | minimize excerpts; summarize only what is necessary |
| personal | employee, user, applicant, contact, account, or identity data | prefer aggregate or redacted evidence; avoid persistence unless necessary |
| regulated | health, financial account, legal, minors, government IDs, protected classes | use only with explicit need and authority; trigger professional/compliance review language |

Do not infer permission from technical accessibility. If access is ambiguous,
mark the source family `not searched / authorization unclear` rather than
collecting it.

## Privacy And Compliance SOP

For internal, confidential, personal, regulated, privileged, customer, employee,
or legally sensitive material, record:

| Control | Requirement |
|---|---|
| Access approval | access basis, requesting user, authorized connector/path, and any denied/unclear systems |
| Minimum necessary | why the source is needed and whether aggregate/redacted evidence would suffice |
| Redaction | personal identifiers, secrets, customer names, privileged excerpts, and unnecessary sensitive details removed or summarized |
| Retention | whether sensitive content is persisted, referenced by pointer only, or omitted from the record |
| Deletion/disposal | cleanup or non-retention note for temporary exports, screenshots, or excerpts |
| Redistribution | unrestricted, internal only, restricted, do not quote, metadata only, or owner approval required |
| Privilege/legal hold | mark privileged or legal-hold material; do not quote broadly; require counsel/owner review |
| Regulated data | health, financial account, government ID, minors, protected class, employment, or similar data triggers owner/SME review |
| Conflict of interest | sponsor, funder, vendor, analyst, or stakeholder incentives that may affect source independence |
| External sharing | do not prepare externally shareable language unless explicitly requested and approved |

If a required privacy/compliance control is unclear, downgrade decision-use
status or mark the relevant source family `not searched / authorization unclear`.

## Workplan

For enterprise work, create a compact workplan in `## Search Path` before heavy
collection:

| Workstream | Purpose | Source Families | Owner | Output | Stop Gate |
|---|---|---|---|---|---|
| W1 | source-of-truth | official/internal canonical sources | main/subagent | claim rows | governing source checked or unavailable |
| W2 | market/data/literature | empirical and external context | main/subagent | source rows | method and comparability checked |
| W3 | counterevidence | risks, objections, disconfirming cases | main/subagent | gap rows | material counterclaims checked |
| W4 | currentness/provenance | freshness, lineage, supersession | main/subagent | verification rows | currentness and lineage resolved |
| W5 | frontier queue convergence | material leads, blocked primary sources, unresolved source-family paths | main/subagent | Lead Ledger / Coverage Debt rows | no material open lead remains without follow-up, closure reason, blockage, or confidence effect |

Use subagents for independent lanes when available. The main agent remains the
only writer for the research record and owns synthesis.

## Deliverable Patterns

Choose the smallest user-facing answer shape that can support the decision, but
do not lower the research protocol or split artifacts. The full evidence trail
still belongs in the single Markdown research record:

- `executive brief`: answer first, confidence, decision implications, caveats,
  sources checked, open risks
- `decision memo`: options, criteria, evidence by criterion, recommendation,
  downside risks, conditions that would change the recommendation
- `vendor/product comparison`: comparable criteria, pricing/availability,
  implementation constraints, support/security/compliance notes, total cost,
  missing data
- `risk register`: claim/risk, likelihood, impact, evidence, controls,
  owner/action, confidence, watch items
- `market or competitor landscape`: market definition, segments, actors,
  evidence strength, uncertain estimates, trigger events, strategic implications
- `literature or evidence review`: search scope, inclusion logic, evidence map,
  quality appraisal, synthesis, limitations
- `source audit`: claim inventory, source lineage, provenance, currentness,
  conflicts, unresolved gaps

Every enterprise deliverable must separate:

- facts directly supported by inspected evidence
- estimates or modeled judgments
- stakeholder claims and incentives
- analyst assessment
- assumptions
- open questions and decision risks

## Decision Matrix

For evaluative, comparative, vendor, strategy, or recommendation research,
include a decision matrix in the single research record unless clearly not
applicable:

```markdown
## Decision Matrix

| Option / Claim | Criterion | Evidence | Source IDs | Confidence | Decision Implication | What Would Change This |
|---|---|---|---|---|---|---|
| ... | ... | ... | S1, S4 | high / medium / low / insufficient | ... | ... |
```

Do not score or rank options numerically unless criteria weights and measurement
bases are explicit enough to make the score meaningful. Prefer categorical
ratings with caveats over false precision.

## Source Reliability Rubric

Use source quality labels from `source-verification.md` for records. When an
enterprise decision needs a more explicit reliability judgment, score candidate
sources with this compact rubric:

| Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Authority | unknown or weak origin | contextual source | expert/credible secondary | primary, governing, or source-of-truth |
| Directness | does not address claim | adjacent/background | partial support | directly supports exact claim |
| Currentness | stale or undated | date unclear or likely old | current enough with caveat | latest/supersession checked |
| Independence | duplicate lineage | single lineage | partially independent | materially independent corroboration |
| Method transparency | no method | opaque method | partial method | method/data definitions inspectable |
| Conflict / COI risk | unresolved material conflict | notable limitation | minor disclosed limitation | no material unresolved conflict found |

Map the score qualitatively:

- `strong`: mostly 3s, no unresolved material conflict, direct inspected support
- `adequate`: enough 2s/3s for the decision, limitations visible
- `weak`: indirect, stale, opaque, single-lineage, or only partially relevant
- `unusable`: uninspected, snippet-only, AI-summary-only, unsupported,
  provenance-unclear for the target claim, or materially contradicted

Do not average scores into false precision. A single `0` on inspected body,
directness, or provenance can make a source unusable for a firm claim even if
other dimensions look strong.

## Quality Gates

Before final synthesis, complete these enterprise gates or mark them `not
applicable` with a reason:

| Gate | Pass Condition |
|---|---|
| Intake | decision/output, audience, scope, criteria or working criteria, and currentness requirement are recorded |
| Decision fit | output directly answers the user's intended decision or explains why evidence cannot support it |
| Criteria coverage | each decision criterion is supported, unsupported, or explicitly out of scope |
| Source authority | important claims use the strongest available source family or are downgraded |
| Provenance | used sources have inspected body/retrieved record, lineage, date/version, and evidence location |
| Corroboration | central nontrivial claims have independent support or are labeled single-source/insufficient |
| Counterevidence | material objections, contradictory sources, and failure cases were searched and recorded |
| Currentness | current-dependent claims have latest-update, supersession, or as-of checks |
| Sensitivity | private, personal, regulated, or confidential data handling is minimized and recorded |
| Reproducibility | Search Craft Log, Wave Log, Lead Ledger, frontier queue convergence, source-family coverage, and verification lanes are complete |
| Stakeholder readability | confidence, caveats, implications, and next actions are visible without reading every note |

If a gate fails, run a targeted gap pass, downgrade affected claims, or present
the result as incomplete rather than decision-ready.

Use `passed`, `failed`, `blocked`, or `not applicable`. For research records
checked for enterprise use, required gates must be `passed`;
conditional `not applicable` rows need a concrete reason. Do not use waived
gates for professional-grade work.

## Executive Synthesis Rules

- Start with the answer, then the evidence basis, then caveats.
- Use finding-style headings that state conclusions, not topics.
- Preserve uncertainty in the same sentence as the claim it qualifies.
- State what was checked and what would most likely change the conclusion.
- Do not bury a single-source, stale, inaccessible, or method-opaque limitation
  in a footnote-style caveat when it affects the decision.
- Separate "recommended now", "reasonable if conditions hold", "defer", and
  "insufficient evidence" outcomes.

## Monitoring And Reuse

When the topic may change after delivery, record monitoring triggers:

- source update pages, dockets, changelogs, release notes, filings, dashboards,
  or datasets to watch
- decision expiry date or recommended refresh cadence
- trigger events that should reopen the research
- claims most vulnerable to change
- unresolved leads worth following if access or time changes
- frontier queue items that could not be followed because access, sensitivity,
  ownership, or tooling changed

Research records are reusable only if their scope, as-of date, source coverage,
and confidence labels are still valid for the new decision. Otherwise reuse them
as leads, not as current evidence.
