#!/usr/bin/env python3
"""Generate a maximum-saturation research lane and worker-wave plan.

This script does not access the network and does not write artifacts. It emits
Markdown seed sections that the agent integrates into the single research
record before source discovery.
"""

from __future__ import annotations

import argparse
import re
import unicodedata


BASE_LANES = [
    (
        "official-primary",
        "authoritative-record",
        "official docs, governing records, filings, standards, releases",
        "rebuttal, correction, supersession, denial",
    ),
    (
        "currentness",
        "historical-timeline",
        "latest updates, changelogs, advisories, dockets, status pages",
        "superseded, deprecated, withdrawn, changed, stale",
    ),
    (
        "source-lineage",
        "claim-provenance",
        "original sources, citations, archives, syndication chains",
        "duplicate lineage, mirror, excerpt, misquote",
    ),
    (
        "frontier-expansion",
        "lead-expansion",
        "citations, authors, institutions, datasets, methods, repositories, issues, dockets, standards, successors, corrections",
        "duplicate lineage, low-value lead, unable to change claim, blocked lead",
    ),
    (
        "blocked-source-recovery",
        "source-retrieval",
        "archives, mirrors, PDFs, APIs, transcripts, repository history, cached copies, cited excerpts",
        "paywall, login wall, dead link, script-only source, inaccessible primary source",
    ),
    (
        "counterevidence",
        "counterevidence",
        "negative cases, criticisms, rebuttals, failed replications, limits",
        "alternative explanation, contradiction, limitation, exception",
    ),
    (
        "method-data",
        "method-quality",
        "datasets, methodology notes, codebooks, benchmarks, surveys",
        "denominator, sample, uncertainty, revision, comparability",
    ),
    (
        "expert-secondary",
        "expert-interpretation",
        "peer-reviewed papers, expert reports, institutional analysis",
        "dissenting expert, limitation, outdated review",
    ),
    (
        "implementation-oss",
        "implementation-detail",
        "source code, repositories, package registries, releases, issues",
        "bug, advisory, deprecation, abandoned, incompatible",
    ),
    (
        "observed-behavior",
        "observed-behavior",
        "forums, reviews, support threads, adoption signals, complaints",
        "selection bias, astroturfing, isolated anecdote, stale thread",
    ),
    (
        "comparative-benchmark",
        "comparative-benchmark",
        "peer baselines, alternatives, rankings, standards, prior periods",
        "non-comparable baseline, different population, proxy mismatch",
    ),
    (
        "transferability",
        "transferability",
        "local constraints, context variables, boundary conditions",
        "different geography, population, incentives, maturity, regulation",
    ),
]


DOMAIN_LANES = {
    "academic": [
        (
            "scholarly-full-text",
            "expert-interpretation",
            "full-text papers, methods, appendices, replication material",
            "failed replication, retraction, erratum, limitation",
        ),
    ],
    "policy": [
        (
            "legal-regulatory",
            "authoritative-record",
            "laws, regulations, guidance, dockets, enforcement, comments",
            "pending rule, supersession, jurisdiction limit, nonbinding guidance",
        ),
    ],
    "market": [
        (
            "market-competitive",
            "comparative-benchmark",
            "competitors, pricing, adoption, market data, procurement signals",
            "vendor bias, proxy metric, stale estimate, hidden segment",
        ),
    ],
    "technical": [
        (
            "technical-docs",
            "implementation-detail",
            "official docs, API reference, specs, changelogs, migration guides",
            "unsupported version, deprecated path, breaking change, issue",
        ),
    ],
    "security": [
        (
            "security-risk",
            "counterevidence",
            "CVEs, advisories, exploit notes, mitigations, incident reports",
            "false positive, patched version, severity dispute, affected scope",
        ),
    ],
    "profile": [
        (
            "identity-profile",
            "profile-identity",
            "official profiles, registries, IDs, affiliations, archives",
            "name collision, outdated affiliation, impersonation, misattribution",
        ),
    ],
}


def split_csv(value: str | None) -> list[str]:
    if not value:
        return []
    return [part.strip() for part in value.split(",") if part.strip()]


def clean(value: str) -> str:
    return " ".join(value.split())


def slug(value: str) -> str:
    ascii_text = (
        unicodedata.normalize("NFKD", value)
        .encode("ascii", "ignore")
        .decode("ascii")
        .lower()
    )
    return re.sub(r"[^a-z0-9]+", "-", ascii_text).strip("-") or "lane"


def lane_rows(domains: list[str]) -> list[tuple[str, str, str, str]]:
    rows = list(BASE_LANES)
    for domain in domains:
        rows.extend(DOMAIN_LANES.get(domain.lower(), []))

    deduped: list[tuple[str, str, str, str]] = []
    seen: set[str] = set()
    for row in rows:
        if row[0] in seen:
            continue
        seen.add(row[0])
        deduped.append(row)
    return deduped


