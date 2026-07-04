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

Do not create a topic folder, `brief.md`, `sources.md`, `notes.md`, claim graph
files, source ledgers, screenshot folders, or per-agent artifacts. Every search
lane, source table, observation manifest, claim ledger, evidence decision,
verification note, and final synthesis belongs in this one Markdown file.

## Principle

The record exists to preserve the evidence trail and final synthesis in one
auditable place. It should show the question, answer, search matrix, search
waves, source support, counterevidence, uncertainty, verification work,
coverage gates, and stop-rule reasoning without scattering artifacts across the
workspace.

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

## Evidence Maturity Dashboard

Summarize whether the evidence record is mature enough for each central claim,
comparison, recommendation, or decision. This dashboard does not replace the
detailed audit sections; it points to the weakest gates before final synthesis.

| Maturity ID | Item | Type | Linked Claims / Questions | Required Gate Cluster | Current Maturity | Blocking Debt / Weakest Link | Decision / Synthesis Effect |
|---|---|---|---|---|---|---|---|
| EM1 | central answer / recommendation / comparison / claim / not applicable | final answer / decision / comparison / claim / source family / not applicable | C1 / Q1 / EV1 / ST1 | search, source, verification, synthesis, decision | mature / caveated / immature / blocked / not applicable | D1 / failed gate / unresolved source family / none | ready / caveat / downgrade / no firm conclusion |

## Decision Usefulness Matrix

State how the research supports a decision, recommendation, comparison, or next
action. If the request is not decision-oriented, mark it `not applicable` and
say why.

| Decision / Use Case | Options / Actions | Criteria | Evidence Link | Risks / Tradeoffs | What Would Change This | Status |
|---|---|---|---|---|---|---|
| user decision or not applicable | option A / option B / no action / not applicable | cost, quality, risk, fit, feasibility, confidence | C1 / O1 / S1 / A1 | unresolved gaps, tradeoffs, uncertainty | new source, changed currentness, resolved debt | actionable / caveated / not decision-ready / not applicable |

## Comparison And Evaluation Audit

Use this for comparisons, recommendations, rankings, vendor/product choices,
market scans, policy/legal options, academic theory comparisons, investment or
security diligence, and any answer that says better, worse, best, prefer,
choose, or recommend.

| Evaluation ID | Options / Entities | Criteria / Axes | Weight / Priority | Evidence Links | Missing / Non-Comparable Data | Tradeoffs / Sensitivity | Status | Decision Effect |
|---|---|---|---|---|---|---|---|---|
| EV1 | option A / option B / not applicable | cost, quality, risk, fit, feasibility, evidence strength, currentness, method, decision criteria | high / medium / low / equal / not applicable | C1 / S1 / O1 / D1 | none / D1 / non-comparable metric / missing source family / not applicable | AS1 / caveat / scenario / none | comparable / partially comparable / non-comparable / biased / blocked / not applicable | supports recommendation / caveat / downgrade / no recommendation |

## Question Coverage Audit

Map the user's request to answer coverage so no subquestion, comparison axis,
constraint, or deliverable requirement silently disappears.

| Question ID | User Need / Subquestion | Answer Status | Evidence / Claim Links | Residual Gap | Final Answer Location |
|---|---|---|---|---|---|
| Q1 | requested question part, comparison axis, constraint, or deliverable requirement | answered / partially answered / unanswered / blocked / out of scope / not applicable | C1 / O1 / S1 / D1 | none / unresolved evidence / blocked source / scope exclusion | Answer / Key Findings / Open Questions |

Before final validation, resolve every `unanswered` question row to `answered`,
`partially answered`, `blocked`, `out of scope`, or `not applicable`, with
residual gap and final-answer location.
Unanswered rows do not pass final validation.

## Tool Capability Audit

Record which harness capabilities were used, blocked, unavailable, or not
applicable. This proves the research used the available search and retrieval
surface rather than relying on one path.

| Capability | Status | Use / Reason | Limits / Fallback | Record Impact |
|---|---|---|---|---|
| web search | planned / used / blocked / unavailable / not applicable | queries, domains, or why not used | limits, rate limits, auth, fallback | sections affected |
| batch / parallel diversified search | planned / used / blocked / unavailable / not applicable | batch size, batch count, lane count, or why not used | tool limit, sequential fallback, rate/auth limits | diversified batch plan / saturation metrics |
| source open / fetch | planned / used / blocked / unavailable / not applicable | pages, PDFs, records, or why not used | blocked sources and alternates | sources / retrieval audit |
| in-source find / extraction | planned / used / blocked / unavailable / not applicable | terms, tables, methods, dates | extraction limits | observations |
| connectors / databases | planned / used / blocked / unavailable / not applicable | connector/database names or why not relevant | auth/access limits | coverage debt |
| local files / code search | planned / used / blocked / unavailable / not applicable | paths, repos, code, docs | sandbox/access limits | evidence / dead ends |
| repository / package access | planned / used / blocked / unavailable / not applicable | GitHub, package registries, releases, issues | auth/rate limits | OSS evidence |
| archive / browser fallback | planned / used / blocked / unavailable / not applicable | archives, browser, cached pages | access limits | retrieval confidence |
| source retrieval fallback | planned / used / blocked / unavailable / not applicable | alternates tried for blocked source-of-truth material | archives, mirrors, APIs, PDFs, cited excerpts, browser | access and retrieval audit / coverage debt |
| document/PDF/table extraction | planned / used / blocked / unavailable / not applicable | PDFs, docs, tables, appendices | extraction limits | method/data evidence |
| subagents / parallel lanes | planned / used / blocked / unavailable / not applicable | lanes, workers, or sequential fallback | availability limits | worker wave plan |

Before final validation, resolve every `planned` capability row to `used`,
`blocked`, `unavailable`, or `not applicable` with a fallback and record impact.

## Search Matrix

