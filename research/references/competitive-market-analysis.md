# Competitive And Market Analysis

Use this reference when research needs to compare organizations, products, markets, strategies, or competitive dynamics. It adapts useful competitive landscape patterns into a domain-agnostic research method.

## Scope First

Do not treat every "competitive analysis" request as the same task. First determine:

- Target: one focal entity with competitors around it, or a side-by-side comparison with no protagonist.
- Competitor set: user-specified, proposed by the agent, or discovered during research.
- Audience and output shape: executive briefing, detailed primer,
  investment-style analysis, product strategy, academic comparison, table,
  deck outline, research memo, spreadsheet, or source map.
- Time horizon: current market, historical evolution, near-term outlook, or scenario planning.

If the competitor set is not specified, propose one and explain inclusion criteria before relying on it.

## Market Landscape Evidence Lanes

For product, industry, or market landscape research, plan separate evidence lanes
when relevant:

- Market sizing: define TAM/SAM/SOM or equivalent scope, geography, segment,
  base year, forecast period, currency, and whether values are revenue, volume,
  users, units, installed base, or spend.
- Competitor claims: capture the exact claim, source it to the original company
  or representative, and verify with independent evidence where possible.
- Pricing and packaging: compare public list prices, contract ranges, usage
  units, discounting signals, free tiers, procurement notes, and hidden
  implementation or switching costs. For purchase or recommendation research,
  also check subscriptions, consumables, accessories, required licenses,
  maintenance, support, warranty extensions, taxes, shipping, depreciation or
  resale value, cancellation terms, upgrade paths, and lock-in.
- Customer behavior: separate stated preferences from observed behavior using
  reviews, app-store data, support forums, surveys, churn/retention disclosures,
  procurement records, usage data, or buyer interviews. For public reviews,
  forums, social media, app stores, support threads, and community posts, check
  sampling bias, incentives/manipulation, duplicate or coordinated posts,
  denominator visibility, geography/language/product-version mix, and
  representativeness. Treat these sources as leads or qualitative examples
  unless the claim is specifically about those channels or is triangulated with
  stronger behavioral or method-disclosed evidence.
- Analyst and industry reports: record publisher, sponsor, methodology, sample,
  market definition, base year, forecast assumptions, and whether figures are
  copied from the same estimate lineage.
- Hiring and product signals: use job posts, roadmap notes, changelogs, patents,
  docs, release notes, integrations, and repository activity as directional
  signals, not proof of shipped capability or revenue.
- Regulatory constraints: identify governing jurisdictions, active rules,
  pending rules, standards, enforcement history, licensing, data restrictions,
  and compliance costs.
- Strategic uncertainty: list assumptions, known unknowns, trigger events,
  disconfirming indicators, and confidence by claim.

Batch scout and target searches across lanes before snowballing. Merge early
findings, then snowball only the lanes that affect the decision, comparison, or
important claims. Stop each lane independently only after its evidence need is
satisfied or explicitly blocked by unavailable sources.

## Open-Source And Community Project Health

For public OSS or community project evaluation, assess:

- maintainers and governance: maintainer count, bus factor, organization or
  foundation backing, decision process, code of conduct, and contribution policy
- release health: release cadence, changelog quality, semantic versioning,
  long-term support policy, deprecations, and compatibility promises
- issue and PR process: triage responsiveness, stale issue volume, maintainer
  responses, review latency, merged PR rate, and release linkage
- security posture: security policy, advisories, CVE/GHSA/OSV records,
  dependency update behavior, disclosure process, and patched-version clarity
- adoption and ecosystem: downstream dependencies, integrations, package
  downloads, forks, community channels, docs/tutorials, and examples
- sustainability: funding, sponsors, commercial backing, contributor diversity,
  licensing, trademark constraints, governance disputes, and abandonment signals

Treat stars, forks, downloads, and issue counts as directional signals, not
direct evidence of quality or sustainability.

## Evidence Standards

Prefer comparable evidence across all entities:

- Same fiscal/calendar period when using metrics.
- Same metric definitions, with caveats when definitions differ.
- Same geography or segment unless the comparison intentionally differs.
- Original or primary sources where possible.
- Clear source labels for estimates and private-company data.

When sources conflict, prefer this order unless the domain suggests a better hierarchy:

1. Primary filings, annual reports, audited disclosures, official datasets.
2. Company presentations, product docs, earnings calls, official announcements.
3. Reputable industry reports and analyst research.
4. Trade press and specialist media.
5. General news for recent developments, verified against stronger sources.

Never leave missing data blank. Use `N/A`, `not disclosed`, or `estimate`, and explain why.

For analyst reports, market-size estimates, and private-company metrics:

- Capture the exact definition, base year, geography, segment, unit, currency,
  and forecast period.
- Check whether the report discloses methodology, sample, model assumptions,
  sponsor, and update date.
- Treat precise numbers as low-confidence when methodology is opaque or the
  estimate appears across repeated secondary lineages.
- Prefer ranges or directional language when estimates disagree or source
  methods are not comparable.
- Do not average incompatible market-size estimates unless definitions and
  periods match.

## Analysis Process

1. Identify the 3-5 metrics or dimensions the industry actually runs on.
2. Establish market context: size, growth, drivers, headwinds, constraints, technology shifts, and buyer behavior.
3. Map industry economics: value chain, ecosystem participants, consolidation dynamics, network effects, or scale effects.
4. Profile the target and peers with consistent metric and qualitative categories.
5. Choose a positioning lens: 2x2 matrix, radar, tier diagram, value-chain map, or ecosystem map.
6. Synthesize durable advantages, structural vulnerabilities, current state versus trajectory, and implications for the user's decision.

Common metric examples:

| Industry | Key metrics |
|---|---|
| SaaS | ARR, NRR, CAC payback, LTV/CAC, Rule of 40 |
| Marketplaces | GMV, take rate, liquidity, repeat rate, supply/demand balance |
| Payments | Volume, take rate, attach rate, transaction margin |
| Retail | Same-store sales, inventory turns, margin, sales per square foot |
| Logistics | Volume, cost per unit, on-time delivery, network utilization |

If the industry is not listed, infer metrics from how operators, buyers, regulators, or researchers evaluate success.

## Output Quality Checks

- User-specified competitors, years, metrics, and wording are preserved exactly.
- Every comparison uses the same basis or flags exceptions explicitly.
- Key claims have citations or source notes.
- Estimated values are visibly marked as estimates.
- Tables are complete: no silent omissions.
- Major uncertainties, assumptions, and disconfirming signals are listed
  explicitly.
- Regulatory, pricing, demand, and product-signal claims have confidence labels
  when they affect strategic conclusions.
- Insight headings state findings, not topics.
- The final synthesis answers "so what?" for the intended audience.