def print_search_matrix(
    topic: str,
    entities: list[str],
    jurisdictions: list[str],
    languages: list[str],
    domains: list[str],
) -> None:
    entity_text = ", ".join(entities) if entities else "topic entities and aliases"
    jurisdiction_text = ", ".join(jurisdictions) if jurisdictions else "global / applicable jurisdictions"
    language_text = ", ".join(languages) if languages else "English plus discovered local terms"

    print("## Search Matrix")
    print()
    print("| Lane | Claim / Subquestion | Evidence Need | Source Families | Query / Path Patterns | Counter-Search | Final Status |")
    print("|---|---|---|---|---|---|---|")
    for index, (name, evidence_need, source_families, counter) in enumerate(lane_rows(domains), start=1):
        lane = f"L{index:02d}-{slug(name)}"
        query_pattern = (
            f"topic={topic}; entities={entity_text}; jurisdictions={jurisdiction_text}; "
            f"languages={language_text}; source-family={name}"
        )
        subquestion = f"Evidence for {name} lane"
        print(
            f"| {lane} | {subquestion} | {evidence_need} | {source_families} | "
            f"{query_pattern} | {counter} | planned |"
        )
    print()
    print("Resolve every Search Matrix lane to complete, blocked, superseded, or not applicable before final validation.")
    print()


def print_evidence_maturity_dashboard_seed() -> None:
    print("## Evidence Maturity Dashboard")
    print()
    print("| Maturity ID | Item | Type | Linked Claims / Questions | Required Gate Cluster | Current Maturity | Blocking Debt / Weakest Link | Decision / Synthesis Effect |")
    print("|---|---|---|---|---|---|---|---|")
    print("| EM1 | central answer | final answer | C1 / Q1 | search, source, verification, synthesis, decision | blocked | D1 / unresolved source family / failed gate | no firm conclusion until maturity improves |")
    print()

def print_decision_usefulness_seed() -> None:
    print("## Decision Usefulness Matrix")
    print()
    print("| Decision / Use Case | Options / Actions | Criteria | Evidence Link | Risks / Tradeoffs | What Would Change This | Status |")
    print("|---|---|---|---|---|---|---|")
    print("| not applicable until decision framing is identified | not applicable | not applicable | C1 | unresolved evidence, coverage debt, or confidence limits | clearer user decision, stronger evidence, resolved debt, changed currentness | not applicable |")
    print()


def print_comparison_evaluation_seed() -> None:
    print("## Comparison And Evaluation Audit")
    print()
    print("| Evaluation ID | Options / Entities | Criteria / Axes | Weight / Priority | Evidence Links | Missing / Non-Comparable Data | Tradeoffs / Sensitivity | Status | Decision Effect |")
    print("|---|---|---|---|---|---|---|---|---|")
    print("| EV1 | not applicable until comparison or recommendation framing is identified | not applicable | not applicable | C1 / S1 / O1 / D1 | not applicable | AS1 / none | not applicable | no recommendation |")
    print()

def print_question_coverage_seed() -> None:
    print("## Question Coverage Audit")
    print()
    print("| Question ID | User Need / Subquestion | Answer Status | Evidence / Claim Links | Residual Gap | Final Answer Location |")
    print("|---|---|---|---|---|---|")
    print("| Q1 | primary user request and deliverable requirements | unanswered | C1 / D1 | replace with decomposed subquestions, comparison axes, constraints, and coverage gaps | Answer / Key Findings / Open Questions |")
    print()
    print("Resolve every unanswered question coverage row to answered, partially answered, blocked, out of scope, or not applicable before final validation.")
    print()


def print_tool_capability_seed() -> None:
    print("## Tool Capability Audit")
    print()
    print("| Capability | Status | Use / Reason | Limits / Fallback | Record Impact |")
    print("|---|---|---|---|---|")
    rows = [
        "web search",
        "batch / parallel diversified search",
        "source open / fetch",
        "in-source find / extraction",
        "connectors / databases",
        "local files / code search",
        "repository / package access",
        "archive / browser fallback",
        "source retrieval fallback",
        "document/PDF/table extraction",
        "subagents / parallel lanes",
    ]
    for capability in rows:
        print(f"| {capability} | planned | use if available for this research need | record limits and fallback | update relevant record sections |")
    print()
    print("Resolve every planned capability row to used, blocked, unavailable, or not applicable before final validation.")
    print()


