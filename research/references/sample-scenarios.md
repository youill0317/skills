# Sample Scenarios

Use these scenarios to benchmark the research skill itself or to choose
appropriate source-family and QA expectations for professional research.

Each scenario needs a record with framing, source map, candidate table, claim
register, query ledger, lead graph, acceptance tests, red-team findings, and
quality rubric result.

## Scenario Matrix

| Scenario | Required Lanes | Expected Source Families | Common Traps | Pass Signal |
|---|---|---|---|---|
| Current event verification | official/latest, chronology, counterclaim, provenance | official statements, filings/dockets, reputable reporting, archives, corrections | publication date vs event date confusion, stale updates, repeated wire lineage | timeline separates event/publication/update dates and currentness passes |
| Market comparison | market definition, competitor set, pricing, customer evidence, counterevidence | filings, company docs, analyst/report methods, pricing pages, customer/review data, industry datasets | incompatible market definitions, copied estimates, hidden total cost | comparison basis is consistent or exceptions are explicit |
| Policy/legal landscape | jurisdiction matrix, governing source, pending rules, enforcement, applicability | statutes, regulations, agency guidance, dockets, enforcement records, court orders | treating guidance as binding, missing effective dates, wrong jurisdiction | each jurisdiction has authority/status/effective/applicability notes |
| Academic literature review | database search, inclusion/exclusion, full-text methods, quality appraisal, citation chasing | scholarly databases, full text, DOI/metadata, registries, retraction sources | abstract-only claims, missing negative studies, review counted as independent | search scope and study quality explain synthesis strength |
| Product/tool recommendation | requirements, current availability, compatibility, security, total cost, alternatives | official docs, changelogs, pricing, advisories, reviews, support/forums, benchmarks | obsolete model/version, regional SKU mismatch, unverified reviews | recommendation maps to criteria and total-cost/risk caveats |
| Disputed claim provenance | source-of-claim, archive, variants, counterclaim, identity | original posts/docs, archives, transcripts, media metadata, official response | screenshot-only evidence, quote drift, translation drift, impersonation | claim wording and lineage are traceable or labeled insufficient |
| Dataset/statistics validation | data source, method, denominator, vintage, comparability, recalculation | official tables/APIs, methodology notes, codebooks, release notes, revisions | denominator mismatch, preliminary data, unit/currency conversion error | number can be reconstructed or limitation is explicit |
| Multilingual local-source research | local-language scout, official local sources, translation check, English coverage comparison | native-script official records, local media, official translation, registries | English-only framing, romanization mismatch, unverified translation | local-language evidence changes or confirms English synthesis |
| Technical/security issue | advisory, affected versions, exploit claim, patch, mitigation, source code/issues | CVE/NVD, vendor advisory, GHSA/OSV, changelog, commits, package registry | exploit rumor, wrong version range, patch not released | affected versions and mitigation are current and directly sourced |
| Internal decision audit | source-of-truth, implementation reality, decision history, customer impact, stale-doc conflict | canonical docs, tickets, repos, configs, BI/support, meeting notes | stale wiki, chat as decision, inaccessible sensitive records mislabeled not found | source hierarchy and access boundaries are explicit |

## Golden / Anti-Pattern Requirements

For each benchmark run, record:

- expected source families
- must-find counterevidence or limitation
- expected confidence label for central claims
- common false-positive or overreach traps
- minimum acceptance tests that must pass
- one good-synthesis example in outline form
- one anti-pattern to avoid

No benchmark is passed merely by producing a long answer. The record must show
that the known traps were actively checked.
