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
- converged through a visible frontier queue, not merely many independent
  searches
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
| G2 Evidence Collection | gather and inspect sources while preserving provenance and rejected leads | `## Sources`, `## Source Coverage`, `## Search Craft Log`, `## Wave Log`, `## Lead Ledger`, `## Expansion Frontier Audit`, rejection reasons |
| G3 Evidence Table Before Narrative | complete Claim Ledger and Evidence sections before writing persuasive synthesis | Claim Ledger, source-to-claim mapping, confidence labels |
| G4 Independent QA / Red Team | attack claim support, source quality, currentness, lineage, sensitivity, and overreach | verification lanes and red-team findings |
| G5 Delivery Acceptance | verify final deliverable answers the decision and meets quality thresholds | scorecard, acceptance gates, final label |
| G6 Post-Delivery Control | support correction, revalidation, and source-update handling | audit/change log, expiry/revalidation triggers, errata notes |

## RACI And Escalation

Use a lightweight role model:

| Role | Responsibility |
|---|---|
| Main agent / lead analyst | framing, lane design, source integration, Claim Ledger, synthesis, final label |
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
| Frontier queue convergence | 0-4 | unresolved material leads, latest EXPAND/gap cycle, closed/blocked lead reasons, confidence effects | ... |
| Search bias and retrieval traps | search or connector discovery | ranking bias, SEO/sponsored pages, snippets/AI overviews, duplicate lineages, language/locality mismatch, query bias, personalization, paywalls, corpus gaps, stale indexes, and platform filters are diagnosed, mitigated, bounded, or tied to confidence |
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
| Question coverage | always | every user-requested part, comparison axis, deliverable requirement, and explicit constraint is answered, bounded, blocked, or carried into open questions |
| Entity and terminology | ambiguous entities or terms | targets, aliases, acronyms, translations, versions, jurisdictions, and false positives are resolved or bounded before evidence use |
| Claim traceability | always | every important claim maps to source IDs and evidence locations |
| Inference boundary | always | synthesized claims separate direct observation from bounded inference, assumptions, transferability limits, and unsupported overreach |
| Assumption sensitivity | decision-relevant or assumption-dependent claims | thresholds, baselines, comparators, scenarios, scope, jurisdiction, timeframe, denominator, method choice, risk tolerance, and constraints are tested or bounded |
| Conflict resolution | any material contradiction | conflicting evidence is adjudicated, bounded, split by context, left unresolved, or marked insufficient with confidence effects |
| Source-body inspection | always | every used source was inspected/retrieved; snippets and AI summaries are leads only |
| Source incentive and bias | decision-relevant or claim-supporting sources | funding, affiliations, vendor/advocacy stakes, self-reporting, sponsorship, publication incentives, disclosure, and corroboration needs are recorded |
| Source manipulation and adversarial provenance | adversarial, identity-dependent, user-generated, repo/package, media, dataset, review, forum, public comment, PDF, screenshot, or agent-facing sources | fabrication, impersonation, coordination, amplification, review manipulation, synthetic media, tampering, poisoned artifacts, active content, and prompt-injection risks are checked safely and reflected in confidence |
| Source-family coverage | always | required primary, data/method, secondary/context, and counterevidence families are checked or justified unavailable |
| Corroboration and triangulation | every important claim | primary/governing support or source-of-truth exception, independent corroboration, counterevidence, method/data checks, lineage diversity, status, and confidence effect are recorded |
| Selection and inclusion | every important evidence set | inclusion criteria, exclusion criteria, downranked results, selection risks, and mitigation are recorded |
| Quotation/context integrity | quote-like or context-sensitive evidence | attribution, exact location, surrounding context, translation/paraphrase risk, claim fit, status, and confidence effect are recorded |
| Search reproducibility | always | Search Craft Log and Wave Log include scout, target, snowball, EXPAND, counter-search, and gap-pass paths with dates/filters/source systems |
| Saturation Metrics | always | query diversity, inspected-source floor, expansion waves, counter-search passes, local-language or jurisdictional sweeps, and material lead closure are recorded with confidence effects |
| Expansion frontier | always | strong seeds and inspected sources generate explicit query or connector passes for citations, authors, datasets, methods, aliases, local terms, successors, corrections, repositories, issues, dockets, standards, reviews, complaints, and counterclaims |
| Frontier queue convergence | always | the latest EXPAND or gap cycle produced no new high-value leads, or every remaining material lead is closed, blocked with confidence effect, duplicate lineage, out of scope, low quality, or unable to change an important claim |
| Synthesis traceability | always | final answer paragraphs, key findings, recommendations, comparison rows, and caveats map to claim IDs, evidence/source links, confidence, unresolved debt, status, and required revision |
| Absence evidence | any `not found`, non-existence, no-current-support, or no-public-record claim | searched boundaries, expected source families, retrieval limits, and permitted inference are recorded before absence supports synthesis |
| Provenance and lineage | always | source lineage, original/mirror/archive/excerpt role, and duplicate lineages are recorded |
| Currentness | current-dependent claims | latest-update/supersession/as-of checks are recorded |
| Reproducibility and refresh | mutable, current-dependent, versioned, or decision-relevant sources | rerun path, stable locator/version, volatility trigger, last-checked date, and refresh action are recorded |
| Method appraisal | data, statistics, surveys, science, benchmarks, forecasts | denominator, definitions, sample/method, uncertainty, and comparability are checked |
| Quantitative measurement | any important number, metric, benchmark, price, ranking, forecast, or market estimate | unit, denominator, scope, period/vintage, method, uncertainty, revision status, and comparability are recorded |
| Conflict handling | any conflict or plausible alternative | contradictions are resolved, bounded, or carried as explicit uncertainty |
| Sensitivity and authorization | internal/sensitive sources | access basis, sensitivity, minimum necessary use, and redistribution limits are recorded |
| Independent review | professional-grade claim | fresh verification or red-team lane has passed |
| Decision readiness | enterprise action | decision-use status is `usable` or `usable with caveats`; owner review needs are explicit |
| Evidence maturity dashboard | final synthesis | central claims, comparisons, recommendations, decisions, and source-family conclusions are summarized by maturity, weakest gate, debt, and decision/synthesis effect before firm prose |

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
- Did the record include `## Sources`, `## Source Coverage`, `## Search Matrix`,
  `## Search Craft Log`, `## Wave Log`, `## Lead Ledger`, `## Claim Ledger`,
  verification lanes, and scorecard?
