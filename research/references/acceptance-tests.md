# Acceptance Tests

Run these tests before final synthesis for professional, enterprise,
externally-reviewed, high-stakes, or decision-ready research.

## Test Matrix

Record the result in the single research record under `## Coverage Gates`.
Required tests that remain `fail` do not pass final validation. Use `blocked`
or `not applicable` only with a concrete reason, evidence/location, remediation
or confidence/synthesis impact, and the affected final sections.

```markdown
## Acceptance Tests

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
| Search Bias And Retrieval Trap Test | conditional | pass / fail / blocked / not applicable | ... | ... |
| Source-Family Coverage Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Lead Ledger / EXPAND Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Expansion Frontier Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Frontier Queue Convergence Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Coverage Debt Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Currentness Test | conditional | pass / fail / blocked / not applicable | ... | ... |
| Counterevidence Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Consensus And Disagreement Test | conditional | pass / fail / blocked / not applicable | ... | ... |
| Provenance / Lineage Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Source Manipulation And Adversarial Provenance Test | conditional | pass / fail / blocked / not applicable | ... | ... |
| Verified-Claim Gate Test | conditional | pass / fail / blocked / not applicable | ... | ... |
| Method / Data Test | conditional | pass / fail / blocked / not applicable | ... | ... |
| Sensitivity / Access Test | conditional | pass / fail / blocked / not applicable | ... | ... |
| Synthesis Overreach Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Decision Usefulness Test | conditional | pass / fail / blocked / not applicable | ... | ... |
| Evidence Maturity Dashboard Test | yes | pass / fail / blocked / not applicable | ... | ... |
| Comparison And Evaluation Test | conditional | pass / fail / blocked / not applicable | ... | ... |
| Deliverable Readability Test | yes | pass / fail / blocked / not applicable | ... | ... |
```

## Test Definitions

- `Single Markdown Record Test`: one explicit research request produced exactly
  one Markdown record with no topic folder, sidecar notes, source ledgers,
  screenshot folders, per-agent artifacts, or auxiliary research files, and all
  search logs, batch plans, frontier queue items, worker-wave notes, source
  rows, observations, blocked-source recovery attempts, claim decisions,
  verification notes, validation outcomes, and synthesis are inside it.
- `Saturation Protocol Test`: the record shows a search matrix, lane plan,
  scout, target, snowball, EXPAND, counter-search, gap pass, and stop-rule
  result, or explicitly records why a tool/access/user-budget limit prevented a
  component.
- `Question Coverage Test`: every user-requested question part, comparison
  axis, deliverable requirement, and explicit constraint is mapped to answered,
  partially answered, unanswered, blocked, out-of-scope, or not-applicable
  status with evidence links, residual gaps, and final-answer location.
  Unanswered rows do not pass final validation.
- `Search Matrix Completion Test`: every Search Matrix lane has a final status
  of complete, blocked, superseded, or not applicable before synthesis; planned
  or running lanes create coverage debt and do not pass final validation.
- `Saturation Metrics Test`: the record states actual counts or closure status
  for query diversity, inspected source/record floor, expansion waves,
  counter-search passes, local-language or jurisdictional sweeps when relevant,
  material lead closure, and frontier queue convergence, with downgrade or
  blockage notes for missed metrics. Metrics that remain `not met` do not pass
  final validation.
- `Decision Usefulness Test`: when the research informs a choice,
  recommendation, comparison, purchase, diligence, strategy, or next action,
  the record states options, criteria, evidence links, risks/tradeoffs, and
  what would change the decision; otherwise it records why decision framing is
  not applicable.
- `Comparison And Evaluation Test`: when the research compares options,
  recommends, ranks, evaluates vendors/products/policies/theories/markets, or
  uses better/worse/prefer/choose language, the record states options/entities,
  criteria/axes, weights or priorities, evidence links, missing or
  non-comparable data, tradeoffs/sensitivity, status, and decision effect. If no
  comparison or recommendation is present, the row is marked `not applicable`.

- `Evidence Maturity Dashboard Test`: central claims, comparisons,
  recommendations, decisions, and source-family conclusions are summarized as
  mature, caveated, immature, blocked, or not applicable, with linked claims or
  questions, required gate cluster, weakest link, and decision/synthesis effect.
  Firm final prose is not written for immature or blocked items.