| Lane | Claim / Subquestion | Evidence Need | Source Families | Query / Path Patterns | Counter-Search | Final Status |
|---|---|---|---|---|---|---|
| L1 | ... | authoritative-record / empirical-data / etc. | official docs, datasets, papers, etc. | exact phrases, aliases, native terms, domains, file types | rebuttal, correction, failed replication, supersession | complete / blocked / superseded / not applicable |

## Diversified Search Batch Plan

Use this when the active search harness supports batched queries. Each batch
should mix source families rather than spend capacity on near-duplicate keyword
variants. Use at least three batches unless the harness blocks batch search;
the set must cover official/source-of-truth, currentness, counterevidence,
frontier-expansion, and blocked-source-recovery paths. When seeded with
`query_matrix.py --format batches --batch-size <tool-limit>`, preserve the
generated query counts, `SB1` / `SB2` execution sub-batches, and tool-limit notes
inside the Purpose column. Replace `tool-limit` with the actual active search
tool limit before final validation.

| Batch | Source Families To Mix | Purpose | Record Integration |
|---|---|---|---|
| B1 | scout / official-primary / pdf-document / dataset-method | execute source-of-truth discovery queries as sub-batches of up to tool-limit; SB1: scout and official-primary; SB2: pdf-document and dataset-method | Search Craft Log / Search Result Triage / Saturation Metrics |
| B2 | currentness / counterevidence / source-lineage / provenance-archive | execute freshness, contradiction, and upstream-origin queries as sub-batches of up to tool-limit; SB1: currentness and counterevidence; SB2: source-lineage and provenance-archive | Currentness And Version Audit / Source Lineage Map / Absence Evidence Audit |
| B3 | frontier-expansion / blocked-source-recovery / scholarly / github-oss / implementation-code | execute lead-expansion and blocked-source-recovery queries as sub-batches of up to tool-limit; SB1: frontier-expansion and blocked-source-recovery; SB2: scholarly, github-oss, and implementation-code | Lead Ledger / Expansion Frontier Audit / Access And Retrieval Audit / Coverage Debt |

## Domain Coverage Matrix

Map the research question against broad domain protocols. This is not a
research route chooser; it prevents missing source families when a request
crosses domains.

| Domain / Protocol | Applicability | Required Source Families | Status | Notes / Exclusions |
|---|---|---|---|---|
| official / primary | applicable / not applicable / uncertain | governing records, official docs, filings, standards, releases | planned / searched / covered / blocked / not applicable | ... |
| currentness / latest state | applicable / not applicable / uncertain | changelogs, advisories, dockets, status pages, latest official updates | planned / searched / covered / blocked / not applicable | ... |
| scholarly / academic | applicable / not applicable / uncertain | full text, methods, literature reviews, replication, citations | planned / searched / covered / blocked / not applicable | ... |
| data / statistics / methods | applicable / not applicable / uncertain | datasets, methodology notes, codebooks, uncertainty, denominators | planned / searched / covered / blocked / not applicable | ... |
| legal / regulatory / policy | applicable / not applicable / uncertain | laws, regulations, guidance, enforcement, comments, effective dates | planned / searched / covered / blocked / not applicable | ... |
| market / competitive / product | applicable / not applicable / uncertain | competitors, pricing, adoption, reviews, procurement, availability | planned / searched / covered / blocked / not applicable | ... |
| technical / OSS / implementation | applicable / not applicable / uncertain | docs, source code, issues, releases, package registries, advisories | planned / searched / covered / blocked / not applicable | ... |
| security / safety / risk | applicable / not applicable / uncertain | advisories, incidents, CVEs, mitigations, risk disclosures | planned / searched / covered / blocked / not applicable | ... |
| provenance / identity / archives | applicable / not applicable / uncertain | original sources, archives, registries, profiles, citations, lineage | planned / searched / covered / blocked / not applicable | ... |
| public sentiment / behavior | applicable / not applicable / uncertain | forums, reviews, support threads, complaints, observed behavior | planned / searched / covered / blocked / not applicable | ... |

Before final validation, resolve every `planned` domain row to `searched`,
`covered`, `blocked`, or `not applicable` with notes and confidence impact.

## Language And Locale Audit

Record language, jurisdiction, and local-source coverage. English-only search is
not enough for local, translated, identity, policy, legal, market, cultural, or
non-English topics unless the audit explains why.

| Locale / Language | Applicability | Native Terms / Aliases | Local Source Families | Status | Confidence Impact |
|---|---|---|---|---|---|
| global / English / local language | applicable / not applicable / uncertain | terms, spellings, scripts, translations | local official, local media, registries, databases, forums, archives | planned / searched / covered / blocked / not applicable | none / downgraded / insufficient |

Before final validation, resolve every `planned` language/locale row to
`searched`, `covered`, `blocked`, or `not applicable` with confidence impact.

## Entity And Terminology Audit

Disambiguate the target before treating search results as evidence. Use this
for people, organizations, products, repositories, laws, standards, datasets,
markets, policies, concepts, aliases, acronyms, translations, versions, and
false positives.

| Entity / Term | Ambiguity Risk | Included Identifiers / Aliases | Exclusion Terms / Lookalikes | Verification Sources | Status | Confidence Effect |
|---|---|---|---|---|---|---|
| target entity or term | name collision / acronym / translation / version / jurisdiction / concept drift / false positive / none | official name, IDs, versions, native terms, repo/package names | entities, meanings, versions, or jurisdictions to exclude | S1 / official registry / source family | resolved / bounded / ambiguous / blocked / not applicable | none / downgrade / insufficient |

## Worker Wave Plan

Record how the investigation will apply search pressure. If subagents are not
available, keep the same plan and mark execution as sequential fallback.

