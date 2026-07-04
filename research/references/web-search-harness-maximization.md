# Web Search Harness Maximization

Use this reference whenever web, search, browser, connector, archive, repository,
or document-fetch tools are available for a research task. It is not a mode.
It is the default operating discipline for maximum-saturation research.

## Principle

Search tools are not answer generators. They are source-discovery and source
access tools. Use them to produce inspected source bodies, lead chains,
counterevidence, currentness checks, and provenance checks that can be recorded
inside the single Markdown research record.

Do not stop at result snippets, AI-generated overviews, search-result summaries,
or subagent summaries. A source counts only after the body or retrieved record
has been opened, inspected, and mapped to an observation, lead, or claim
decision.

## Harness Max-Use Rule

Use the full search surface exposed by the harness. Combine general web search
with official domains, site/filetype queries, local-language queries,
date/currentness queries, counter-search, archives, PDFs, APIs, repositories,
package registries, issue trackers, standards, datasets, and connectors when
relevant.

For each important lane, push beyond visible top results: open likely primary
sources, follow citations and outbound links, search exact titles or quoted
phrases, inspect source bodies, and route inaccessible sources through
authorized alternates such as archives, PDFs, APIs, official mirrors, repository
history, or browser/connector access. If a harness capability is unavailable or
blocked, record it in `## Tool Capability Audit` and create coverage debt rather
than treating the lane as complete.

## Batch Search Discipline

Use the active harness close to its practical limit:

- batch independent queries together when the tool supports it
- mix source families in each early batch: scout, official, document/PDF,
  scholarly, dataset/method, currentness, counterevidence, and provenance
- avoid repeated equivalent queries; every new query should change source
  family, vocabulary, operator, language, jurisdiction, timeframe, or
  counterevidence angle
- keep one batch for broad discovery before narrowing around the first good
  source
- reserve later batches for targeted gaps, lead expansion, counter-search,
  source-lineage checks, and currentness

For tools with small per-call query limits, group queries by independent
decision value, not by convenience. For example, do not spend a whole early
batch on five similar keyword variants when official, counterevidence,
provenance, and currentness queries are still missing.

When local command execution is available, use
`research/scripts/query_matrix.py --format batches --batch-size <tool-limit>` to
seed diversified search batches. Treat each batch as a portfolio across source
families rather than a set of near-duplicate keyword variants. The default batch
shape should mix scout, official/primary, document/PDF, scholarly, dataset,
currentness, counterevidence, lineage/provenance, frontier-expansion, and
blocked-source-recovery paths before narrowing.

## Minimum Search Pressure Before Synthesis

When web/search tools are available, do not synthesize from a single search
family or a single result page. Before firm synthesis, each central claim or
decision axis needs visible pressure from these search paths unless the record
marks a path blocked or not applicable with a reason:

- broad scout for vocabulary, aliases, and source-family discovery
- official, governing, primary, repository, docket, dataset, or source-of-truth
  search
- document/PDF, method, appendix, changelog, advisory, codebook, release, or
  filing search
- counterevidence, limitation, criticism, denial, correction, failed
  replication, incident, issue, complaint, or supersession search
- currentness, latest, effective-date, version, release, advisory, or
  deprecation search for time-sensitive claims
- provenance or source-lineage search for origin, first report, cited-by,
  archive, transcript, mirror, syndication, or quote context
- frontier-expansion search from citations, authors, datasets, standards,
  repositories, issues, dockets, native terms, corrections, and blocked sources

Search counts alone do not satisfy this floor. A lane counts only when the best
available results are opened or retrieved, inspected, classified, and integrated
into `## Search Craft Log`, `## Search Result Triage`, `## Sources`,
`## Observation Manifest`, `## Lead Ledger`, `## Expansion Frontier Audit`,
`## Coverage Debt`, or `## Claim Ledger`.

## Frontier Queue Discipline