- `Tool Capability Test`: available search, source-open/fetch, extraction,
  connector/database, local file/code, repository/package, archive/browser,
  document/PDF, and subagent/parallel-lane capabilities are used, blocked,
  unavailable, or not applicable with fallback and record impact. The record
  must explicitly cover web search, batch / parallel diversified search,
  source open/fetch, source retrieval fallback, and subagent/parallel or
  sequential-lane capability so harness limits and actual usage are auditable;
  planned capability rows do not pass final validation.
- `Diversified Search Batch Test`: the record shows at least three batch /
  parallel diversified search passes that mix independent source families,
  including official/source-of-truth, currentness, counterevidence,
  frontier-expansion, and blocked-source-recovery passes, and maps each batch
  to named record sections where evidence, leads, debt, and verification were
  integrated. When a batch-search generator or active search-tool limit is
  used, the record preserves execution sub-batches, query counts, and numeric
  tool-limit notes; generic notes or unmapped batch rows do not pass.
- `Worker Wave Test`: the record shows W0 framing, W1 scout, W2 target and
  snowball, W3 EXPAND/counter/currentness/provenance/gap work, and W4
  verification/synthesis-overreach work, or records a blocked component and
  confidence impact.
- `Domain Coverage Test`: broad domain protocols are explicitly considered,
  including official/primary, currentness, scholarly, data/method, legal/policy,
  market/product, technical/OSS, security/risk, provenance/identity/archive, and
  public sentiment/behavior; each is searched, covered, blocked, or marked not
  applicable with a reason. Planned domain rows do not pass final validation.
- `Language And Locale Test`: local, translated, identity, policy, legal,
  market, cultural, or non-English topics include native terms, aliases,
  scripts, local source families, and local-language searches, or explain why
  these are not applicable. Planned language/locale rows do not pass final
  validation.
- `Entity And Terminology Test`: ambiguous entities, aliases, acronyms,
  translations, product/version labels, jurisdictions, overloaded concepts, and
  false positives are resolved, bounded, blocked with confidence impact, or
  marked not applicable before sources support claims.
- `Search Craft Floor Test`: query diversity, operator/source-family variation,
  two-cycle theme coverage, and language/locality choices meet the floors in
  `research-process.md` or the limits are recorded.
- `Search Result Triage Test`: meaningful search results are classified as
  `open-now`, `lead`, `duplicate-lineage`, `context-only`, or `dead-end`; only
  opened or retrieved sources become evidence.
- `Search Bias And Retrieval Trap Test`: important search lanes and source
  families record whether ranking bias, SEO or sponsored results, snippet or
  AI-overview leakage, duplicate lineage, language/locality mismatch, query bias,
  personalization, paywalls, corpus gaps, stale indexes, or platform filters
  could distort discovery; each material trap is mitigated, bounded, blocked, or
  tied to a confidence effect.

- `Selection And Inclusion Test`: important evidence sets record inclusion
  criteria, exclusion or downrank criteria, included sources, excluded or
  downranked results, selection risk, mitigation, status, and confidence effect
  so cherry-picking and convenience sampling are visible.
- `Access And Retrieval Test`: important sources are opened or retrieved; when
  primary access fails, authorized alternate paths such as archives, PDFs, APIs,
  browser access, mirrors, repositories, package registries, cached copies, or
  cited excerpts are tried or the affected claims are downgraded.
- `Source-Opened Follow-Up Test`: high-value opened sources are mined for
  citations, authors, datasets, identifiers, native terms, corrections,
  counterclaims, and blocked primaries; material leads are searched, closed,
  blocked, downgraded, or converted into Lead Ledger / Expansion Frontier rows.
- `Source Coverage Floor Test`: inspected source bodies or retrieved records
  are sufficient for the task scope, usually 12+ narrow, 25+ broad/comparative,
  or 50+ very broad/diligence/literature/market/policy/discovery/SOTA, unless
  scarcity or access limits are recorded and reflected in confidence.