| Wave | Purpose | Lanes / Passes | Execution | Completion Criteria |
|---|---|---|---|---|
| W0 | framing and query matrix | ... | main agent | search matrix, evidence needs, source families, stop gates set |
| W1 | scout | ... | parallel / sequential fallback | vocabulary, aliases, source families, false positives identified |
| W2 | target and snowball | ... | parallel / sequential fallback | strong seeds inspected and leads extracted |
| W3 | EXPAND, counter-search, currentness, provenance, gap pass | ... | parallel / sequential fallback | high-value leads followed or closed |
| W4 | verification and synthesis-overreach | ... | parallel / sequential fallback | claims, sources, lineage, gaps, and synthesis audited |

## Search Craft Log

Record query diversity and integration notes. Do not count raw search volume as
coverage unless the result was integrated into the investigation.

| Lane | Cycle | Query / Path | Operator / Angle | Source Family | Integrated Finding | Next Lead / Gap |
|---|---|---|---|---|---|---|
| L1 | landscape / targeted gap | ... | site / filetype / exact / local-language / counter-search | official / dataset / academic / archive / OSS / etc. | confirmed / contradicted / refined / dead end | ... |

## Search Result Triage

Classify meaningful search results before synthesis. This prevents snippets,
duplicate lineage, and unopened leads from silently becoming evidence.

| Result ID | Lane / Query | Result / URL / Path | Classification | Reason | Follow-Up |
|---|---|---|---|---|---|
| R1 | L1 / query text | ... | open-now / lead / duplicate-lineage / context-only / dead-end | why classified this way | opened as S1 / added LD1 / ignored with reason |

## Search Bias And Retrieval Trap Audit

Use this to audit whether the search system, platform ranking, query wording,
corpus coverage, snippet display, sponsored/SEO content, duplicate-lineage
results, language choice, personalization, paywalls, or unavailable databases may
have distorted discovery before evidence selection.

| Trap ID | Lane / Query / Source Family | Potential Trap | Diagnostic Check | Mitigation / Alternate Path | Evidence / Follow-Up Links | Status | Confidence Effect |
|---|---|---|---|---|---|---|---|
| SB1 | L1 / query / source family | SEO/ranking/snippet/AI-overview/sponsored/duplicate-lineage/language/personalization/paywall/corpus gap | compare official/primary/local/counter-search/domain-limited/results beyond top ranks | site/filetype/exact/local-language/archive/database/direct-domain/counter-search | R1 / S1 / LD1 / D1 | bias-mitigated / bounded / trap-found / blocked / not applicable | none / downgrade / insufficient |

## Selection And Inclusion Audit

Audit why the selected evidence set is adequate rather than cherry-picked,
convenience-sampled, or source-family biased.

| Evidence Set | Inclusion Criteria | Exclusion / Downrank Criteria | Included Sources | Excluded / Downranked Results | Selection Risk | Mitigation | Status | Confidence Effect |
|---|---|---|---|---|---|---|---|---|
| official / dataset / academic / market / review / repository / counterevidence set | criteria for inclusion | low quality, duplicate lineage, wrong target, stale, inaccessible, irrelevant, weak method | S1 / S2 | R1 / LD1 / source family | cherry-pick / survivorship / convenience / language / paywall / ranking / none | counter-search, source-family balance, random/transparent cut, independent lineage, caveat | balanced / bounded / biased / incomplete / blocked / not applicable | none / downgrade / insufficient |

## Access And Retrieval Audit

For important sources, record whether the source body or retrieved record was
actually accessed. If access fails, try authorized alternate paths before using
the source as evidence or downgrading the affected claim.

| Retrieval ID | Target Source / Lead | Primary Access Path | Alternate Paths Tried | Retrieval Status | Evidence Use | Confidence Impact |
|---|---|---|---|---|---|---|
| AR1 | S1 / LD1 / official report | direct URL / connector / repository / database | archive, PDF, API, browser, mirror, package, cached copy, cited excerpt | retrieved / alternate retrieved / blocked / not applicable | used / lead only / excluded | none / downgraded C1 / insufficient |

## Prior Record Check

Use this only when older local research records exist.

| Prior Record | Relevance | Sections Loaded | Claims Reused | Refresh Result |
|---|---|---|---|---|
| 001-topic.md | strong / partial / weak | summary / sources / claim ledger / etc. | C1, S1, or none | refreshed / superseded / contradicted / not used |

## Wave Log

Record scout, target, snowball, EXPAND, counter-search, and gap-pass work at the
level needed to reconstruct the investigation.

| Wave | Lane | Pass | Query / Source Path | Result | Leads Raised | Decision |
|---|---|---|---|---|---|---|
| W1 | L1 | scout | ... | ... | ... | follow / duplicate / dead end / blocked / low quality |

## Lead Ledger

Track every high-value lead raised by searches, inspected sources, subagents, or
verification. Use this as the active frontier queue: a lead may be closed only
with a reason, and synthesis should not proceed while material open leads remain
unless they are blocked or tied to confidence downgrades.

| Lead ID | Raised From | Lead | Why It Matters | Action | Outcome |
|---|---|---|---|---|---|
| LD1 | W1 / S1 / L2 | ... | could change C1 / close source-family gap | followed / duplicate / blocked / low quality / out of scope | source found / no result / claim downgraded / unresolved |

Before final validation, every material lead must have a closed action:
`followed`, `duplicate`, `blocked`, `low-quality`, `out-of-scope`, or
`not applicable`. Do not leave final lead outcomes as `unresolved`; either close
the lead, block it with reason, or tie it to a confidence downgrade.

## Source-Opened Follow-Up Audit

Every high-value opened source must either produce follow-up search pressure or
record why it produced no material leads. This prevents source opening from
becoming a terminal citation step.