- Did Source Lineage Mapping prevent duplicate-lineage summaries, mirrors,
  translations, syndicated articles, and repeated datasets from being counted
  as independent evidence?
- Did the record prove harness max-use through resolved tool capabilities,
  diversified batch execution with numeric sub-batches, query diversity,
  opened-source coverage, recursive frontier reuse, and closure or downgrading
  of material leads?
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
- claiming convergence while high-value frontier queue items remain open
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

## Decision Usefulness

Professional research should make its decision relevance explicit. When the
request informs a choice, recommendation, diligence, purchase, strategy, or next
action, record options, criteria, evidence links, tradeoffs, residual risks, and
what would change the decision. If the request is not decision-oriented, mark
that explicitly instead of inventing a recommendation.

## Comparison And Evaluation Audit

Professional research must not compare options on shifting or hidden criteria.
For every material comparison, recommendation, ranking, vendor/product choice,
policy/legal option, market scan, theory comparison, investment diligence, or
security diligence choice, record the options/entities, criteria or axes, weights
or priorities, evidence links, missing or non-comparable data, tradeoffs,
sensitivity conditions, status, and decision effect.

A professional record should not say one option is better, preferred, best,
cheaper, safer, stronger, weaker, or recommended unless the comparison row is
comparable or the limitation is explicit. If evidence is asymmetric, stale,
non-comparable, sponsored, or missing for one side, mark the row partially
comparable, non-comparable, biased, or blocked and reflect that status in the
final synthesis.

## Question Coverage Audit

Professional research must show that it answered the user's actual request, not
only an adjacent topic discovered during source search. The record should map
each subquestion, comparison axis, deliverable requirement, and explicit
constraint to evidence links, residual gaps, and the final-answer location.
Unanswered rows require a visible caveat, open question, or confidence impact.

## Entity And Terminology Audit

Professional research must disambiguate targets before evidence collection
hardens. For ambiguous names, acronyms, translations, native-script variants,
product/version labels, repositories, laws, standards, datasets, markets,
policies, or overloaded concepts, record the included identifiers, excluded
lookalikes, verification sources, and confidence effect.

