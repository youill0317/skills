"""Shared research lane and source-family taxonomy."""

from __future__ import annotations

import re


BASE_LANES = [
    (
        "L1",
        "authoritative baseline",
        "official, primary, governing, standard, filing, documentation",
        "source-of-truth search and direct retrieval",
    ),
    (
        "L2",
        "currentness and supersession",
        "latest official updates, releases, dockets, advisories, status pages",
        "latest/current/version/effective-date search",
    ),
    (
        "L3",
        "independent corroboration",
        "scholarly, expert, dataset, independent reporting, reputable analysis",
        "independent-source search and method inspection",
    ),
    (
        "L4",
        "counterevidence and limits",
        "criticism, failures, retractions, contrary findings, disputes",
        "negative and disagreement search",
    ),
    (
        "L5",
        "provenance and incentives",
        "authors, organizations, funding, archives, source lineage",
        "upstream source and archive search",
    ),
    (
        "L6",
        "frontier expansion",
        "citations, references, related entities, datasets, standards, cases",
        "snowball search from useful sources",
    ),
]


DOMAIN_LANES = {
    "legal": (
        "legal and regulatory applicability",
        "laws, regulations, guidance, enforcement, cases, effective dates",
        "jurisdiction and authority hierarchy search",
    ),
    "policy": (
        "policy and regulatory applicability",
        "laws, regulations, guidance, enforcement, consultations",
        "jurisdiction and authority hierarchy search",
    ),
    "market": (
        "market and competitive evidence",
        "vendors, pricing, adoption, procurement, reviews, benchmarks",
        "market, vendor, and comparison search",
    ),
    "competitive": (
        "competitive landscape",
        "competitors, alternatives, pricing, market share, benchmarks",
        "option and criteria search",
    ),
    "technical": (
        "technical and implementation evidence",
        "docs, source code, repositories, issues, releases, packages",
        "repository and implementation search",
    ),
    "oss": (
        "OSS evidence",
        "source code, maintainers, releases, issues, advisories, forks",
        "repository and package ecosystem search",
    ),
    "security": (
        "security and risk evidence",
        "advisories, incidents, CVEs, mitigations, threat models",
        "advisory, incident, and mitigation search",
    ),
    "scholarly": (
        "scholarly literature evidence",
        "papers, reviews, methods, replication, citations",
        "scholarly database and citation search",
    ),
    "data": (
        "data and measurement evidence",
        "datasets, surveys, methodology, denominators, codebooks",
        "dataset and method search",
    ),
    "statistics": (
        "statistical evidence",
        "datasets, surveys, methodology, denominators, uncertainty",
        "statistics and method search",
    ),
    "identity": (
        "identity and entity disambiguation",
        "profiles, registries, aliases, same-name exclusions, archives",
        "identity verification search",
    ),
    "profile": (
        "profile and entity disambiguation",
        "profiles, registries, aliases, same-name exclusions, archives",
        "identity verification search",
    ),
    "sentiment": (
        "public behavior and sentiment",
        "reviews, forums, complaints, support threads, community reports",
        "public trace and manipulation-aware search",
    ),
    "multilingual": (
        "local-language coverage",
        "native terms, local official sources, local media, local databases",
        "local-language and jurisdiction search",
    ),
    "current": (
        "current-event verification",
        "latest official updates, corrections, denials, timestamped reports",
        "time-bounded latest-status search",
    ),
}


BASE_FAMILIES = [
    "official-primary",
    "currentness",
    "counterevidence",
    "scholarly",
    "data-method",
    "provenance-archive",
    "frontier-expansion",
    "blocked-source-recovery",
]


FAMILY_ALIASES = {
    "official": "official-primary",
    "primary": "official-primary",
    "latest": "currentness",
    "current": "currentness",
    "freshness": "currentness",
    "criticism": "counterevidence",
    "disagreement": "counterevidence",
    "academic": "scholarly",
    "literature": "scholarly",
    "statistics": "data-method",
    "data": "data-method",
    "survey": "data-method",
    "dataset": "data-method",
    "archive": "provenance-archive",
    "provenance": "provenance-archive",
    "lineage": "provenance-archive",
    "expand": "frontier-expansion",
    "snowball": "frontier-expansion",
    "blocked": "blocked-source-recovery",
    "legal": "legal-regulatory",
    "policy": "legal-regulatory",
    "regulatory": "legal-regulatory",
    "market": "market-competitive",
    "competitive": "market-competitive",
    "vendor": "market-competitive",
    "security": "security-risk",
    "risk": "security-risk",
    "oss": "technical-oss",
    "github": "technical-oss",
    "code": "technical-oss",
    "technical": "technical-oss",
    "profile": "identity-profile",
    "identity": "identity-profile",
    "sentiment": "public-sentiment",
    "review": "public-sentiment",
    "multilingual": "local-language",
    "local": "local-language",
}