Treat the search process as a live frontier queue. Every meaningful result,
opened source, citation, dataset, author, institution, standard, repository,
issue, docket, archive target, review cluster, local-language term,
counterclaim, correction, and blocked primary source should either become a
lead or be explicitly closed as duplicate, irrelevant, low quality, out of
scope, or unable to affect the answer.

Prioritize frontier items by decision impact, error risk, source-family
uniqueness, proximity to original or primary evidence, ability to resolve
coverage debt, and likelihood of changing confidence. Later batches should come
from the strongest unresolved frontier items, not from more variants of the
first successful query family.

Run expansion in mixed batches where possible: combine citation snowballing,
official/source-of-truth follow-up, method or dataset lookup, currentness,
counterevidence, provenance, local-language, archive, repository, and
review/forum paths according to the topic. A lane reaches convergence only when
a full expansion or gap cycle produces no new high-value leads, or remaining
leads are closed with reasons and confidence effects in the single record.

## Query Portfolio

For each important search matrix row, run a portfolio rather than a single
query:

- broad scout query for vocabulary and landscape
- exact-phrase query for the claim, title, product, law, source, quote, or
  metric
- official/source-of-truth query using institution, regulator, vendor, standard
  body, repository, docket, or dataset names
- document query using filetype, report, guidance, specification, methodology,
  appendix, changelog, advisory, release, or codebook terms
- scholarly or technical query when methods, definitions, experiments,
  benchmarks, or expert interpretation matter
- local-language or native-script query for local, jurisdictional, translated,
  identity, or non-English topics
- counter-search query for criticism, rebuttal, denial, correction, failed
  replication, limitation, lawsuit, incident, bug, vulnerability, or
  supersession
- provenance query for original, source, first reported, archive, transcript,
  quoted, cited by, references, based on, mirror, or syndication
- currentness query for latest, update, changelog, release notes, deprecated,
  superseded, advisory, effective date, or valid-at date

Record the query portfolio in `## Search Craft Log` and the outcome in
`## Wave Log`, `## Lead Ledger`, `## Expansion Frontier Audit`, or
`## Coverage Debt`.

## Saturation Metrics

Use `## Saturation Metrics` as the running dashboard for harness pressure. For
each important lane or whole-record scope, record distinct query count,
inspected source/record count, expansion-wave count, counter-search coverage,
local-language or jurisdictional sweep status, material lead closure, and
frontier queue convergence. Update the metrics during the run, not only in the
final pass.

If metrics are below floor because the harness is unavailable, access is
blocked, or the corpus is genuinely sparse, record the reason and confidence
effect. If metrics are below floor because the search was thin, continue with a
targeted scout, target, EXPAND, counter-search, or gap pass.

## Expansion Frontier Audit

Use `## Expansion Frontier Audit` to convert the strongest web results and
opened source bodies into new search pressure. Extract citations, authors,
institutions, datasets, methods, aliases, native terms, product/version labels,
successors, corrections, repositories, issues, dockets, standards, reviews,
complaints, and counterclaims. For each material frontier, record the exact
query, connector path, archive path, repository path, database path, or blocked
reason.

Do not count a broad web sweep as saturated if strong sources still contain
unsearched frontiers that could change an important claim or close a missing
source family.

## Source Opening Ladder

After search results arrive, open sources in this order when available:

1. governing, official, primary, original, or source-of-truth records
2. datasets, methodology notes, codebooks, appendices, release notes, source
   code, issues, dockets, filings, laws, standards, and advisories
3. systematic reviews, peer-reviewed papers, expert reports, institutional
   analysis, and high-quality journalism that links to primary material
4. archives, mirrors, cached pages, transcripts, or quote sources for
   provenance and missing-source recovery
5. forums, reviews, social media, support threads, app stores, and community
   traces when behavior, sentiment, adoption, failure reports, or edge cases are
   relevant

Weak sources can be useful as leads. They do not become strong evidence unless
the research question is specifically about those sources or they are
triangulated with stronger evidence and their limits are recorded.