If disambiguation is unresolved, bound the answer to the searched target or
lower confidence. Do not merge lookalike entities or adjacent concepts for
convenience.

## Tool Capability Audit

Professional research should show which available capabilities were used or why
they were unavailable, blocked, or not applicable: web search, source
open/fetch, in-source extraction, connectors or databases, local file/code
search, repository/package access, archives/browser fallback, document/PDF/table
extraction, and subagents or parallel lanes. Skipping a stronger available
capability creates coverage debt unless it cannot affect the claim.

## Access And Retrieval

Professional research must distinguish discovered sources from retrieved
sources. Important sources should be opened, fetched, or retrieved before they
support a claim. If primary access fails, the record should show authorized
alternate attempts such as archives, PDFs, APIs, browser access, official
mirrors, repositories, package registries, cached copies, or cited excerpts.
Blocked important sources lower confidence unless another strong inspected
source resolves the same claim.

## Search Bias And Retrieval Trap Audit

Professional research must treat search results as an instrument with known
failure modes. For important lanes and source families, record whether ranking
bias, SEO or sponsored placement, snippets or AI overviews, duplicate lineages,
language/locality mismatch, query wording, personalization, paywalls, corpus
coverage, stale indexes, missing archives, review manipulation, or platform
filters could distort discovery.

A professional record should show the diagnostic check and mitigation: official
or domain-limited search, filetype search, exact title search, local-language
terms, archive lookup, database/direct-site search, repository/package registry
search, cited-source snowballing, counter-search, or inspection beyond top-ranked
results. Unmitigated traps should downgrade or bound affected claims.

## Selection And Inclusion Audit

Professional research must show why its evidence set is not cherry-picked. For
important source families, literature sets, market sets, product comparisons,
review/forum sets, repositories, datasets, and counterevidence sets, record
inclusion criteria, exclusion or downrank criteria, included sources, excluded
or downranked results, selection risk, mitigation, and confidence effect.

Convenience-selected, paywall-limited, language-limited, ranking-biased, or
survivorship-biased evidence sets require a visible caveat, follow-up pass, or
confidence downgrade.

## Saturation Metrics

Professional research must make search pressure visible, not merely implied by
the final narrative. The record should state actual counts or closure status
for distinct query formulations, inspected relevant sources or records,
EXPAND/lead-expansion waves, counter-search passes, local-language or
jurisdictional sweeps when applicable, material high-value lead closure, and
frontier queue convergence.

Missed or blocked metrics require a recorded reason, coverage debt or follow-up
pass, and confidence impact. A professional-grade label is not appropriate when
important search-pressure gaps remain unexplained.

## Expansion Frontier Audit

Professional research must show how discovery expands from strong seeds. For
each important seed, inspected source, result, lead, citation chain, author,
institution, dataset, method, alias, local term, successor, correction,
repository, issue, docket, standard, review, complaint, or counterclaim, record
the extracted frontier, lead type, query or connector pass, status, outcome,
and confidence effect.

This prevents shallow breadth: a record cannot claim saturation merely because
it ran many independent searches if the best sources contained unresolved
frontiers that could change the answer.

## Frontier Queue Convergence

Professional research must show that lead expansion actually converged. The
record should use the Lead Ledger, Expansion Frontier Audit, Saturation Metrics,
Coverage Debt, and Stop Rule Audit to show whether the latest EXPAND or gap
cycle produced new high-value leads. Any remaining material lead must be closed
as duplicate lineage, blocked with confidence effect, out of scope, low quality,
unable to change important claims, or downgraded in the affected claim.

A professional-grade label is not appropriate when important frontier items
remain open without a follow-up pass, closure reason, blockage note, or
confidence effect.

## Absence Evidence

Professional research must not turn search failure into an unbounded
non-existence claim. When the conclusion depends on no evidence being found,
the record should show the search boundary, expected authoritative source
families, languages or jurisdictions, repositories/databases/archives checked,
retrieval limits, and the exact inference allowed.

If the expected source family was not searched or was blocked, say "not found
in the searched sources" rather than "does not exist", and lower confidence
unless the missing family cannot affect the decision.

## Currentness And Version Audit

Professional research must separate event date, publication date, accessed date,
effective date, valid-at date, release tag, product/model version, jurisdiction,
and supersession status when these can affect a claim. Current-dependent claims
that cannot be latest-checked should be downgraded or marked `insufficient`.