def print_diversified_search_batch_seed() -> None:
    print("## Diversified Search Batch Plan")
    print()
    print("When the active search harness supports batched queries, seed source-family portfolios with:")
    print()
    print("`python research/scripts/query_matrix.py --topic \"<topic>\" --format batches --batch-size <tool-limit>`")
    print()
    print("Preserve generated query counts, `SB1` / `SB2` execution sub-batches, and numeric tool-limit notes in the Purpose column.")
    print()
    print("| Batch | Source Families To Mix | Purpose | Record Integration |")
    print("|---|---|---|---|")
    print("| B1 | scout / official-primary / pdf-document / dataset-method | execute source-of-truth discovery queries as sub-batches of up to tool-limit; SB1: scout and official-primary; SB2: pdf-document and dataset-method | Search Craft Log / Search Result Triage / Saturation Metrics |")
    print("| B2 | currentness / counterevidence / source-lineage / provenance-archive | execute freshness, contradiction, and upstream-origin queries as sub-batches of up to tool-limit; SB1: currentness and counterevidence; SB2: source-lineage and provenance-archive | Currentness And Version Audit / Source Lineage Map / Absence Evidence Audit |")
    print("| B3 | frontier-expansion / blocked-source-recovery / scholarly / github-oss / implementation-code | execute lead-expansion and blocked-source-recovery queries as sub-batches of up to tool-limit; SB1: frontier-expansion and blocked-source-recovery; SB2: scholarly, github-oss, and implementation-code | Lead Ledger / Expansion Frontier Audit / Access And Retrieval Audit / Coverage Debt |")
    print("| B4+ | unresolved source families and highest-impact open leads | execute coverage-debt clearing queries as sub-batches of up to tool-limit; SB1: unresolved source families; SB2: highest-impact open leads | Saturation Metrics / Stop Rule Audit / Evidence Maturity Dashboard |")
    print()


def print_worker_waves() -> None:
    print("## Worker Wave Plan")
    print()
    print("| Wave | Purpose | Lanes / Passes | Execution | Completion Criteria |")
    print("|---|---|---|---|---|")
    print("| W0 | framing and query matrix | scope, evidence needs, source families, false positives, stop gates | main agent | record initialized; search matrix, query seeds, and acceptance gates present |")
    print("| W1 | scout | broad source-family discovery across independent lanes | parallel if available / sequential fallback | vocabulary, aliases, source families, false positives, and seed sources identified |")
    print("| W2 | target and snowball | official, primary, scholarly, dataset, repository, archive, and expert seeds | parallel if available / sequential fallback | source bodies inspected; citations, methods, datasets, issues, and updates extracted |")
    print("| W3 | EXPAND, counter-search, currentness, provenance, gap pass | follow leads, test negations, check latest state, trace lineage, close gaps | parallel if available / sequential fallback | frontier queue converged; high-value leads followed or closed; coverage debt updated |")
    print("| W4 | verification and synthesis-overreach | claim audit, source audit, currentness audit, lineage audit, contradiction/gap audit, overreach audit | parallel if available / sequential fallback | important claims supported, downgraded, excluded, or marked insufficient |")
    print()


def print_domain_coverage_seed() -> None:
    print("## Domain Coverage Matrix")
    print()
    print("| Domain / Protocol | Applicability | Required Source Families | Status | Notes / Exclusions |")
    print("|---|---|---|---|---|")
    rows = [
        ("official / primary", "governing records, official docs, filings, standards, releases"),
        ("currentness / latest state", "changelogs, advisories, dockets, status pages, latest official updates"),
        ("scholarly / academic", "full text, methods, literature reviews, replication, citations"),
        ("data / statistics / methods", "datasets, methodology notes, codebooks, uncertainty, denominators"),
        ("legal / regulatory / policy", "laws, regulations, guidance, enforcement, comments, effective dates"),
        ("market / competitive / product", "competitors, pricing, adoption, reviews, procurement, availability"),
        ("technical / OSS / implementation", "docs, source code, issues, releases, package registries, advisories"),
        ("security / safety / risk", "advisories, incidents, CVEs, mitigations, risk disclosures"),
        ("provenance / identity / archives", "original sources, archives, registries, profiles, citations, lineage"),
        ("public sentiment / behavior", "forums, reviews, support threads, complaints, observed behavior"),
    ]
    for domain, families in rows:
        print(f"| {domain} | uncertain | {families} | planned | mark covered, blocked, or not applicable before synthesis |")
    print()
    print("Resolve every planned domain row to searched, covered, blocked, or not applicable before final validation.")
    print()


def print_language_locale_seed(languages: list[str], jurisdictions: list[str]) -> None:
    print("## Language And Locale Audit")
    print()
    print("| Locale / Language | Applicability | Native Terms / Aliases | Local Source Families | Status | Confidence Impact |")
    print("|---|---|---|---|---|---|")
    language_text = ", ".join(languages) if languages else "English plus discovered local terms"
    jurisdiction_text = ", ".join(jurisdictions) if jurisdictions else "global / applicable jurisdictions"
    print(f"| {jurisdiction_text} / {language_text} | uncertain | native terms, aliases, spellings, scripts, translations | local official, local media, registries, databases, forums, archives | planned | downgrade local or translated claims if blocked |")
    print()
    print("Resolve every planned language/locale row to searched, covered, blocked, or not applicable before final validation.")
    print()