FAMILY_PATTERNS = {
    "official-primary": [
        "{topic} official",
        "{topic} (site:.gov OR site:.edu OR site:.org)",
        "{topic} (report OR standard OR guidance OR documentation)",
    ],
    "currentness": [
        "{topic} (latest OR updated OR changelog)",
        "{topic} (effective date OR superseded OR revised)",
        "{topic} ({current_year} OR {prior_year})",
    ],
    "counterevidence": [
        "{topic} (criticism OR limitation OR controversy)",
        "{topic} (rebuttal OR correction OR retraction)",
        '{topic} (failure OR risk OR "not supported")',
    ],
    "scholarly": [
        "{topic} (systematic review OR meta-analysis)",
        "{topic} (site:scholar.google.com OR doi)",
        "{topic} (method OR sample OR replication)",
    ],
    "data-method": [
        "{topic} (dataset OR statistics OR survey)",
        "{topic} (methodology OR codebook OR denominator)",
        "{topic} (table OR appendix OR raw data)",
    ],
    "provenance-archive": [
        "{topic} (original source OR primary source)",
        "{topic} (archive OR archived OR cached)",
        "{topic} (author OR funding OR affiliation)",
    ],
    "frontier-expansion": [
        "{topic} (references OR citations OR bibliography)",
        "{topic} (related standard OR related case OR related dataset)",
        '{topic} ("cited by" OR "see also")',
    ],
    "blocked-source-recovery": [
        "{topic} filetype:pdf",
        "{topic} (mirror OR cached OR archive)",
        "{topic} (API OR repository OR docket)",
    ],
    "legal-regulatory": [
        "{topic} (law OR regulation OR statute OR enforcement)",
        "{topic} (guidance OR rulemaking OR consultation)",
        "{topic} (jurisdiction OR applicability OR effective date)",
    ],
    "market-competitive": [
        "{topic} (pricing OR procurement OR vendor)",
        "{topic} (competitors OR market share OR adoption)",
        "{topic} (review OR comparison OR benchmark)",
    ],
    "security-risk": [
        "{topic} (advisory OR vulnerability OR incident)",
        "{topic} (CVE OR exploit OR mitigation)",
        "{topic} (risk disclosure OR threat model)",
    ],
    "technical-oss": [
        "{topic} site:github.com",
        "{topic} (release notes OR issues OR pull requests)",
        "{topic} (source code OR implementation OR package)",
    ],
    "identity-profile": [
        "{topic} (official profile OR registry)",
        "{topic} (alias OR same name OR impersonation)",
        "{topic} (biography OR organization profile)",
    ],
    "public-sentiment": [
        "{topic} (forum OR discussion OR complaint)",
        "{topic} (reviews OR user reports OR support thread)",
        "{topic} (reddit OR community OR comments)",
    ],
    "local-language": [
        "{topic} (local language OR native term)",
        '{topic} "{languages}"',
        '{topic} "{jurisdictions}"',
    ],
}


def split_values(value: str | None) -> list[str]:
    if not value:
        return []
    return [part.strip() for part in re.split(r"[,;/]", value) if part.strip()]


def normalize_family(value: str) -> str:
    key = value.strip().lower()
    return FAMILY_ALIASES.get(key, key.replace("_", "-").replace(" ", "-"))


def selected_families(raw: str | None) -> list[str]:
    requested: list[str] = []
    for item in split_values(raw):
        family = normalize_family(item)
        if family not in requested:
            requested.append(family)

    families = requested + [family for family in BASE_FAMILIES if family not in requested]
    return families


def domain_keys(value: str | None) -> list[str]:
    keys: list[str] = []
    for raw in split_values(value):
        normalized = raw.strip().lower().replace("_", "-")
        for token in re.split(r"[/\-\s]+", normalized):
            if token in DOMAIN_LANES and token not in keys:
                keys.append(token)
    return keys