## Reproducibility And Refresh Audit

Professional research should be refreshable. For mutable, current-dependent,
versioned, or decision-relevant sources and claims, record the rerun path,
stable locator or version, volatility trigger, last-checked date, and refresh
action. Examples include archive URLs, release tags, commits, package versions,
dataset vintages, docket IDs, report editions, API endpoints, and exact query
families.

If a source is volatile and cannot be reproduced or refreshed through an
authorized path, bound the claim to the checked date or lower confidence.

## Quantitative And Measurement Audit

Professional research must make numbers auditable. For each important
statistic, ranking, benchmark, price, market-size estimate, survey result,
forecast, KPI, score, or measured comparison, record unit, denominator,
population/scope, geography, period or vintage, method/source, uncertainty,
revision status, and comparability limits.

Do not compare numbers across sources, periods, populations, currencies,
benchmark setups, or methods unless the comparability limit is recorded. Missing
denominators, opaque methods, stale vintage, or proxy metrics lower confidence
or make the claim `insufficient`.

## Consensus And Disagreement Audit

Professional research must distinguish consensus from repeated citation,
search-result prominence, stakeholder messaging, or a loud minority. For central
questions and important claims, record the relevant source community or field,
consensus signal, disagreement or minority view, evidence links, recency and
scope limits, status, and confidence effect.

A professional record should not call something consensus, mainstream, widely
accepted, best practice, standard, generally preferred, or settled unless the
record shows the source community and the evidence basis for that label. If the
field is split, the evidence base is thin, or the dissent is decision-relevant,
mark the row mixed, contested, fringe, unclear, or blocked and narrow the final
claim.

## Source Incentive And Bias Audit

Professional research must distinguish source authority from source incentives.
For decision-relevant or claim-supporting sources, record funding,
affiliation, vendor interest, advocacy position, regulatory or political stake,
self-reporting, sponsorship or affiliate relationship, publication incentive,
disclosure status, mitigation, corroboration, and confidence effect.

Do not discard a source merely because it has incentives, but do not let
interested sources carry strong claims without independent corroboration or a
clear caveat. Vendor claims, advocacy claims, commissioned reports, sponsored
content, and self-reported metrics should normally be corroborated by primary
records, independent lineages, or method/data checks.

## Source Manipulation And Adversarial Provenance Audit

Professional research must distinguish ordinary bias from active manipulation or
adversarial provenance risk. For important sources that could be fabricated,
coordinated, impersonated, poisoned, tampered with, or unsafe, record the source
or claim, risk type, authenticity/provenance check, coordination/amplification
check, safety/injection check, evidence links, status, and confidence effect.

This is especially important for user-generated content, reviews, social posts,
forums, public comments, repositories, packages, scripts, datasets, PDFs,
screenshots, media, identity claims, and AI/agent-facing pages. Use passive,
authorized checks and do not execute untrusted artifacts without explicit
approval. If provenance remains unresolved and material, downgrade, exclude, or
mark the affected claim insufficient.

## Corroboration And Triangulation Audit

Professional research should prove claim strength claim-by-claim. For every
important claim, record whether there is primary or governing support,
independent corroboration from separate lineages, strongest counterevidence or
limitations, method/data verification where relevant, lineage diversity, status,
and confidence effect.

High-risk, current, comparative, causal, quantitative, legal, financial,
security, safety, or decision-relevant claims should not be high confidence when
they are single-source, contradicted, or blocked unless the record explains a
source-of-truth exception and why the unresolved dimension cannot change the
claim.

## Quotation And Context Audit

Professional research treats direct quotes, translated quotes, paraphrased
source positions, headlines, excerpts, screenshots, social posts, interviews,
legal/policy passages, and paper conclusions as context-sensitive evidence.
Record attribution, precise location, surrounding context, translation or
paraphrase risk, claim fit, status, and confidence effect before using such
passages as support.

Downgrade or mark the affected claim insufficient when the passage is narrower
than the synthesized claim, the original context is missing, attribution is
unclear, translation risk is material, or only a snippet/summary was inspected.

## Evidence Location Audit