def print_entity_terminology_seed(
    topic: str,
    entities: list[str],
    languages: list[str],
) -> None:
    print("## Entity And Terminology Audit")
    print()
    print("| Entity / Term | Ambiguity Risk | Included Identifiers / Aliases | Exclusion Terms / Lookalikes | Verification Sources | Status | Confidence Effect |")
    print("|---|---|---|---|---|---|---|")
    entity_text = ", ".join(entities) if entities else topic
    language_text = ", ".join(languages) if languages else "English plus discovered native/local terms"
    print(f"| {entity_text} | name collision / acronym / translation / version / jurisdiction / concept drift / false positive | official names, IDs, versions, aliases, native terms, repositories, packages | lookalikes, adjacent meanings, unrelated acronyms, wrong versions, wrong jurisdictions | official source family / S1 when inspected | blocked | insufficient until disambiguated across {language_text} |")
    print()


def print_search_result_triage_seed() -> None:
    print("## Search Result Triage")
    print()
    print("| Result ID | Lane / Query | Result / URL / Path | Classification | Reason | Follow-Up |")
    print("|---|---|---|---|---|---|")
    print("| R1 | W0 planning | search result triage seed | lead | replace with meaningful search results; only opened or retrieved sources become evidence | add source, lead, duplicate-lineage, context-only, or dead-end decision |")
    print()


def print_lead_ledger_seed() -> None:
    print("## Lead Ledger")
    print()
    print("| Lead ID | Raised From | Lead | Why It Matters | Action | Outcome |")
    print("|---|---|---|---|---|---|")
    print("| LD1 | W1 / S1 / L2 | source, citation, dataset, method, issue, counterclaim, or blocked source | could change C1 / close source-family gap | followed | source found, no result, claim downgraded, or blocked with reason |")
    print()
    print("Close every material lead as followed, duplicate, blocked, low-quality, out-of-scope, or not applicable before final validation.")
    print()


def print_expansion_frontier_seed() -> None:
    print("## Source-Opened Follow-Up Audit")
    print()
    print("| Follow-Up ID | Source / Observation | Extracted Lead | Lead Type | Follow-Up Search / Connector Path | Action | Outcome / Confidence Effect |")
    print("|---|---|---|---|---|---|---|")
    print("| SOF1 | S1 / O1 | citation, author, dataset, identifier, native term, correction, counterclaim, blocked source, or none | citation / author / dataset / identifier / native term / correction / counterclaim / blocked source / none | query, connector path, archive path, repository path, or not applicable | unresolved | insufficient until source-opened leads are followed, closed, blocked, or downgraded |")
    print()
    print("Before final validation, close every source-opened follow-up row or convert it into Lead Ledger / Expansion Frontier Audit / Coverage Debt.")
    print()
    print("## Expansion Frontier Audit")
    print()
    print("| Frontier ID | Raised From | Seed / Source | Extracted Frontier | Lead Type | Query / Connector Pass | Status | Outcome / Confidence Effect |")
    print("|---|---|---|---|---|---|---|---|")
    print("| EF1 | W1 / S1 / R1 / LD1 | seed source, citation, author, dataset, method, entity, alias, docket, package, issue, review, counterclaim | citations, authors, datasets, aliases, methods, updates, corrections, successors, counterclaims, co-citations | source | query, connector path, snowball pass, EXPAND pass, archive path, repository path, database path, or blocked reason | planned | no confidence increase until frontier is searched, closed, blocked, or downgraded |")
    print()
    print("Resolve every planned expansion frontier row to searched, followed, duplicate-lineage, low-quality, blocked, out-of-scope, or not applicable before final validation.")
    print()


def print_search_bias_trap_seed() -> None:
    print("## Search Bias And Retrieval Trap Audit")
    print()
    print("| Trap ID | Lane / Query / Source Family | Potential Trap | Diagnostic Check | Mitigation / Alternate Path | Evidence / Follow-Up Links | Status | Confidence Effect |")
    print("|---|---|---|---|---|---|---|---|")
    print("| SB1 | L1 / query / source family | ranking bias, SEO/sponsored result, snippet or AI-overview leakage, duplicate lineage, language/locality mismatch, query bias, personalization, paywall, corpus gap, stale index, or platform filter | compare against official, primary, local-language, domain-limited, counter-search, exact-title, archive, database, or beyond-top-rank results | alternate query/source path and mitigation | R1 / S1 / LD1 / D1 | blocked | insufficient until material search-bias traps are mitigated or bounded |")
    print()

