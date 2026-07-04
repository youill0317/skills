# Query And Source Patterns

Apply `evidence-needs-core.md` first. This file contains general query mechanics
that are useful across domains. Load narrower references for domain-specific
patterns.

## Specialized References

| Need | Load |
|---|---|
| person, organization, public figure, author, vendor, nonprofit, project, or institution profile | `profiles-and-identity.md` |
| non-English, multilingual, local-language, or origin-jurisdiction research | `multilingual-research.md` |
| official statistics, datasets, dashboards, surveys, administrative data, benchmarks, models, rankings, estimates, or proxy data | `data-statistics-and-surveys.md` |
| reviews, forums, social media, app stores, support threads, or community traces | `public-sentiment-and-behavior.md` |
| repeated claims, provenance, quotes, screenshots, viral claims, archives, deleted sources, or historical captures | `source-provenance-and-archives.md` |
| current events, fast-changing claims, filings, corrections, denials, or latest-status checks | `current-events.md` |
| policy, regulatory, or legal landscape research | `policy-regulatory-legal.md` |
| academic paper search or literature review | `scholarly-search-and-literature-review.md` |
| market, competitor, product, recommendation, purchase, OSS, or community-health research | `competitive-market-analysis.md` |
| explicitly requested and authorized internal or connected-source research | `enterprise-search-and-synthesis.md` |
| business, strategy, diligence, procurement, policy, risk, executive, or decision-support research | `enterprise-research-operations.md` |
| professional, high-stakes, externally reviewed, or research-firm-replacement work | `professional-research-quality.md` |
| clinical/medical, financial/investment, litigation/legal-support, OSINT, security, procurement, customer/UX, or regulated-domain research | `high-stakes-domain-protocols.md` |

## Broadening And Narrowing

If searches return too few useful results, broaden in this order:

1. Remove date or location filters.
2. Replace exact phrases with core terms.
3. Add synonyms, acronyms, translated terms, and local-language variants.
4. Search for higher-level categories, institutions, authors, or standards.
5. Follow citations, linked documents, footnotes, and named datasets.

If searches return too many weak results, narrow in this order:

1. Add exact phrases for named claims, titles, laws, products, or papers.
2. Add source family terms such as `filing`, `guidance`, `dataset`, `standard`,
   `methodology`, `changelog`, `court`, `minutes`, or `working paper`.
3. Restrict by authoritative domains, institutions, jurisdictions, or file
   types.
4. Add date ranges only when freshness or historical sequence matters.
5. Exclude overloaded meanings or unrelated entities.

## Ranking Signals

Rank candidate sources by:

- Authority: source origin, expertise, directness, and institutional role.
- Freshness: whether the source is current enough for the claim.
- Independence: whether sources have separate reporting, data, or authorship
  lineages.
- Completeness: whether the source includes method, data, context, dates, and
  limitations.
- Relevance: whether the source directly addresses the actual question rather
  than an adjacent one.

## Conflict Handling

Do not hide source conflicts. When sources disagree:

1. Separate claims by date, source family, jurisdiction, and evidence type.
2. Check whether later sources supersede earlier ones.
3. Prefer primary sources over summaries when they address the same claim.
4. Treat repeated rewrites of one source lineage as one piece of evidence.
5. Keep unresolved conflicts visible in the investigation plan.

## Counterevidence Planning

For important claims, define what would weaken or overturn the claim before
searching. Look for:

- negative findings, failed replications, corrections, retractions, or denials
- alternative explanations or mechanisms
- scope limits, boundary conditions, exceptions, or subgroup differences
- evidence that a cited source is stale, superseded, dependent, or indirect
- missing primary evidence behind repeated secondary claims

## Evaluation Criteria

For evaluative requests, define criteria before searching. Make vague terms
operational:

- `meaningful`, `material`, or `significant`: specify magnitude, affected
  population, affected process, business line, risk threshold, or decision
  relevance.
- `viable`, `feasible`, or `practical`: separate performance, economics,
  operational constraints, implementation readiness, demand, supply, regulatory
  fit, and execution risk.
- `harmful`, `beneficial`, or `equitable`: identify who is affected, by what
  mechanism, over what time horizon, and compared with what baseline.
- `better` or `worse`: define the benchmark, comparator, prior period, standard,
  or user-stated criterion.

When criteria are missing and materially change the research path, ask a narrow
clarifying question. Otherwise state working criteria internally and test them
against evidence.

## Transferability Checks

Before applying evidence from one setting to another, compare context variables
that could change the conclusion:

- baseline conditions and starting levels
- population, customer, geography, institution, or user mix
- implementation design, incentives, constraints, and enforcement
- market, legal, cultural, infrastructure, technical, or operational context
- time period, maturity stage, and whether evidence is forecasted or observed
- subgroup or distributional effects

Treat evidence as weaker when the source setting and target setting differ on
variables central to the claim.

## Forecasting And Time Horizon

For forward-looking questions:

- separate current evidence from forecast assumptions
- identify baseline trend, plausible mechanisms, leading indicators, and trigger
  events
- distinguish adoption, behavior change, economics, implementation, and second
  order effects
- look for disconfirming indicators and countervailing forces
- lower confidence when the time horizon depends on unobserved behavior,
  unstable regulation, immature technology, or proxy data