Professional research must point to the precise evidence location inside used
sources whenever possible: page, section, table, line, timestamp, field, release
tag, issue ID, docket entry, appendix, or equivalent locator. URL-only support
is weak for important claims and should lower confidence unless the source is
short, atomic, and fully inspected.

## Language And Locale Audit

Professional research must not rely on English-only discovery for local,
translated, identity, policy, legal, market, cultural, or non-English topics
unless the record explains why local-language source families cannot change the
answer. Native terms, aliases, scripts, local institutions, local official
sources, registries, archives, media, and forums should be considered where
relevant.

## Claim Risk Triage

Professional research must not spend equal verification effort on all claims.
Triage important claims by decision impact and error risk before synthesis.
High-priority claims require primary or governing sources where applicable,
counter-search, currentness, lineage, source quality, method/data, and
adversarial checks before firm conclusions.

## Distortion Pattern Audit

Professional research should explicitly test repeated, translated, summarized,
second-hand, synthetic, or other-AI-provided claims for stale evidence,
misattribution, conflation, circular citation, inference upgraded to fact,
magnitude drift, quote distortion, translation drift, cherry-picking, and
survivorship bias. Material unresolved distortion lowers confidence or blocks
firm synthesis.

## Evidence Maturity Dashboard

Professional research should expose readiness at a glance before synthesis. The
record should summarize central claims, comparisons, recommendations, decisions,
and source-family conclusions by maturity status, linked claims/questions,
required gate cluster, weakest link or blocking debt, and decision/synthesis
effect.

A professional record should not present a firm conclusion when the dashboard
marks the relevant item immature or blocked. Those items should be downgraded,
caveated, moved to open questions, or marked insufficient.

## Confidence Calibration

Professional research must show why each important claim receives its final
confidence label. Calibrate confidence against evidence strength, consistency,
directness, currentness, source-lineage independence, method/data quality,
counterevidence, coverage debt, and synthesis-overreach risk. Do not use source
count alone as a confidence proxy.

Claims with unresolved currentness, unclear lineage, opaque methods, material
counterevidence, or unclosed coverage debt cannot receive `high` confidence
unless the record explains why the unresolved dimension cannot affect the
claim.

## Synthesis Traceability Audit

Professional research must audit the final prose, not only the underlying
claims. Each answer paragraph, key finding, recommendation, decision/action,
comparison row, caveat, and material summary sentence should map to claim IDs,
source or observation links, confidence, unresolved limits or debt, status, and
required revision.

If a polished sentence cannot be traced, it must be revised, caveated, moved to
uncertainty/open questions, or removed. Professional-grade delivery is not
appropriate when the final narrative contains unsupported synthesis.

## Inference Boundary Audit

Professional research must make the jump from evidence to synthesis visible.
For each important synthesized claim, distinguish direct observation from
bounded inference, comparison, extrapolation, causal interpretation, forecast,
recommendation, or speculative step. Record the assumptions required,
transferability limits, what the evidence does not support, and the confidence
effect.

If the inference boundary is speculative or overreaches inspected evidence,
rewrite the claim, downgrade it, or mark it `insufficient` before final
synthesis.

## Assumption And Sensitivity Audit

Professional research should identify which assumptions can change the answer.
For every decision-relevant or assumption-dependent claim, record the
assumption or variable, plausible range or alternative, evidence or test,
sensitivity, status, and confidence effect.

When a reasonable alternative would change the conclusion, the record should
present bounded scenarios or caveats rather than a single firm answer. Untested
or blocked decision-changing assumptions lower confidence or block a
decision-ready label.

## Conflict Resolution Matrix

Professional research must make contradictions explicit. When sources,
observations, methods, dates, jurisdictions, versions, lineages, or
interpretations disagree, record the conflict, evidence on each side,
adjudication basis, resolution, and confidence effect.

Do not resolve conflicts by source count alone. Prefer direct, authoritative,
current, methodologically stronger, and independent-lineage evidence where
appropriate; otherwise bound the claim, split it by context, keep the conflict
visible, or mark the affected claim `insufficient`.

## Adversarial Review

Professional research must challenge its own provisional synthesis before final
labeling. The record should show the strongest counterclaim, missing
source-family risk, incentive or bias concern, method weakness, currentness gap,
transferability limit, and synthesis-overreach concern, or explain why a
challenge is not applicable. Material unresolved challenges lower the final
label or confidence.

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