def print_selection_inclusion_seed() -> None:
    print("## Selection And Inclusion Audit")
    print()
    print("| Evidence Set | Inclusion Criteria | Exclusion / Downrank Criteria | Included Sources | Excluded / Downranked Results | Selection Risk | Mitigation | Status | Confidence Effect |")
    print("|---|---|---|---|---|---|---|---|---|")
    print("| source family evidence set | include inspected, relevant, non-duplicate-lineage sources that can affect important claims | exclude or downrank wrong target, stale, inaccessible, duplicate-lineage, low-quality, snippet-only, or weak-method results | S1 | R1 / LD1 | cherry-pick / survivorship / convenience / language / paywall / ranking / none | counter-search, source-family balance, transparent cut, independent lineage, caveat | incomplete | insufficient until inclusion/exclusion criteria are applied |")
    print()


def print_access_retrieval_seed() -> None:
    print("## Access And Retrieval Audit")
    print()
    print("| Retrieval ID | Target Source / Lead | Primary Access Path | Alternate Paths Tried | Retrieval Status | Evidence Use | Confidence Impact |")
    print("|---|---|---|---|---|---|---|")
    print("| AR1 | S1 / LD1 | direct URL, connector, repository, or database | archive, PDF, API, browser, mirror, package registry, cached copy, cited excerpt | blocked | lead only until retrieved | downgrade affected claims if blocked |")
    print()


def print_coverage_debt_seed() -> None:
    print("## Coverage Debt")
    print()
    print("| Debt ID | Raised From | Gap / Missing Coverage | Why It Matters | Follow-Up Owner / Pass | Status | Confidence Effect |")
    print("|---|---|---|---|---|---|---|")
    print("| D1 | W0 | coverage debt seed | replace with thin lanes, blocked source bodies, unfollowed leads, missing source families, stale claims, weak provenance, or unresolved contradictions | main agent | open | unresolved debt lowers affected claim confidence |")
    print()
    print("Resolve every open coverage debt row to cleared, blocked, downgraded, or not applicable before final validation.")
    print()


def print_source_lineage_seed() -> None:
    print("## Source Lineage Map")
    print()
    print("| Lineage ID | Upstream Source / Origin | Member Sources | Independence Status | Claims Affected | Notes |")
    print("|---|---|---|---|---|---|")
    print("| G1 | source lineage seed | S1 | unclear | C1 | replace with upstream origins before counting sources as independent |")
    print()


def print_source_quality_seed() -> None:
    print("## Source Quality Audit")
    print()
    print("| Source ID | Authority | Directness | Currentness | Method / Data Quality | Lineage | Overall Status | Confidence Effect |")
    print("|---|---|---|---|---|---|---|---|")
    print("| S1 | unknown | indirect | unknown | opaque | unclear | weak | downgrade until source body, method, currentness, and lineage are audited |")
    print()


def print_corroboration_triangulation_seed() -> None:
    print("## Corroboration And Triangulation Audit")
    print()
    print("| Claim ID | Primary / Governing Support | Independent Corroboration | Counterevidence / Limitation | Method / Data Check | Lineage Diversity | Status | Confidence Effect |")
    print("|---|---|---|---|---|---|---|---|")
    print("| C1 | none | none | not searched | not applicable | unclear | blocked | insufficient until primary/governing support, independent corroboration or source-of-truth exception, counterevidence, and relevant method/data checks are recorded |")
    print()


def print_consensus_disagreement_seed() -> None:
    print("## Consensus And Disagreement Audit")
    print()
    print("| Consensus ID | Claim / Question | Source Community / Field | Consensus Signal | Disagreement / Minority View | Evidence Links | Recency / Scope Limits | Status | Confidence Effect |")
    print("|---|---|---|---|---|---|---|---|---|")
    print("| CN1 | C1 / Q1 | relevant field, expert community, regulator, standards body, literature, market, maintainer group, or affected users | guideline, review, meta-analysis, standard, official position, repeated independent findings, or market evidence | dissent, minority view, unresolved split, failure case, fringe claim, or none found | C1 / S1 / G1 / O1 / D1 | timeframe, jurisdiction, population, version, method, or source-family limit | unclear | insufficient until consensus and disagreement are audited |")
    print()

def print_source_incentive_bias_seed() -> None:
    print("## Source Incentive And Bias Audit")
    print()
    print("| Source / Lineage | Incentive / Bias Risk | Funding / Affiliation / Stake | Disclosure Status | Mitigation / Corroboration | Status | Confidence Effect |")
    print("|---|---|---|---|---|---|---|")
    print("| S1 / G1 | vendor / advocacy / political / regulatory / academic / self-report / affiliate / publication bias / none / unknown | funder, employer, sponsor, seller, regulator, advocacy group, author stake, or unknown | disclosed / undisclosed / unclear / not applicable | independent source, primary record, counter-search, method audit, or caveat | unknown | downgrade until incentives and corroboration are audited |")
    print()