| Follow-Up ID | Source / Observation | Extracted Lead | Lead Type | Follow-Up Search / Connector Path | Action | Outcome / Confidence Effect |
|---|---|---|---|---|---|---|
| SOF1 | S1 / O1 | citation, author, dataset, identifier, native term, correction, counterclaim, blocked source, or none | citation / author / dataset / identifier / native term / correction / counterclaim / blocked source / none | query, connector path, archive path, repository path, or not applicable | followed / closed / blocked / duplicate-lineage / low quality / out of scope / no leads / not applicable | source found / no material lead / blocked / confidence downgraded / insufficient |

Final rows cannot remain `planned`, `open`, or `unresolved`; close them,
convert them into `## Lead Ledger` / `## Expansion Frontier Audit`, or reflect
them in confidence.

## Expansion Frontier Audit

Track the recursive frontier generated by strong seeds, inspected sources,
search results, citations, authors, datasets, methods, aliases, local terms,
successors, corrections, repositories, issues, dockets, standards, reviews,
complaints, and counterclaims.

| Frontier ID | Raised From | Seed / Source | Extracted Frontier | Lead Type | Query / Connector Pass | Status | Outcome / Confidence Effect |
|---|---|---|---|---|---|---|---|
| EF1 | W1 / S1 / R1 / LD1 | seed source, citation, author, dataset, method, entity, alias, docket, package, issue, review, counterclaim | citations / authors / datasets / aliases / methods / updates / corrections / successors / counterclaims / co-citations | source / entity / citation / dataset / method / currentness / counterevidence / local-language / archive / OSS / market / legal-policy / risk | query, connector path, snowball pass, EXPAND pass, archive path, repository path, database path, or blocked reason | planned / searched / followed / duplicate-lineage / low-quality / blocked / out-of-scope / not applicable | source found / no new lead / LD1 / D1 / confidence downgraded |

Before final validation, resolve every `planned` frontier row to `searched`,
`followed`, `duplicate-lineage`, `low-quality`, `blocked`, `out-of-scope`, or
`not applicable`, with outcome and confidence effect.

## Coverage Debt

Track gaps that could weaken saturation or change an important claim. A debt
item is cleared only by follow-up work, a recorded closure reason, blockage
with confidence impact, or a downgrade in the claim ledger.

| Debt ID | Raised From | Gap / Missing Coverage | Why It Matters | Follow-Up Owner / Pass | Status | Confidence Effect |
|---|---|---|---|---|---|---|
| D1 | L1 / LD1 / C1 / source audit | ... | could change C1 / source-family coverage / lineage | target / EXPAND / counter-search / verification | open / cleared / blocked / downgraded / not applicable | none / lowers C1 to medium / insufficient |

Before final validation, resolve every `open` coverage debt row to `cleared`,
`blocked`, `downgraded`, or `not applicable`. Open debt must either be cleared,
blocked with reason, tied to confidence downgrade, or shown irrelevant.

## Sources

| ID | Source | Type | Accessed / As Of | Why Used | Key Evidence | Limits |
|---|---|---|---|---|---|---|
| S1 | Title and URL/path | official / primary / dataset / expert / secondary / contextual | YYYY-MM-DD | why this source matters | section, page, table, line, timestamp, or field | limits, bias, stale risk, access limits |

## Source Coverage

Summarize source-count floors and diversity targets without treating count as
quality.

| Scope / Family | Target | Inspected | Notes |
|---|---:|---:|---|
| materially relevant sources or records | 12+ / 25+ / 50+ as appropriate | ... | scarcity, blocked access, duplicate lineages |
| official / primary / governing | as needed | ... | ... |
| empirical / method / data | when applicable | ... | ... |
| counterevidence / criticism / limitations | required for central claims | ... | ... |
| currentness / supersession | when applicable | ... | ... |
| OSS / implementation evidence | when applicable | ... | pinned SHA/tag/release when possible |
| scholarly full text / methods | when applicable | ... | no title/abstract-only support for method-sensitive claims |

## Saturation Metrics

Record search pressure explicitly. Metrics are coverage prompts, not evidence
quality substitutes. A missed metric requires a blockage note, follow-up pass,
or confidence downgrade before firm synthesis.

| Metric | Target / Floor | Actual | Status | Evidence / Record Link | Confidence Effect |
|---|---|---:|---|---|---|
| distinct search queries | 10+ per important web lane when web search exists | ... | met / not met / blocked / not applicable | Search Craft Log / Wave Log | none / downgrade / insufficient |
| inspected relevant sources or records | 12+ narrow, 25+ broad, 50+ very broad when sources exist | ... | met / not met / blocked / not applicable | Sources / Source Coverage | none / downgrade / insufficient |
| expansion waves | at least two broad EXPAND waves; three no-new-lead waves for convergence on very broad work | ... | met / not met / blocked / not applicable | Wave Log / Lead Ledger | none / downgrade / insufficient |
| frontier queue convergence | latest EXPAND or gap cycle produces no new high-value leads, or all remaining material leads are closed, blocked, duplicate-lineage, out of scope, low quality, or confidence-downgraded | ... | met / not met / blocked / not applicable | Lead Ledger / Expansion Frontier Audit / Coverage Debt | none / downgrade / insufficient |
| counter-search passes | every central claim gets negation, rebuttal, limitation, or supersession search | ... | met / not met / blocked / not applicable | Search Craft Log / Claim Ledger | none / downgrade / insufficient |
| local-language or jurisdictional sweeps | required when language, locale, policy, identity, market, or local facts matter | ... | met / not met / blocked / not applicable | Language And Locale Audit | none / downgrade / insufficient |
| material high-value leads closed | all material LD rows followed, closed, blocked, or tied to confidence downgrade | ... | met / not met / blocked / not applicable | Lead Ledger / Coverage Debt | none / downgrade / insufficient |

Before final validation, resolve every `not met` saturation metric to `met`,
`blocked`, or `not applicable`. A missed metric must be blocked with reason,
followed up, or tied to confidence downgrade before final synthesis.

## Source Lineage Map