- `Source Lineage Map Test`: sources used as independent support are mapped to
  upstream origins; same-lineage summaries, mirrors, syndicated articles,
  excerpts, translations, and repeated use of one dataset are not double-counted.
- `Source Quality Audit Test`: every used source is assessed for authority,
  directness, currentness, method/data quality, lineage, overall status, and
  confidence effect.
- `Corroboration And Triangulation Test`: every important claim records
  primary/governing support or a source-of-truth exception, independent
  corroboration or single-authority rationale, counterevidence/limitations,
  method/data checks when relevant, lineage diversity, status, and confidence
  effect before firm synthesis.
- `Consensus And Disagreement Test`: central questions and important claims
  record the relevant source community or field, consensus signal,
  disagreement or minority view, evidence links, recency/scope limits, status,
  and confidence effect before the answer describes a position as consensus,
  mainstream, best practice, standard, broadly accepted, or generally true.

- `Source Incentive And Bias Test`: decision-relevant or claim-supporting
  sources are audited for funding, affiliation, vendor/advocacy stake,
  self-reporting, sponsorship, publication bias, disclosure status, mitigation,
  corroboration needs, and confidence effects.
- `Source Manipulation And Adversarial Provenance Test`: sources with material
  fabrication, impersonation, account takeover, coordinated amplification,
  review manipulation, astroturfing, synthetic media, tampered document/data,
  poisoned repository/package, malicious script, active content, or
  prompt-injection risk are checked passively and safely; unresolved risks are
  downgraded, excluded, blocked, or marked insufficient.

- `Quantitative And Measurement Test`: important numbers, statistics, rankings,
  benchmarks, prices, market-size estimates, surveys, forecasts, KPIs, scores,
  or measured comparisons record unit, denominator, population/scope, period or
  vintage, method/source, uncertainty, and comparability limits before firm
  synthesis.
- `Currentness And Version Audit Test`: current, dated, version-dependent, or
  jurisdiction-dependent claims record evidence date/version, latest or
  supersession checks, status, and confidence effect.
- `Reproducibility And Refresh Test`: mutable, current-dependent, versioned, or
  decision-relevant claims and sources record rerun path, stable
  locator/version, volatility or refresh trigger, last-checked date, refresh
  action, status, and confidence effect.
- `Evidence Location Audit Test`: every used source and important observation
  has a precise evidence location such as page, section, table, line,
  timestamp, field, release tag, issue ID, docket entry, or a blockage reason
  with confidence impact.
- `Quotation And Context Test`: every direct quote, translated passage,
  paraphrased source position, headline, excerpt, screenshot, social post,
  interview statement, legal/policy passage, and paper conclusion used as
  support records attribution, precise location, surrounding context,
  translation/paraphrase risk, claim fit, status, and confidence effect.
- `Absence Evidence Test`: conclusions that rely on not finding evidence record
  the searched boundary, source families, language/jurisdiction or repository
  scope, retrieval limits, and the exact inference allowed; otherwise the claim
  is downgraded or phrased as bounded to searched sources.
- `Claim Risk Triage Test`: important claims are prioritized by decision
  impact and error risk, and high-priority claims receive primary-source,
  counter-search, currentness, lineage, method/data, and adversarial checks
  before firm synthesis.
- `Claim Traceability Test`: every important final claim maps to inspected
  observations, source IDs, lineage IDs, verification gates, counterevidence or
  coverage debt, and confidence effect before firm synthesis.
- `Inference Boundary Test`: important synthesized claims distinguish direct
  observations from bounded inference, comparison, extrapolation, causal
  interpretation, forecast, recommendation, or speculative steps; assumptions,
  transferability limits, unsupported boundaries, and confidence effects are
  recorded before firm synthesis.
- `Assumption And Sensitivity Test`: assumptions, thresholds, baselines,
  comparators, scopes, scenarios, timeframes, versions, jurisdictions,
  denominators, methods, risk tolerances, and user constraints that could change
  the conclusion are tested, bounded, blocked with confidence effects, or
  surfaced as scenario caveats in final synthesis.