def print_source_manipulation_provenance_seed() -> None:
    print("## Source Manipulation And Adversarial Provenance Audit")
    print()
    print("| Manipulation ID | Source / Claim / Community | Manipulation Risk | Authenticity / Provenance Check | Coordination / Amplification Check | Safety / Injection Check | Evidence Links | Status | Confidence Effect |")
    print("|---|---|---|---|---|---|---|---|---|")
    print("| MP1 | S1 / C1 / G1 | fabrication, impersonation, account takeover, coordinated amplification, review manipulation, synthetic media, poisoned package/repo, prompt injection, tampered PDF/data, or unclear provenance | original source, stable locator, metadata, history, archive, signature, maintainer identity, filing/docket, or official cross-check | account age, posting pattern, syndication, duplicate content, bot/amplification signal, review burst, or not applicable | untrusted code/script, hidden prompt, external instruction, active content, install/execute risk, or not applicable | S1 / C1 / G1 / O1 / LD1 / D1 | blocked | insufficient until manipulation and adversarial provenance risks are checked |")
    print()

def print_quantitative_measurement_seed() -> None:
    print("## Quantitative And Measurement Audit")
    print()
    print("| Claim / Metric | Value | Unit / Denominator | Population / Scope | Period / Vintage | Method / Source | Uncertainty / Comparability | Status | Confidence Effect |")
    print("|---|---|---|---|---|---|---|---|---|")
    print("| C1 / metric | value or not applicable | unit, denominator, base, currency, or rank base | population, geography, segment, product, or jurisdiction | date, period, release, revision, or vintage | source, method, dataset, benchmark, or survey | margin, sample, proxy, non-comparable baseline, or caveat | blocked | quantitative claims remain insufficient until measurement details are audited |")
    print()


def print_saturation_metrics_seed() -> None:
    print("## Saturation Metrics")
    print()
    print("| Metric | Target / Floor | Actual | Status | Evidence / Record Link | Confidence Effect |")
    print("|---|---|---:|---|---|---|")
    rows = [
        (
            "distinct search queries",
            "at least 10 per important web lane when web search exists",
        ),
        (
            "inspected relevant sources or records",
            "12+ narrow, 25+ broad, 50+ very broad when sources exist",
        ),
        (
            "expansion waves",
            "at least two broad EXPAND waves; three no-new-lead waves for very broad convergence",
        ),
        (
            "frontier queue convergence",
            "latest EXPAND or gap cycle yields no new high-value leads, or remaining material leads are closed, blocked, duplicate-lineage, out of scope, low quality, or confidence-downgraded",
        ),
        (
            "counter-search passes",
            "every central claim gets negation, rebuttal, limitation, or supersession search",
        ),
        (
            "local-language or jurisdictional sweeps",
            "required when language, locale, policy, identity, market, or local facts matter",
        ),
        (
            "material high-value leads closed",
            "all material LD rows followed, closed, blocked, or tied to confidence downgrade",
        ),
    ]
    for metric, target in rows:
        print(f"| {metric} | {target} | 0 | blocked | not run yet | insufficient until executed |")
    print()


def print_currentness_version_seed() -> None:
    print("## Currentness And Version Audit")
    print()
    print("| Claim / Source | Currentness Need | Evidence Date / Version | Latest / Supersession Check | Status | Confidence Effect |")
    print("|---|---|---|---|---|---|")
    print("| C1 / S1 | current | unknown | blocked until latest/supersession check runs | unknown | current-dependent claims remain insufficient until checked |")
    print()


def print_reproducibility_refresh_seed() -> None:
    print("## Reproducibility And Refresh Audit")
    print()
    print("| Item | Reproduction Path | Stable Locator / Version | Volatility / Refresh Trigger | Last Checked | Refresh Action | Status | Confidence Effect |")
    print("|---|---|---|---|---|---|---|---|")
    print("| whole record / C1 / S1 | query, URL, connector path, repo path, API, docket, registry, or dataset path | archive URL, release tag, commit, package version, dataset vintage, report edition, docket ID, table ID, or not yet stable | price / policy / version / law / dataset / market / status / mutable page changes | not checked yet | rerun search, reopen source, check changelog, refresh dataset, or compare new version | blocked | insufficient until rerun path and refresh trigger are recorded |")
    print()


def print_evidence_location_seed() -> None:
    print("## Evidence Location Audit")
    print()
    print("| Claim / Observation | Source ID | Required Locator | Locator Present? | Location Detail | Confidence Effect |")
    print("|---|---|---|---|---|---|")
    print("| C1 / O1 | S1 | page / section / table / line / timestamp / field / tag / issue / docket | no | add exact source location before firm synthesis | insufficient until location is recorded |")
    print()