Map upstream source lineages before treating sources as independent support.
Repeated summaries, mirrors, syndicated articles, excerpts, and reports based
on the same dataset or press release count as one lineage unless independent
evidence is shown.

| Lineage ID | Upstream Source / Origin | Member Sources | Independence Status | Claims Affected | Notes |
|---|---|---|---|---|---|
| G1 | original report / dataset / filing / statement / unknown | S1, S2 | original / independent / same-lineage / mirror / unclear | C1 | why sources do or do not count as independent |

## Source Quality Audit

Audit each used source before synthesis. Source count does not compensate for
weak authority, indirect evidence, stale currentness, opaque methods, or unclear
lineage.

| Source ID | Authority | Directness | Currentness | Method / Data Quality | Lineage | Overall Status | Confidence Effect |
|---|---|---|---|---|---|---|---|
| S1 | primary / expert / secondary / contextual / unknown | direct / partial / indirect | current / stale / unknown / not applicable | strong / adequate / weak / opaque / not applicable | original / independent / same-lineage / mirror / unclear | strong / usable / limited / weak / exclude | raises / supports / limits / downgrades / excludes C1 |

## Corroboration And Triangulation Audit

Use this to decide whether each important claim has the right mix of evidence,
not just many citations.

| Claim ID | Primary / Governing Support | Independent Corroboration | Counterevidence / Limitation | Method / Data Check | Lineage Diversity | Status | Confidence Effect |
|---|---|---|---|---|---|---|---|
| C1 | S1 / none / source-of-truth exception | G1 / G2 / none / not applicable | none found / O2 / D1 / not searched | verified / bounded / weak / opaque / not applicable | independent / same-lineage / unclear / single authoritative source | triangulated / partially corroborated / single-source / contradicted / blocked / not applicable | none / downgrade / insufficient |

## Consensus And Disagreement Audit

Use this for every central research question, important claim, recommendation,
market conclusion, policy/legal interpretation, scientific or academic claim,
technical/security claim, and other claim where field consensus or expert
disagreement affects how strongly the answer should be stated.

| Consensus ID | Claim / Question | Source Community / Field | Consensus Signal | Disagreement / Minority View | Evidence Links | Recency / Scope Limits | Status | Confidence Effect |
|---|---|---|---|---|---|---|---|---|
| CN1 | C1 / Q1 / not applicable | expert community, regulator, standards body, literature, market, maintainer group, affected users, or not applicable | guideline, review, meta-analysis, official position, repeated independent findings, market evidence, or not applicable | dissenting evidence, minority view, unresolved split, fringe claim, or none found | C1 / S1 / G1 / O1 / D1 | timeframe, jurisdiction, population, version, source-family limit, or not applicable | consensus / dominant consensus / mixed / contested / fringe / unclear / blocked / not applicable | supports, caveats, downgrades, or blocks final claim |

## Source Incentive And Bias Audit

Audit source incentives separately from source quality. A source can be
authoritative and still biased by funding, affiliation, vendor interest,
advocacy, self-reporting, sponsorship, or publication incentives.

| Source / Lineage | Incentive / Bias Risk | Funding / Affiliation / Stake | Disclosure Status | Mitigation / Corroboration | Status | Confidence Effect |
|---|---|---|---|---|---|---|
| S1 / G1 | vendor / advocacy / political / regulatory / academic / self-report / affiliate / publication bias / none / unknown | funder, employer, sponsor, seller, regulator, advocacy group, author stake, or unknown | disclosed / undisclosed / unclear / not applicable | independent source, primary record, counter-search, method audit, or caveat | clear / disclosed / mitigated / conflicted / unknown / blocked / not applicable | none / downgrade / insufficient |

## Source Manipulation And Adversarial Provenance Audit

Use this when a source, repository, package, account, review set, dataset,
screenshot, PDF, media item, public comment set, forum thread, or AI/agent-facing
page could be fabricated, manipulated, coordinated, impersonated, poisoned, or
unsafe to trust as-is.

| Manipulation ID | Source / Claim / Community | Manipulation Risk | Authenticity / Provenance Check | Coordination / Amplification Check | Safety / Injection Check | Evidence Links | Status | Confidence Effect |
|---|---|---|---|---|---|---|---|---|
| MP1 | S1 / C1 / G1 / community / not applicable | fabrication, impersonation, account takeover, coordinated amplification, review manipulation, synthetic media, poisoned package/repo, prompt injection, tampered PDF/data, or not applicable | original source, stable locator, metadata, history, archive, signature, maintainer identity, filing/docket, or official cross-check | account age, posting pattern, syndication, duplicate content, bot/amplification signal, review burst, or not applicable | untrusted code/script, hidden prompt, external instruction, active content, install/execute risk, or not applicable | S1 / C1 / G1 / O1 / LD1 / D1 | clear / mitigated / suspected / found / blocked / not applicable | none / downgrade / insufficient / exclude |

## Quantitative And Measurement Audit

Use this for numbers, statistics, rankings, benchmarks, prices, market-size
estimates, survey results, forecasts, KPIs, scores, and measured comparisons.

| Claim / Metric | Value | Unit / Denominator | Population / Scope | Period / Vintage | Method / Source | Uncertainty / Comparability | Status | Confidence Effect |
|---|---|---|---|---|---|---|---|---|
| C1 / metric | value or range | unit, denominator, base, currency, rank base | population, geography, segment, product, jurisdiction | date, period, release, revision, vintage | S1 / method / dataset / benchmark / survey | margin, sample, proxy, non-comparable baseline, caveat | verified / bounded / inconsistent / opaque / blocked / not applicable | none / downgrade / insufficient |

## Currentness And Version Audit

Audit stale-risk and version-dependent claims. Currentness includes publication
date, event date, effective date, accessed date, valid-at date, release tag,
model/version, jurisdiction, and supersession status where relevant.