## Open, Find, And Extract

For every important source body:

- open the source or retrieve the connector record before citing it
- use in-page search or equivalent extraction for exact claim terms, dates,
  methods, tables, limitations, definitions, version numbers, and references
- record the inspected section, page, table, line, timestamp, issue number,
  release tag, docket ID, or field in `## Sources` or `## Observation Manifest`
- extract citations, datasets, named institutions, authors, standards,
  repositories, issues, advisories, corrections, and archives as leads
- mark inaccessible, blocked, paywalled, script-only, login-only, or ambiguous
  sources in `## Dead Ends` or `## Coverage Debt`

If the source body cannot be opened but the source may matter, try authorized
alternatives: official mirrors, PDFs, archives, browser access, APIs,
connectors, package registries, repository files, text fetches, or quoted
primary excerpts. If still blocked, do not use it as firm support.

## Source-Opened Follow-Up Rule

Every high-value opened source should create follow-up search pressure before
it supports a central claim. Extract at least one of these when present and
either search it, close it, or record why it cannot affect the answer:

- cited source, footnote, appendix, method, dataset, codebook, or repository
- author, institution, regulator, standards body, docket, issue, advisory, or
  release identifier
- exact title, quoted phrase, claim wording, metric label, product/version
  label, native-language term, alias, or predecessor/successor name
- correction, update, retraction, supersession, erratum, limitation, dissent,
  counterclaim, complaint, incident, bug, or vulnerability

If a strong source produces no follow-up leads, record `none` with a reason in
`## Lead Ledger` or `## Expansion Frontier Audit`. Do not treat source opening
as complete until material extracted leads are followed, blocked, closed, or
converted into confidence effects.

## Expansion Waves

Run lead expansion in waves:

- wave 1 extracts high-value leads from broad scout and primary seeds
- wave 2 follows citations, documents, methods, standards, repositories,
  issues, archives, dockets, and counterclaims
- wave 3 checks unresolved leads that could change claim confidence, scope,
  timing, or applicability

Stop expansion only when a full wave creates no new high-value leads, or when
remaining leads are duplicate lineage, low quality, blocked, out of scope, or
unable to change important claims. Record the closure reason.

## Currentness And Supersession

For current-dependent claims:

- search the claim plus latest/update/superseded/deprecated/changelog/release
  notes/advisory/effective-date terms
- compare publication date, event date, effective date, accessed date, version,
  release tag, and valid-at date
- check whether official guidance, docs, laws, datasets, advisories, prices,
  package versions, or product availability changed after the strongest source
- downgrade or label `insufficient` when currentness cannot be verified

## Counterevidence Search

For central claims, search the strongest plausible ways the claim could be
wrong before synthesis:

- direct negation, denial, correction, retraction, erratum, supersession
- failed replication, null result, negative case, limitation, boundary condition
- lawsuit, enforcement, incident, vulnerability, bug, complaint, recall
- source-lineage challenge, duplicated reporting, vendor-funded claim,
  methodological flaw, stale data, or non-comparable metric

If counterevidence is weak or absent, record what was searched. If
counterevidence is material, keep it visible in the claim ledger and final
synthesis.

## Absence Evidence

When a search does not find support, record the result as bounded absence
evidence, not proof of non-existence. Add rows to `## Absence Evidence Audit`
for important "not found" conclusions, including the source families,
languages, jurisdictions, dates, repositories, databases, or archives actually
searched and the access limits encountered.

Only use absence as support when the expected authoritative source family was
searched or the record explains why another searched family is a reliable
proxy. Otherwise, keep the claim at `low` or `insufficient` confidence.

## Search Output Triage

Classify each search result quickly:

- `open-now`: likely primary, governing, original, method, dataset, or central
  counterevidence
- `lead`: useful citation, actor, term, document, issue, archive, or
  source-family path