def print_quotation_context_seed() -> None:
    print("## Quotation And Context Audit")
    print()
    print("| Quote / Passage | Source ID | Speaker / Author | Location | Context Checked | Translation / Paraphrase Risk | Claim Fit | Status | Confidence Effect |")
    print("|---|---|---|---|---|---|---|---|---|")
    print("| C1 / O1 | S1 | speaker, author, institution, or unknown | exact source location | full context, surrounding section, original language, thread, or method context | unresolved | context missing until checked | unresolved | insufficient until quotation context is audited |")
    print()


def print_absence_evidence_seed() -> None:
    print("## Absence Evidence Audit")
    print()
    print("| Claim / Question | Search Boundary | Source Families Checked | Absence Result | Inference Allowed | Confidence Effect |")
    print("|---|---|---|---|---|---|")
    print("| C1 | scope, dates, languages, jurisdictions, repositories, databases, archives, and source systems searched | official / primary / dataset / scholarly / archive / local-language / repository / counter-search | blocked | no absence inference until expected source families are searched or blocked with reason | insufficient until bounded |")
    print()


def print_claim_risk_triage_seed() -> None:
    print("## Claim Risk Triage")
    print()
    print("| Claim ID | Decision Impact | Error Risk | Verification Priority | Required Checks | Escalation / Downgrade Rule |")
    print("|---|---|---|---|---|---|")
    print("| C1 | high | high | high | primary source, counter-search, currentness, lineage, method/data, adversarial review | downgrade or mark insufficient if required checks fail |")
    print()


def print_claim_traceability_seed() -> None:
    print("## Claim Traceability Matrix")
    print()
    print("| Claim ID | Final Decision | Observations | Sources | Lineages | Verification Gates | Counterevidence / Debt | Confidence Effect |")
    print("|---|---|---|---|---|---|---|---|")
    print("| C1 | unresolved | O1 | S1 | G1 | claim/source/currentness/lineage/overreach | D1 | insufficient until traced to inspected evidence |")
    print()
    print("Before final validation, replace unresolved traceability decisions with use, downgrade, exclude, or insufficient.")
    print()


def print_inference_boundary_seed() -> None:
    print("## Inference Boundary Audit")
    print()
    print("| Claim ID | Observation Base | Inference Type | Required Assumptions | Boundary / Not Supported | Status | Confidence Effect |")
    print("|---|---|---|---|---|---|---|")
    print("| C1 | O1 / S1 | direct observation / bounded inference / comparison / extrapolation / causal / forecast / recommendation / speculative | assumptions needed for any inference beyond observation | what the evidence does not support | blocked | insufficient until inference boundary is audited |")
    print()


def print_assumption_sensitivity_seed() -> None:
    print("## Assumption And Sensitivity Audit")
    print()
    print("| Assumption ID | Claim / Decision | Assumption / Variable | Plausible Range / Alternative | Evidence / Test | Sensitivity | Status | Confidence Effect |")
    print("|---|---|---|---|---|---|---|---|")
    print("| AS1 | C1 / decision | threshold, market definition, scope, timeframe, denominator, benchmark, jurisdiction, version, risk tolerance, or constraint | plausible alternative or scenario | S1 / O1 / D1 | high | untested | insufficient until decision-changing assumptions are tested, bounded, or surfaced as caveats |")
    print()


def print_conflict_resolution_seed() -> None:
    print("## Conflict Resolution Matrix")
    print()
    print("| Conflict ID | Claims / Observations | Conflict Type | Evidence On Each Side | Adjudication Basis | Resolution | Confidence Effect |")
    print("|---|---|---|---|---|---|---|")
    print("| CF1 | C1 / O1 | none until conflicts are found | no material conflict checked yet | authority, directness, currentness, method, lineage, scope, retrieval quality | unresolved | insufficient until material conflicts are checked or marked not applicable |")
    print()