| Claim / Source | Currentness Need | Evidence Date / Version | Latest / Supersession Check | Status | Confidence Effect |
|---|---|---|---|---|---|
| C1 / S1 | current / historical / versioned / not applicable | YYYY-MM-DD / version / unknown | latest checked / superseded / no later source found / blocked | current / stale / superseded / unknown / not applicable | none / downgraded / insufficient |

## Reproducibility And Refresh Audit

Record how future analysts can rerun or refresh volatile, current-dependent,
versioned, or decision-relevant evidence.

| Item | Reproduction Path | Stable Locator / Version | Volatility / Refresh Trigger | Last Checked | Refresh Action | Status | Confidence Effect |
|---|---|---|---|---|---|---|---|
| whole record / C1 / S1 | query, URL, connector path, repo path, API, docket, registry, or dataset path | archive URL, release tag, commit, package version, dataset vintage, report edition, docket ID, table ID | price / policy / version / law / dataset / market / status / mutable page changes | YYYY-MM-DD | rerun search, reopen source, check changelog, refresh dataset, compare new version | reproducible / bounded / volatile / blocked / not applicable | none / downgrade / insufficient |

## Observation Manifest

Use for observations that support or weaken important claims. Keep it compact;
one row may summarize a bounded source section when enough detail is included.

| Obs ID | Source ID | Evidence Layer | Location | Observation | Independence / Lineage | Valid At | Notes |
|---|---|---|---|---|---|---|---|
| O1 | S1 | primary / dataset / method / currentness / counterevidence | page, section, table, line, field, timestamp | ... | original / independent / same lineage / unclear | date/version | access, sensitivity, translation, or method notes |

## Evidence Location Audit

Every used source and important observation needs a precise evidence locator.
URLs alone are not enough when the source has sections, pages, tables, lines,
timestamps, fields, release tags, issue IDs, or docket entries.

| Claim / Observation | Source ID | Required Locator | Locator Present? | Location Detail | Confidence Effect |
|---|---|---|---|---|---|
| C1 / O1 | S1 | page / section / table / line / timestamp / field / tag / issue / docket | yes / no / blocked / not applicable | exact location or blockage reason | none / downgrade / insufficient |

## Quotation And Context Audit

Use this for direct quotes, translated quotes, paraphrased source positions,
headlines, excerpts, screenshots, social posts, interviews, legal/policy
passages, paper conclusions, and other context-sensitive statements.

| Quote / Passage | Source ID | Speaker / Author | Location | Context Checked | Translation / Paraphrase Risk | Claim Fit | Status | Confidence Effect |
|---|---|---|---|---|---|---|---|---|
| C1 / O1 / quoted or paraphrased passage | S1 | speaker, author, institution, or unknown | page, section, line, timestamp, post, paragraph, table | full paragraph, surrounding section, legal clause, methods, thread, interview, original language | none / low / material / unresolved / not applicable | supports / narrower than claim / contradicts / context missing / not applicable | clear / bounded / distorted / unresolved / blocked / not applicable | none / downgrade / insufficient |

## Absence Evidence Audit

Use this when a conclusion depends on not finding evidence. A search miss is
bounded evidence, not global proof of non-existence.

| Claim / Question | Search Boundary | Source Families Checked | Absence Result | Inference Allowed | Confidence Effect |
|---|---|---|---|---|---|
| C1 | scope, dates, languages, jurisdictions, repos, databases, archives, or source systems searched | official / primary / dataset / scholarly / archive / local-language / repository / counter-search | found / not found / mixed / blocked / not applicable | what absence can and cannot support | none / downgrade / insufficient |

## Claim Ledger

Every important claim used, downgraded, excluded, or explicitly judged
insufficient belongs here before final synthesis. Draft rows may start as
`unresolved`, but final validation requires every Claim Ledger decision to
resolve to `use`, `downgrade`, `exclude`, or `insufficient`.

| Claim ID | Claim | Type | Risk | Support | Counterevidence | Currentness / Version | Verified-Claim Gate | Confidence | Decision |
|---|---|---|---|---|---|---|---|---|---|
| C1 | ... | factual / temporal / comparative / causal / quantitative / evaluative | normal / high | O1, S1 | none found / O2 conflicts | checked YYYY-MM-DD / not current-verified | pass / fail / blocked / not applicable | high / medium / low / insufficient | use / downgrade / exclude / insufficient |

## Claim Risk Triage

Prioritize verification pressure by decision impact and error risk. High-impact
or high-error-risk claims require stronger checks before firm synthesis.

| Claim ID | Decision Impact | Error Risk | Verification Priority | Required Checks | Escalation / Downgrade Rule |
|---|---|---|---|---|---|
| C1 | high / medium / low | high / medium / low | high / medium / low | primary source, counter-search, currentness, lineage, method/data, adversarial review | downgrade or mark insufficient if required checks fail |

## Claim Traceability Matrix

Connect every important final claim to inspected observations, source IDs,
lineage IDs, verification gates, counterevidence, and coverage debt. A claim
without traceability cannot appear as firm synthesis.

| Claim ID | Final Decision | Observations | Sources | Lineages | Verification Gates | Counterevidence / Debt | Confidence Effect |
|---|---|---|---|---|---|---|---|
| C1 | use / downgrade / exclude / insufficient | O1 | S1 | G1 | claim/source/currentness/lineage/overreach | none / D1 / O2 conflicts | high / medium / low / insufficient |

Final Claim Traceability decisions cannot remain `unresolved`; unresolved
evidence must become an `insufficient`, `downgrade`, or `exclude` decision with
the linked debt shown.

## Inference Boundary Audit

Separate direct observation from synthesis. A claim can be traceable and still
overstate what the evidence supports.

| Claim ID | Observation Base | Inference Type | Required Assumptions | Boundary / Not Supported | Status | Confidence Effect |
|---|---|---|---|---|---|---|
| C1 | O1 / S1 | direct observation / bounded inference / comparison / extrapolation / causal / forecast / recommendation / speculative | assumptions needed for the inference | what the evidence does not support | supported / bounded / overreach / speculative / blocked / not applicable | none / downgrade / insufficient |