- `Conflict Resolution Test`: material contradictions between sources,
  observations, methods, dates, jurisdictions, versions, lineages, or
  interpretations are adjudicated, bounded, split by context, left unresolved,
  or marked insufficient with confidence effects.
- `Confidence Calibration Test`: final confidence for every important claim is
  calibrated against evidence strength, consistency, directness, currentness,
  source-lineage independence, method/data quality, counterevidence, and
  unresolved coverage debt.
- `Synthesis Traceability Test`: final answer paragraphs, key findings,
  recommendations, decision/action items, comparison rows, caveats, and
  material summary sentences map to claim IDs, source or observation IDs,
  confidence, unresolved debt, and revision status; unsupported prose is
  revised, caveated, moved to uncertainty/open questions, or removed.
- `Adversarial Review Test`: provisional conclusions are challenged with
  alternate interpretations, missing source-family checks, incentive/bias
  checks, method weaknesses, transferability limits, stale evidence, and the
  strongest counterevidence before final synthesis.
- `Stop Rule Audit Test`: the record explains why research can stop for each
  important claim or subquestion, including lane completion, EXPAND lead
  closure, counter-search, currentness, lineage, source quality, traceability,
  confidence calibration, adversarial review, and remaining gaps. Stop-rule rows
  that remain `not satisfied` do not pass final validation.
- `Atomic Claim Decomposition Test`: complex theses, forwarded claims, other-AI
  conclusions, rumors, screenshots, market stories, or dense paragraphs are
  decomposed into independently checkable atomic claims before verification.
- `Distortion Pattern Audit Test`: repeated, translated, summarized,
  second-hand, synthetic, or other-AI-provided claims are checked for stale
  evidence, misattribution, conflation, circular citation, inference upgraded to
  fact, magnitude drift, quote distortion, translation drift, cherry-picking,
  and survivorship bias where relevant.
- `Claim Support Test`: every important claim appears in the Claim Ledger and
  maps to inspected/retrieved sources or is labeled `insufficient`.
  Unresolved final Claim Ledger or Claim Traceability decisions do not pass
  final validation.
- `Snippet Leakage Test`: no source marked `used` relies only on snippets,
  generated overviews, AI summaries, abstracts when full text is needed, or
  unsupported secondary claims.
- `Source-Family Coverage Test`: required source families are checked,
  unavailable, or explicitly not applicable with reasons.
- `Lead Ledger / EXPAND Test`: high-value leads from searches, inspected
  sources, subagents, and verification are followed or closed with reasons.
  Open actions or unresolved final lead outcomes do not pass final validation.
- `Expansion Frontier Test`: strong seeds, inspected sources, search results,
  citations, authors, datasets, methods, aliases, local terms, successors,
  corrections, repositories, issues, dockets, standards, reviews, complaints,
  and counterclaims that could change important claims are converted into
  explicit query or connector passes, closed with reasons, blocked with
  confidence effects, or marked unable to change the claim. Planned frontier
  rows do not pass final validation.
- `Frontier Queue Convergence Test`: the Lead Ledger and Expansion Frontier
  Audit show that the latest EXPAND or gap cycle produced no new high-value
  leads, or every remaining material lead is closed, blocked with confidence
  effect, duplicate-lineage, out of scope, low quality, or unable to change an
  important claim.
- `Coverage Debt Test`: thin lanes, unfollowed high-value leads, missing source
  families, blocked source bodies, unresolved contradictions, freshness gaps,
  weak provenance, and method gaps are cleared, blocked with reason, or tied to
  confidence downgrades. Open coverage debt rows do not pass final validation.
- `Currentness Test`: current-dependent claims have as-of timestamp,
  latest-update/supersession check, and source date/version.
- `Counterevidence Test`: the strongest plausible counterclaims, contradictions,
  negative cases, and limitations were searched and reflected in confidence.
- `Provenance / Lineage Test`: original/source-of-claim, duplicate lineage,
  mirror/archive/excerpt role, and mutable-source custody are recorded.
- `Verified-Claim Gate Test`: high-risk non-code claims have primary/governing
  backing or a source-of-truth exception, independent lineages where applicable,
  counter-search, temporal evidence, and a gate outcome before firm synthesis.
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