def print_confidence_calibration_seed() -> None:
    print("## Confidence Calibration")
    print()
    print("| Claim ID | Evidence Strength | Consistency | Directness | Currentness | Lineage Independence | Method / Data Quality | Counterevidence / Debt | Calibrated Confidence | Rationale |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    print("| C1 | weak | unresolved | indirect | unknown | unclear | opaque | D1 | insufficient | upgrade only after inspected evidence, independent lineage, currentness, and counterevidence gates support it |")
    print()


def print_synthesis_traceability_seed() -> None:
    print("## Synthesis Traceability Audit")
    print()
    print("| Output Item | Final Section | Claim Links | Evidence / Source Links | Confidence | Unresolved Limits / Debt | Status | Required Revision |")
    print("|---|---|---|---|---|---|---|---|")
    print("| ST1 | Answer / Key Findings | C1 | S1 / O1 | insufficient | D1 | blocked | keep final synthesis caveated until traceability passes |")
    print()


def print_adversarial_review_seed() -> None:
    print("## Adversarial Review")
    print()
    print("| Review ID | Claim / Finding Challenged | Challenge | Evidence Checked | Result | Outcome | Synthesis Effect |")
    print("|---|---|---|---|---|---|---|")
    print("| A1 | C1 | strongest counterclaim, missing source family, incentive bias, method weakness, stale evidence, or transferability limit | counter-search, source quality audit, coverage debt, and lineage map | unresolved until checked | unresolved | keep claim insufficient or downgrade until challenge is resolved |")
    print()


def print_stop_rule_audit_seed() -> None:
    print("## Stop Rule Audit")
    print()
    print("| Item | Scope | Stop Criteria Checked | Status | Remaining Gap | Confidence Impact |")
    print("|---|---|---|---|---|---|")
    print("| SR1 | whole record | lanes, source families, EXPAND, counter-search, currentness, lineage, quality, traceability, calibration, adversarial review | not satisfied | coverage debt seed remains | insufficient until stop criteria are satisfied or blocked with confidence impact |")
    print()
    print("Resolve every not satisfied stop-rule row to satisfied, blocked, or not applicable before final validation.")
    print()


def print_distortion_audit_seed() -> None:
    print("## Distortion Pattern Audit")
    print()
    print("| Claim / Source | Pattern Checked | Finding | Status | Claim Effect |")
    print("|---|---|---|---|---|")
    print("| C1 / S1 | stale, misattribution, conflation, circular citation, inference upgraded to fact, magnitude drift, quote distortion, translation drift, cherry-pick, survivorship bias | unresolved until primary/source-lineage checks run | unresolved | keep claim insufficient or downgraded until clear |")
    print()


def print_verification_plan() -> None:
    print("## Verification Notes")
    print()
    print("Planned verification lanes before final synthesis:")
    print()
    print("- claim verification audit")
    print("- frontier queue convergence audit")
    print("- source audit")
    print("- currentness audit when claims are date/version dependent")
    print("- contradiction and gap audit")
    print("- source-lineage audit")
    print("- method/data audit when empirical, benchmark, survey, or causal evidence matters")
    print("- verified-claim gate for high-risk non-code claims")
    print("- synthesis-overreach audit")
    print()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", required=True)
    parser.add_argument("--request", default="")
    parser.add_argument("--scope", default="")
    parser.add_argument(
        "--domains",
        default="",
        help="Comma-separated domain hints: academic, policy, market, technical, security, profile",
    )
    parser.add_argument("--entities", default="", help="Comma-separated entities")
    parser.add_argument("--jurisdictions", default="", help="Comma-separated jurisdictions")
    parser.add_argument("--languages", default="", help="Comma-separated languages or native terms")
    args = parser.parse_args()

    topic = clean(args.topic)
    request = clean(args.request) or topic
    scope = clean(args.scope) or "maximum-saturation research with explicit assumptions"
    domains = split_csv(args.domains)
    entities = split_csv(args.entities)
    jurisdictions = split_csv(args.jurisdictions)
    languages = split_csv(args.languages)

    print(f"<!-- Research plan seed for: {topic} -->")
    print(f"<!-- User request: {request} -->")
    print(f"<!-- Scope: {scope} -->")
    print()
    print_evidence_maturity_dashboard_seed()
    print_decision_usefulness_seed()

    print_comparison_evaluation_seed()
    print_question_coverage_seed()
    print_tool_capability_seed()
    print_search_matrix(topic, entities, jurisdictions, languages, domains)
    print_diversified_search_batch_seed()
    print_domain_coverage_seed()
    print_language_locale_seed(languages, jurisdictions)
    print_entity_terminology_seed(topic, entities, languages)
    print_worker_waves()
    print_search_result_triage_seed()
    print_lead_ledger_seed()
    print_search_bias_trap_seed()
    print_expansion_frontier_seed()
    print_selection_inclusion_seed()
    print_access_retrieval_seed()
    print_coverage_debt_seed()
    print_source_lineage_seed()
    print_source_quality_seed()
    print_corroboration_triangulation_seed()
    print_consensus_disagreement_seed()
    print_source_incentive_bias_seed()
    print_source_manipulation_provenance_seed()
    print_quantitative_measurement_seed()
    print_saturation_metrics_seed()
    print_currentness_version_seed()
    print_reproducibility_refresh_seed()
    print_evidence_location_seed()
    print_quotation_context_seed()
    print_absence_evidence_seed()
    print_claim_risk_triage_seed()
    print_claim_traceability_seed()
    print_inference_boundary_seed()
    print_assumption_sensitivity_seed()
    print_conflict_resolution_seed()
    print_confidence_calibration_seed()
    print_synthesis_traceability_seed()
    print_adversarial_review_seed()
    print_stop_rule_audit_seed()
    print_distortion_audit_seed()
    print_verification_plan()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