## Assumption And Sensitivity Audit

Use this when a claim, recommendation, forecast, market estimate, comparison,
policy/legal applicability analysis, technical conclusion, or decision support
item could change under reasonable alternative assumptions.

| Assumption ID | Claim / Decision | Assumption / Variable | Plausible Range / Alternative | Evidence / Test | Sensitivity | Status | Confidence Effect |
|---|---|---|---|---|---|---|---|
| AS1 | C1 / decision | threshold, market definition, scope, timeframe, denominator, benchmark, jurisdiction, version, risk tolerance, or constraint | plausible alternative or scenario | S1 / O1 / D1 / not tested | low / medium / high / decision-changing | stable / sensitive / decision-changing / untested / blocked / not applicable | none / downgrade / insufficient / scenario caveat |

## Conflict Resolution Matrix

Use this for material contradictions between sources, observations, claims,
methods, dates, jurisdictions, versions, or lineages.

| Conflict ID | Claims / Observations | Conflict Type | Evidence On Each Side | Adjudication Basis | Resolution | Confidence Effect |
|---|---|---|---|---|---|---|
| CF1 | C1 / O1 / O2 | source / data / method / date / jurisdiction / version / lineage / interpretation / none | S1 supports; S2 conflicts | authority, directness, currentness, method, lineage, scope, retrieval quality | prefer / bound / split / unresolved / insufficient / not applicable | none / downgrade / insufficient |

## Confidence Calibration

Calibrate final confidence from evidence quality, consistency, directness,
currentness, lineage independence, method quality, counterevidence, and
coverage debt. Confidence follows the weakest material unresolved dimension,
not the number of sources.

| Claim ID | Evidence Strength | Consistency | Directness | Currentness | Lineage Independence | Method / Data Quality | Counterevidence / Debt | Calibrated Confidence | Rationale |
|---|---|---|---|---|---|---|---|---|---|
| C1 | strong / adequate / weak / none | consistent / mixed / conflicting / unknown | direct / partial / indirect | current / stale / unknown / not applicable | independent / same-lineage / unclear / not applicable | strong / adequate / weak / opaque / not applicable | none / minor / material / unresolved | high / medium / low / insufficient | why confidence is capped here |

## Synthesis Traceability Audit

Map final-answer prose back to the record before firm synthesis.

| Output Item | Final Section | Claim Links | Evidence / Source Links | Confidence | Unresolved Limits / Debt | Status | Required Revision |
|---|---|---|---|---|---|---|---|
| ST1 | Answer / Key Findings / Recommendation / Comparison / Caveat | C1 | S1 / O1 | high / medium / low / insufficient | none / D1 / caveat / open question | ready / caveated / revise / blocked / exclude / not applicable | none / add caveat / narrow scope / remove / move to Open Questions |

## Adversarial Review

Before final synthesis, attack the provisional answer. Test alternate
interpretations, missing source families, source incentives, method weaknesses,
transferability limits, stale evidence, and the strongest counterevidence.

| Review ID | Claim / Finding Challenged | Challenge | Evidence Checked | Result | Outcome | Synthesis Effect |
|---|---|---|---|---|---|---|
| A1 | C1 / finding | strongest counterclaim or failure mode | sources, searches, debt IDs, or observations checked | supported / weakened / unresolved | upheld / revised / downgraded / unresolved / insufficient | how final answer changed |

## Stop Rule Audit

Prove why research can stop for each important claim or subquestion. Stopping
requires completed or explicitly blocked search lanes, followed or closed leads,
counter-search, currentness, lineage, source quality, traceability, confidence
calibration, and adversarial review.

| Item | Scope | Stop Criteria Checked | Status | Remaining Gap | Confidence Impact |
|---|---|---|---|---|---|
| SR1 | C1 / L1 / whole record | lanes, source families, EXPAND, counter-search, currentness, lineage, quality, traceability, calibration, adversarial review | satisfied / blocked / not satisfied / not applicable | none / D1 / unresolved source family | none / downgraded / insufficient |

Before final validation, resolve every `not satisfied` stop-rule row to
`satisfied`, `blocked`, or `not applicable`. A final record cannot keep firm
synthesis while the stop rule is not satisfied.

## Atomic Claim Decomposition

Use when the user provided or the research surfaced a complex thesis, rumor,
recommendation, news item, other-AI answer, or dense paragraph.

| Atomic Claim ID | Parent Claim / Source | Atomic Claim | Verification Priority | Distortion Risk | Status |
|---|---|---|---|---|---|
| AC1 | C1 / S2 | one independently checkable fact | high / medium / low | stale / misattribution / magnitude / conflation / inference / none | verify / verified / downgraded / refuted / unresolved |

## Distortion Pattern Audit

Audit repeated, translated, summarized, second-hand, synthetic, or
other-AI-provided claims for common distortion patterns before using them in
firm synthesis.

| Claim / Source | Pattern Checked | Finding | Status | Claim Effect |
|---|---|---|---|---|
| C1 / S2 | stale / misattribution / conflation / circular citation / inference upgraded to fact / magnitude drift / quote distortion / translation drift / cherry-pick / survivorship bias / none | what was checked | clear / found / unresolved / not applicable | none / downgrade / exclude / insufficient |

## Verified Claims

Use this section as the allowlist for high-risk non-code claims that can appear
as firm synthesis. Claims not listed here must be stated with lower confidence,
kept in uncertainty, or excluded.

| Claim ID | Primary / Governing Source | Independent Lineages | Counter-Search | Temporal Evidence | Gate Outcome |
|---|---|---|---|---|---|
| C1 | S1 | S1 lineage; S3 independent | no stronger refutation found / S4 limits | observed/accessed/valid/effective date | pass / partial / fail |