- `duplicate-lineage`: repeats an already inspected upstream source
- `context-only`: useful background but not claim support
- `dead-end`: inaccessible, low quality, irrelevant, stale, spam, or unable to
  affect a claim

Only `open-now` sources and later-inspected leads can become evidence.
When a result is `duplicate-lineage`, add or update the `## Source Lineage Map`
instead of counting it as independent corroboration.

## Search Bias And Retrieval Trap Pressure

For every important web or connector search lane, assume the visible result set
is biased until checked. Run diagnostics for top-result dependence,
SEO/sponsored pages, snippets or AI-generated overviews, duplicate syndication,
English/local-language mismatch, query wording, personalization, paywalls, stale
indexes, missing archives, review manipulation, marketplace ranking, and corpus
coverage gaps. Use alternate paths such as official domains, filetype queries,
exact-title queries, local terms, archives, direct site search, databases,
repositories, package registries, cited-source snowballing, and counter-search.
Record the result in `## Search Bias And Retrieval Trap Audit`.

## Consensus And Disagreement Pressure

When an answer could imply consensus, mainstream view, best practice, standard,
or broad preference, search for consensus signals and disagreement separately.
Use query families for guidelines, standards, systematic reviews, meta-analyses,
official positions, expert reviews, maintainer positions, repeated independent
findings, dissent, criticism, failures, minority views, and fringe claims. Record
the result in `## Consensus And Disagreement Audit` before synthesis.

## Comparison And Evaluation Pressure

When the topic asks for comparison, recommendation, ranking, alternatives,
vendor/product choice, market scan, policy/legal option, academic theory
comparison, investment diligence, or security diligence, search each option and
criterion symmetrically where possible. Add targeted queries for missing criteria,
non-comparable definitions, counterexamples, failure cases, and tradeoffs before
synthesis. Record the result in `## Comparison And Evaluation Audit` rather than
hiding it in prose.

## Record Integration

Every meaningful search or source-opening pass should update at least one of:

- `## Search Craft Log`
- `## Search Result Triage`
- `## Search Bias And Retrieval Trap Audit`
- `## Saturation Metrics`
- `## Decision Usefulness Matrix`
- `## Comparison And Evaluation Audit`
- `## Tool Capability Audit`
- `## Domain Coverage Matrix`
- `## Language And Locale Audit`
- `## Access And Retrieval Audit`
- `## Wave Log`
- `## Lead Ledger`
- `## Expansion Frontier Audit`
- `## Sources`
- `## Source Lineage Map`
- `## Source Quality Audit`
- `## Corroboration And Triangulation Audit`
- `## Consensus And Disagreement Audit`
- `## Source Incentive And Bias Audit`
- `## Source Manipulation And Adversarial Provenance Audit`
- `## Quantitative And Measurement Audit`
- `## Currentness And Version Audit`
- `## Evidence Location Audit`
- `## Absence Evidence Audit`
- `## Observation Manifest`
- `## Claim Ledger`
- `## Claim Risk Triage`
- `## Claim Traceability Matrix`
- `## Confidence Calibration`
- `## Adversarial Review`
- `## Stop Rule Audit`
- `## Distortion Pattern Audit`
- `## Coverage Debt`
- `## Dead Ends`

Accumulating tabs, snippets, or bookmarks without integrating them into the
single record does not count toward saturation.

## Failure Modes

Avoid these failures:

- opening only the top search result
- using result snippets as evidence
- running many near-duplicate keyword searches
- searching only English for local or translated topics
- treating repeated secondary articles as independent support
- failing to search the opposite claim
- treating `not found` as proof of absence without searched-boundary limits
- failing to check latest/currentness for unstable claims
- ignoring blocked primary sources without alternate retrieval attempts
- synthesizing before lead expansion, expansion frontier, and coverage debt are
  resolved
- treating the first plausible source family as convergence while material
  frontier queue items remain open

When any failure mode occurs, record it as coverage debt and remediate or
downgrade affected claims.