## Evidence

For each important claim, name the supporting source IDs and the evidence
location inside those sources.

## Counterevidence / Uncertainty

Conflicting evidence, weak spots, source limits, source-lineage concerns, and
what would change the answer.

## What I Checked

Source families, query paths, documents, datasets, repositories, connectors, or
local artifacts inspected.

## What I Did Not Check

Relevant source families, leads, or checks not completed, with reasons.

## Search Path

What searches, source families, databases, connectors, or documents were used.
Include enough detail that a future agent can reconstruct the investigation.
Record scout, target, snowball, EXPAND, counter-search, and gap-pass work.

## Leads Followed

Important citations, datasets, authors, laws, standards, product pages,
counterclaims, related terms, repositories, archives, issue threads, or
methodology documents followed during the research.

## Dead Ends

Searches or leads that failed, repeated known evidence, were inaccessible, or
were rejected as low quality.

## Verification Notes

Claim checks, source-quality checks, currentness checks, counterevidence
checks, source-lineage checks, method/data checks, transferability checks, and
synthesis-overreach checks performed before finalizing.

### Evidence Ledger

| Claim | Support | Counterevidence | Source Quality / Lineage | Currentness | Verified-Claim Gate | Confidence | Decision |
|---|---|---|---|---|---|---|---|
| Claim text | S1 section/page | none found / S2 conflicts | primary / independent / same lineage | checked YYYY-MM-DD | pass / fail / not applicable | high / medium / low / insufficient | use / downgrade / exclude / unresolved |

## Coverage Gates

State which gates passed, failed, were blocked, or were not applicable:

- saturation completeness
- question coverage audit
- saturation metrics
- search matrix
- diversified search batch plan
- decision usefulness
- evidence maturity dashboard
- comparison and evaluation audit
- tool capability audit
- domain coverage matrix
- language and locale audit
- entity and terminology audit
- search craft floors
- search result triage
- search bias and retrieval trap audit
- selection and inclusion audit
- access and retrieval audit
- source-count and source-diversity floor
- lane coverage
- worker-wave coverage
- source lineage map
- source quality audit
- corroboration and triangulation audit
- consensus and disagreement audit
- source incentive and bias audit
- source manipulation and adversarial provenance audit
- quantitative and measurement audit
- currentness and version audit
- reproducibility and refresh audit
- evidence location audit
- absence evidence audit
- claim risk triage
- claim traceability matrix
- inference boundary audit
- assumption and sensitivity audit
- conflict resolution matrix
- confidence calibration
- adversarial review
- stop rule audit
- distortion pattern audit
- scout
- target
- snowball
- EXPAND lead loop
- frontier queue convergence
- expansion frontier audit / frontier extraction
- lead ledger
- coverage debt cleared or downgraded
- counter-search
- gap pass
- source audit
- claim verification audit
- currentness audit
- contradiction and gap audit
- source-lineage audit
- verified-claim gate
- synthesis-overreach audit
- method/data audit, when applicable

Explain why the stop rule was reached, or list unresolved gaps and affected
claims.

## Acceptance Tests

Record required test results before final synthesis.
Required rows that remain `fail` do not pass final validation. Use `blocked` or
`not applicable` only with a concrete reason, evidence/location, remediation or
confidence/synthesis impact, and the affected final sections.

| Test | Required? | Result | Evidence / Location | Remediation |
|---|---|---|---|---|
| Single Markdown Record Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Saturation Protocol Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Question Coverage Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Search Matrix Completion Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Saturation Metrics Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Decision Usefulness Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Evidence Maturity Dashboard Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Comparison And Evaluation Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Tool Capability Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Diversified Search Batch Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Worker Wave Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Domain Coverage Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Language And Locale Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Entity And Terminology Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Search Craft Floor Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Search Result Triage Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Search Bias And Retrieval Trap Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Selection And Inclusion Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Access And Retrieval Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Source-Opened Follow-Up Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Source Coverage Floor Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Source Lineage Map Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Source Quality Audit Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Corroboration And Triangulation Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Consensus And Disagreement Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Source Incentive And Bias Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Source Manipulation And Adversarial Provenance Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Quantitative And Measurement Test | conditional | pass / fail / blocked / not applicable | ... | ... |
| Currentness And Version Audit Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Reproducibility And Refresh Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Evidence Location Audit Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Quotation And Context Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Absence Evidence Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Claim Risk Triage Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Claim Traceability Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Inference Boundary Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Assumption And Sensitivity Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Conflict Resolution Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Confidence Calibration Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Synthesis Traceability Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Adversarial Review Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Stop Rule Audit Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Atomic Claim Decomposition Test | conditional | pass / fail / blocked / not applicable | ... | ... |
| Distortion Pattern Audit Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Claim Support Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Snippet Leakage Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Source-Family Coverage Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Lead Ledger / EXPAND Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Expansion Frontier Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Frontier Queue Convergence Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Coverage Debt Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Currentness Test | conditional | pass / fail / blocked / not applicable | ... | ... |
| Counterevidence Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Provenance / Lineage Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Verified-Claim Gate Test | conditional | pass / fail / blocked / not applicable | ... | ... |
| Method / Data Test | conditional | pass / fail / blocked / not applicable | ... | ... |
| Synthesis Overreach Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Deliverable Readability Test | yes | pass / fail / blocked / not applicable | ... | ... |

## Confidence

Confidence by important claim or subquestion: high / medium / low /
insufficient.

## Open Questions

Unresolved issues, pending leads, or checks that would matter for a later
refresh.
```

Use source IDs from `## Sources` throughout the file. A used source must have an
inspected body or retrieved record; snippets, AI summaries, generated summaries,
search result previews, and subagent conclusions are leads, not evidence.

## Optional Additions

Add a compact decision matrix, comparison table, timeline, claim graph, or
domain-specific table only when it clarifies the answer. Keep it inside the
same Markdown file. Do not create large tables merely to satisfy format.
