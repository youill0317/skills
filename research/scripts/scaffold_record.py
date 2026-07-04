#!/usr/bin/env python3
"""Create one Markdown research record scaffold.

Usage:
  python research/scripts/scaffold_record.py --topic "topic" --request "user request" --scope "scope"

The scaffold intentionally contains FILLME placeholders. A completed record
should pass `validate_record.py` without `--allow-placeholders`.
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
import argparse
import re
import sys
import unicodedata


def slugify(topic: str) -> str:
    ascii_text = (
        unicodedata.normalize("NFKD", topic)
        .encode("ascii", "ignore")
        .decode("ascii")
        .lower()
    )
    slug = re.sub(r"[^a-z0-9]+", "-", ascii_text).strip("-")
    slug = re.sub(r"-{2,}", "-", slug)
    return slug[:60].strip("-") or "research"


def next_prefix(record_dir: Path) -> int:
    highest = 0
    if record_dir.exists():
        for path in record_dir.glob("[0-9][0-9][0-9]-*.md"):
            try:
                highest = max(highest, int(path.name[:3]))
            except ValueError:
                continue
    return highest + 1


def build_record(topic: str, request: str, scope: str, as_of: str) -> str:
    today = datetime.now().astimezone().strftime("%Y-%m-%d")
    return f"""# Research: {topic}

Date: {today}
User request: {request}
Scope: {scope}
As of: {as_of}

## Answer

FILLME

## Key Findings

- FILLME

## Evidence Maturity Dashboard

Summarize whether the evidence record is mature enough for each central claim,
comparison, recommendation, or decision. This dashboard does not replace the
detailed audit sections; it points to the weakest gates before final synthesis.

| Maturity ID | Item | Type | Linked Claims / Questions | Required Gate Cluster | Current Maturity | Blocking Debt / Weakest Link | Decision / Synthesis Effect |
|---|---|---|---|---|---|---|---|
| EM1 | central answer | final answer | C1 / Q1 | search, source, verification, synthesis, decision | blocked | D1 / unresolved source family / failed gate | no firm conclusion until maturity improves |

## Decision Usefulness Matrix

| Decision / Use Case | Options / Actions | Criteria | Evidence Link | Risks / Tradeoffs | What Would Change This | Status |
|---|---|---|---|---|---|---|
| not applicable | not applicable | not applicable | C1 | FILLME | FILLME | not applicable |

## Comparison And Evaluation Audit

Use this for comparisons, recommendations, rankings, vendor/product choices,
market scans, policy/legal options, academic theory comparisons, investment or
security diligence, and any answer that says better, worse, best, prefer,
choose, or recommend.

| Evaluation ID | Options / Entities | Criteria / Axes | Weight / Priority | Evidence Links | Missing / Non-Comparable Data | Tradeoffs / Sensitivity | Status | Decision Effect |
|---|---|---|---|---|---|---|---|---|
| EV1 | not applicable | not applicable | not applicable | C1 / S1 / O1 / D1 | not applicable | AS1 / none | not applicable | no recommendation |

## Question Coverage Audit

| Question ID | User Need / Subquestion | Answer Status | Evidence / Claim Links | Residual Gap | Final Answer Location |
|---|---|---|---|---|---|
| Q1 | FILLME | unanswered | C1 / D1 | FILLME | Answer / Open Questions |

Resolve every unanswered question coverage row before final validation.

## Tool Capability Audit

| Capability | Status | Use / Reason | Limits / Fallback | Record Impact |
|---|---|---|---|---|
| web search | planned | FILLME | FILLME | FILLME |
| batch / parallel diversified search | planned | FILLME | FILLME | FILLME |
| source open / fetch | planned | FILLME | FILLME | FILLME |
| in-source find / extraction | planned | FILLME | FILLME | FILLME |
| connectors / databases | planned | FILLME | FILLME | FILLME |
| local files / code search | planned | FILLME | FILLME | FILLME |
| repository / package access | planned | FILLME | FILLME | FILLME |
| archive / browser fallback | planned | FILLME | FILLME | FILLME |
| source retrieval fallback | planned | FILLME | FILLME | FILLME |
| document/PDF/table extraction | planned | FILLME | FILLME | FILLME |
| subagents / parallel lanes | planned | FILLME | FILLME | FILLME |

## Search Matrix

| Lane | Claim / Subquestion | Evidence Need | Source Families | Query / Path Patterns | Counter-Search | Final Status |
|---|---|---|---|---|---|---|
| L1 | FILLME | FILLME | FILLME | FILLME | FILLME | planned |

## Diversified Search Batch Plan

| Batch | Source Families To Mix | Purpose | Record Integration |
|---|---|---|---|
| B1 | scout / official-primary / pdf-document / dataset-method | execute source-of-truth discovery queries as sub-batches of up to tool-limit; SB1: scout and official-primary; SB2: pdf-document and dataset-method | Search Craft Log / Search Result Triage / Saturation Metrics |
| B2 | currentness / counterevidence / source-lineage / provenance-archive | execute freshness, contradiction, and upstream-origin queries as sub-batches of up to tool-limit; SB1: currentness and counterevidence; SB2: source-lineage and provenance-archive | Currentness And Version Audit / Source Lineage Map / Absence Evidence Audit |
| B3 | frontier-expansion / blocked-source-recovery / scholarly / github-oss / implementation-code | execute lead-expansion and blocked-source-recovery queries as sub-batches of up to tool-limit; SB1: frontier-expansion and blocked-source-recovery; SB2: scholarly, github-oss, and implementation-code | Lead Ledger / Expansion Frontier Audit / Access And Retrieval Audit / Coverage Debt |

## Domain Coverage Matrix

| Domain / Protocol | Applicability | Required Source Families | Status | Notes / Exclusions |
|---|---|---|---|---|
| official / primary | uncertain | governing records, official docs, filings, standards, releases | planned | FILLME |
| currentness / latest state | uncertain | changelogs, advisories, dockets, status pages, latest official updates | planned | FILLME |
| scholarly / academic | uncertain | full text, methods, literature reviews, replication, citations | planned | FILLME |
| data / statistics / methods | uncertain | datasets, methodology notes, codebooks, uncertainty, denominators | planned | FILLME |
| legal / regulatory / policy | uncertain | laws, regulations, guidance, enforcement, comments, effective dates | planned | FILLME |
| market / competitive / product | uncertain | competitors, pricing, adoption, reviews, procurement, availability | planned | FILLME |
| technical / OSS / implementation | uncertain | docs, source code, issues, releases, package registries, advisories | planned | FILLME |
| security / safety / risk | uncertain | advisories, incidents, CVEs, mitigations, risk disclosures | planned | FILLME |
| provenance / identity / archives | uncertain | original sources, archives, registries, profiles, citations, lineage | planned | FILLME |
| public sentiment / behavior | uncertain | forums, reviews, support threads, complaints, observed behavior | planned | FILLME |

## Language And Locale Audit

| Locale / Language | Applicability | Native Terms / Aliases | Local Source Families | Status | Confidence Impact |
|---|---|---|---|---|---|
| global / English / local language | uncertain | FILLME | local official, local media, registries, databases, forums, archives | planned | FILLME |

## Entity And Terminology Audit

| Entity / Term | Ambiguity Risk | Included Identifiers / Aliases | Exclusion Terms / Lookalikes | Verification Sources | Status | Confidence Effect |
|---|---|---|---|---|---|---|
| FILLME | FILLME | FILLME | FILLME | S1 / source family | blocked | insufficient |

## Worker Wave Plan

| Wave | Purpose | Lanes / Passes | Execution | Completion Criteria |
|---|---|---|---|---|
| W0 | framing and query matrix | FILLME | main agent | FILLME |
| W1 | scout | FILLME | sequential fallback | FILLME |
| W2 | target and snowball | FILLME | sequential fallback | FILLME |
| W3 | EXPAND, counter-search, currentness, provenance, gap pass | FILLME | sequential fallback | FILLME |
| W4 | verification and synthesis-overreach | FILLME | sequential fallback | FILLME |

## Search Craft Log

| Lane | Cycle | Query / Path | Operator / Angle | Source Family | Integrated Finding | Next Lead / Gap |
|---|---|---|---|---|---|---|
| L1 | landscape | FILLME | FILLME | FILLME | FILLME | FILLME |

## Search Result Triage

| Result ID | Lane / Query | Result / URL / Path | Classification | Reason | Follow-Up |
|---|---|---|---|---|---|
| R1 | L1 | FILLME | open-now | FILLME | FILLME |

## Search Bias And Retrieval Trap Audit

Use this to audit whether the search system, platform ranking, query wording,
corpus coverage, snippet display, sponsored/SEO content, duplicate-lineage
results, language choice, personalization, paywalls, or unavailable databases may
have distorted discovery before evidence selection.

| Trap ID | Lane / Query / Source Family | Potential Trap | Diagnostic Check | Mitigation / Alternate Path | Evidence / Follow-Up Links | Status | Confidence Effect |
|---|---|---|---|---|---|---|---|
| SB1 | L1 / query | FILLME | FILLME | FILLME | R1 / S1 / LD1 / D1 | blocked | insufficient until search-bias and retrieval traps are checked |

## Selection And Inclusion Audit

| Evidence Set | Inclusion Criteria | Exclusion / Downrank Criteria | Included Sources | Excluded / Downranked Results | Selection Risk | Mitigation | Status | Confidence Effect |
|---|---|---|---|---|---|---|---|---|
| FILLME | FILLME | FILLME | S1 | R1 / LD1 | FILLME | FILLME | incomplete | insufficient |

## Access And Retrieval Audit

| Retrieval ID | Target Source / Lead | Primary Access Path | Alternate Paths Tried | Retrieval Status | Evidence Use | Confidence Impact |
|---|---|---|---|---|---|---|
| AR1 | S1 | direct URL | archive, PDF, API, browser, mirror, package, cached copy, cited excerpt | blocked | lead only | insufficient |

## Prior Record Check

| Prior Record | Relevance | Sections Loaded | Claims Reused | Refresh Result |
|---|---|---|---|---|
| none | not applicable | none | none | not applicable |

## Wave Log

| Wave | Lane | Pass | Query / Source Path | Result | Leads Raised | Decision |
|---|---|---|---|---|---|---|
| W1 | L1 | scout | FILLME | FILLME | FILLME | follow |

## Lead Ledger

| Lead ID | Raised From | Lead | Why It Matters | Action | Outcome |
|---|---|---|---|---|---|
| LD1 | W1 | FILLME | FILLME | followed | FILLME |

Close every material lead before firm synthesis or tie it to confidence.

## Source-Opened Follow-Up Audit

| Follow-Up ID | Source / Observation | Extracted Lead | Lead Type | Follow-Up Search / Connector Path | Action | Outcome / Confidence Effect |
|---|---|---|---|---|---|---|
| SOF1 | S1 / O1 | FILLME | citation / author / dataset / identifier / native term / correction / counterclaim / blocked source / none | FILLME | unresolved | insufficient until source-opened leads are closed |

Final rows cannot remain planned, open, or unresolved; close them, convert them into Lead Ledger / Expansion Frontier Audit, or reflect them in confidence.

## Expansion Frontier Audit

| Frontier ID | Raised From | Seed / Source | Extracted Frontier | Lead Type | Query / Connector Pass | Status | Outcome / Confidence Effect |
|---|---|---|---|---|---|---|---|
| EF1 | W1 / S1 / R1 / LD1 | FILLME | FILLME | source | FILLME | planned | FILLME |

## Coverage Debt

| Debt ID | Raised From | Gap / Missing Coverage | Why It Matters | Follow-Up Owner / Pass | Status | Confidence Effect |
|---|---|---|---|---|---|---|
| D1 | L1 | FILLME | FILLME | FILLME | open | FILLME |

## Sources

| ID | Source | Type | Accessed / As Of | Why Used | Key Evidence | Limits |
|---|---|---|---|---|---|---|
| S1 | FILLME | FILLME | {today} | FILLME | FILLME | FILLME |

## Source Coverage

| Scope / Family | Target | Inspected | Notes |
|---|---:|---:|---|
| materially relevant sources or records | 12+ / 25+ / 50+ as appropriate | 0 | FILLME |
| official / primary / governing | as needed | 0 | FILLME |
| empirical / method / data | when applicable | 0 | FILLME |
| counterevidence / criticism / limitations | required for central claims | 0 | FILLME |
| currentness / supersession | when applicable | 0 | FILLME |
| OSS / implementation evidence | when applicable | 0 | FILLME |
| scholarly full text / methods | when applicable | 0 | FILLME |

## Saturation Metrics

| Metric | Target / Floor | Actual | Status | Evidence / Record Link | Confidence Effect |
|---|---|---:|---|---|---|
| distinct search queries | at least 10 per important web lane when web search exists | 0 | blocked | not run yet | insufficient until executed |
| inspected relevant sources or records | 12+ narrow, 25+ broad, 50+ very broad when sources exist | 0 | blocked | not run yet | insufficient until executed |
| expansion waves | at least two broad EXPAND waves; three no-new-lead waves for very broad convergence | 0 | blocked | not run yet | insufficient until executed |
| frontier queue convergence | latest EXPAND or gap cycle produces no new high-value leads, or all remaining material leads are closed, blocked, duplicate-lineage, out of scope, low quality, or confidence-downgraded | 0 | blocked | not run yet | insufficient until frontier convergence is documented |
| counter-search passes | every central claim gets negation, rebuttal, limitation, or supersession search | 0 | blocked | not run yet | insufficient until executed |
| local-language or jurisdictional sweeps | required when language, locale, policy, identity, market, or local facts matter | 0 | blocked | not run yet | insufficient until executed |
| material high-value leads closed | all material LD rows followed, closed, blocked, or tied to confidence downgrade | 0 | blocked | not run yet | insufficient until executed |

## Source Lineage Map

| Lineage ID | Upstream Source / Origin | Member Sources | Independence Status | Claims Affected | Notes |
|---|---|---|---|---|---|
| G1 | FILLME | S1 | unclear | C1 | FILLME |

## Source Quality Audit

| Source ID | Authority | Directness | Currentness | Method / Data Quality | Lineage | Overall Status | Confidence Effect |
|---|---|---|---|---|---|---|---|
| S1 | unknown | indirect | unknown | opaque | unclear | weak | downgrades C1 |

## Corroboration And Triangulation Audit

| Claim ID | Primary / Governing Support | Independent Corroboration | Counterevidence / Limitation | Method / Data Check | Lineage Diversity | Status | Confidence Effect |
|---|---|---|---|---|---|---|---|
| C1 | none | none | not searched | not applicable | unclear | blocked | insufficient |

## Consensus And Disagreement Audit

Use this for every central research question, important claim, recommendation,
market conclusion, policy/legal interpretation, scientific or academic claim,
technical/security claim, and other claim where field consensus or expert
disagreement affects how strongly the answer should be stated.

| Consensus ID | Claim / Question | Source Community / Field | Consensus Signal | Disagreement / Minority View | Evidence Links | Recency / Scope Limits | Status | Confidence Effect |
|---|---|---|---|---|---|---|---|---|
| CN1 | C1 / Q1 | FILLME | FILLME | FILLME | C1 / S1 / G1 / O1 / D1 | FILLME | unclear | insufficient until consensus and disagreement are audited |

## Source Incentive And Bias Audit

| Source / Lineage | Incentive / Bias Risk | Funding / Affiliation / Stake | Disclosure Status | Mitigation / Corroboration | Status | Confidence Effect |
|---|---|---|---|---|---|---|
| S1 / G1 | unknown | unknown | unclear | independent corroboration required | unknown | downgrades C1 |

## Source Manipulation And Adversarial Provenance Audit

Use this when a source, repository, package, account, review set, dataset,
screenshot, PDF, media item, public comment set, forum thread, or AI/agent-facing
page could be fabricated, manipulated, coordinated, impersonated, poisoned, or
unsafe to trust as-is.

| Manipulation ID | Source / Claim / Community | Manipulation Risk | Authenticity / Provenance Check | Coordination / Amplification Check | Safety / Injection Check | Evidence Links | Status | Confidence Effect |
|---|---|---|---|---|---|---|---|---|
| MP1 | S1 / C1 / G1 | FILLME | FILLME | FILLME | FILLME | S1 / C1 / G1 / O1 / LD1 / D1 | blocked | insufficient until manipulation and adversarial provenance risks are checked |

## Quantitative And Measurement Audit

| Claim / Metric | Value | Unit / Denominator | Population / Scope | Period / Vintage | Method / Source | Uncertainty / Comparability | Status | Confidence Effect |
|---|---|---|---|---|---|---|---|---|
| C1 / not applicable | not applicable | not applicable | not applicable | not applicable | not applicable | not applicable | not applicable | none |

## Currentness And Version Audit

| Claim / Source | Currentness Need | Evidence Date / Version | Latest / Supersession Check | Status | Confidence Effect |
|---|---|---|---|---|---|
| C1 / S1 | current | unknown | blocked | unknown | insufficient |

## Reproducibility And Refresh Audit

| Item | Reproduction Path | Stable Locator / Version | Volatility / Refresh Trigger | Last Checked | Refresh Action | Status | Confidence Effect |
|---|---|---|---|---|---|---|---|
| whole record / C1 / S1 | FILLME | FILLME | FILLME | {today} | FILLME | blocked | insufficient |

## Observation Manifest

| Obs ID | Source ID | Evidence Layer | Location | Observation | Independence / Lineage | Valid At | Notes |
|---|---|---|---|---|---|---|---|
| O1 | S1 | FILLME | FILLME | FILLME | FILLME | {today} | FILLME |

## Evidence Location Audit

| Claim / Observation | Source ID | Required Locator | Locator Present? | Location Detail | Confidence Effect |
|---|---|---|---|---|---|
| C1 / O1 | S1 | page / section / table / line / timestamp / field / tag / issue / docket | no | FILLME | insufficient |

## Quotation And Context Audit

| Quote / Passage | Source ID | Speaker / Author | Location | Context Checked | Translation / Paraphrase Risk | Claim Fit | Status | Confidence Effect |
|---|---|---|---|---|---|---|---|---|
| C1 / O1 | S1 | unknown | FILLME | FILLME | unresolved | context missing | unresolved | insufficient |

## Absence Evidence Audit

| Claim / Question | Search Boundary | Source Families Checked | Absence Result | Inference Allowed | Confidence Effect |
|---|---|---|---|---|---|
| C1 | FILLME | official / primary / dataset / scholarly / archive / local-language / repository / counter-search | blocked | no absence inference until searched | insufficient |

## Claim Ledger

| Claim ID | Claim | Type | Risk | Support | Counterevidence | Currentness / Version | Verified-Claim Gate | Confidence | Decision |
|---|---|---|---|---|---|---|---|---|---|
| C1 | FILLME | factual | normal | O1, S1 | FILLME | FILLME | not applicable | insufficient | unresolved |

Final validation requires Claim Ledger decisions to resolve to use, downgrade, exclude, or insufficient; unresolved is draft-only.

## Claim Risk Triage

| Claim ID | Decision Impact | Error Risk | Verification Priority | Required Checks | Escalation / Downgrade Rule |
|---|---|---|---|---|---|
| C1 | high | high | high | primary source, counter-search, currentness, lineage, method/data, adversarial review | downgrade or mark insufficient if required checks fail |

## Claim Traceability Matrix

| Claim ID | Final Decision | Observations | Sources | Lineages | Verification Gates | Counterevidence / Debt | Confidence Effect |
|---|---|---|---|---|---|---|---|
| C1 | unresolved | O1 | S1 | G1 | FILLME | D1 | insufficient |

## Inference Boundary Audit

| Claim ID | Observation Base | Inference Type | Required Assumptions | Boundary / Not Supported | Status | Confidence Effect |
|---|---|---|---|---|---|---|
| C1 | O1 / S1 | bounded inference | FILLME | FILLME | blocked | insufficient |

## Assumption And Sensitivity Audit

| Assumption ID | Claim / Decision | Assumption / Variable | Plausible Range / Alternative | Evidence / Test | Sensitivity | Status | Confidence Effect |
|---|---|---|---|---|---|---|---|
| AS1 | C1 / decision | FILLME | FILLME | S1 / O1 / D1 | high | untested | insufficient |

## Conflict Resolution Matrix

| Conflict ID | Claims / Observations | Conflict Type | Evidence On Each Side | Adjudication Basis | Resolution | Confidence Effect |
|---|---|---|---|---|---|---|
| CF1 | C1 / O1 | none | no material conflict checked yet | FILLME | unresolved | insufficient |

## Confidence Calibration

| Claim ID | Evidence Strength | Consistency | Directness | Currentness | Lineage Independence | Method / Data Quality | Counterevidence / Debt | Calibrated Confidence | Rationale |
|---|---|---|---|---|---|---|---|---|---|
| C1 | weak | unresolved | indirect | unknown | unclear | opaque | D1 | insufficient | FILLME |

## Synthesis Traceability Audit

| Output Item | Final Section | Claim Links | Evidence / Source Links | Confidence | Unresolved Limits / Debt | Status | Required Revision |
|---|---|---|---|---|---|---|---|
| ST1 | Answer / Key Findings | C1 | S1 / O1 | insufficient | D1 | blocked | keep final synthesis caveated until traceability passes |

## Adversarial Review

| Review ID | Claim / Finding Challenged | Challenge | Evidence Checked | Result | Outcome | Synthesis Effect |
|---|---|---|---|---|---|---|
| A1 | C1 | FILLME | FILLME | unresolved | unresolved | lowers C1 to insufficient |

## Stop Rule Audit

| Item | Scope | Stop Criteria Checked | Status | Remaining Gap | Confidence Impact |
|---|---|---|---|---|---|
| SR1 | C1 | lanes, source families, EXPAND, counter-search, currentness, lineage, quality, traceability, calibration, adversarial review | not satisfied | D1 | insufficient |

## Atomic Claim Decomposition

| Atomic Claim ID | Parent Claim / Source | Atomic Claim | Verification Priority | Distortion Risk | Status |
|---|---|---|---|---|---|
| AC1 | C1 | FILLME | high | none | verify |

## Distortion Pattern Audit

| Claim / Source | Pattern Checked | Finding | Status | Claim Effect |
|---|---|---|---|---|
| C1 / S1 | stale, misattribution, conflation, circular citation, inference upgraded to fact, magnitude drift, quote distortion, translation drift, cherry-pick, survivorship bias | FILLME | unresolved | insufficient |

## Verified Claims

| Claim ID | Primary / Governing Source | Independent Lineages | Counter-Search | Temporal Evidence | Gate Outcome |
|---|---|---|---|---|---|
| C1 | FILLME | FILLME | FILLME | FILLME | fail |

## Evidence

FILLME

## Counterevidence / Uncertainty

FILLME

## What I Checked

FILLME

## What I Did Not Check

FILLME

## Search Path

FILLME

## Leads Followed

FILLME

## Dead Ends

FILLME

## Verification Notes

FILLME

### Evidence Ledger

| Claim | Support | Counterevidence | Source Quality / Lineage | Currentness | Verified-Claim Gate | Confidence | Decision |
|---|---|---|---|---|---|---|---|
| FILLME | S1 | FILLME | FILLME | FILLME | not applicable | insufficient | unresolved |

## Coverage Gates

- saturation completeness: FILLME
- question coverage audit: FILLME
- saturation metrics: FILLME
- search matrix: FILLME
- diversified search batch plan: FILLME
- decision usefulness: FILLME
- evidence maturity dashboard: FILLME
- comparison and evaluation audit: FILLME
- tool capability audit: FILLME
- domain coverage matrix: FILLME
- language and locale audit: FILLME
- entity and terminology audit: FILLME
- search craft floors: FILLME
- search result triage: FILLME
- search bias and retrieval trap audit: FILLME
- selection and inclusion audit: FILLME
- access and retrieval audit: FILLME
- source-count and source-diversity floor: FILLME
- lane coverage: FILLME
- worker-wave coverage: FILLME
- source lineage map: FILLME
- source quality audit: FILLME
- corroboration and triangulation audit: FILLME
- consensus and disagreement audit: FILLME
- source incentive and bias audit: FILLME
- source manipulation and adversarial provenance audit: FILLME
- quantitative and measurement audit: FILLME
- currentness and version audit: FILLME
- reproducibility and refresh audit: FILLME
- evidence location audit: FILLME
- absence evidence audit: FILLME
- claim risk triage: FILLME
- claim traceability matrix: FILLME
- inference boundary audit: FILLME
- assumption and sensitivity audit: FILLME
- conflict resolution matrix: FILLME
- confidence calibration: FILLME
- adversarial review: FILLME
- stop rule audit: FILLME
- distortion pattern audit: FILLME
- scout: FILLME
- target: FILLME
- snowball: FILLME
- EXPAND lead loop: FILLME
- frontier queue convergence: FILLME
- expansion frontier audit / frontier extraction: FILLME
- lead ledger: FILLME
- coverage debt cleared or downgraded: FILLME
- counter-search: FILLME
- gap pass: FILLME
- source audit: FILLME
- claim verification audit: FILLME
- currentness audit: FILLME
- contradiction and gap audit: FILLME
- source-lineage audit: FILLME
- verified-claim gate: FILLME
- synthesis-overreach audit: FILLME
- method/data audit, when applicable: FILLME

## Acceptance Tests

| Test | Required? | Result | Evidence / Location | Remediation |
|---|---|---|---|---|
| Single Markdown Record Test | yes | FILLME | FILLME | FILLME |
| Saturation Protocol Test | yes | FILLME | FILLME | FILLME |
| Question Coverage Test | yes | FILLME | FILLME | FILLME |
| Search Matrix Completion Test | yes | FILLME | FILLME | FILLME |
| Saturation Metrics Test | yes | FILLME | FILLME | FILLME |
| Decision Usefulness Test | yes | FILLME | FILLME | FILLME |
| Evidence Maturity Dashboard Test | yes | FILLME | FILLME | FILLME |
| Comparison And Evaluation Test | yes | FILLME | FILLME | FILLME |
| Tool Capability Test | yes | FILLME | FILLME | FILLME |
| Diversified Search Batch Test | yes | FILLME | FILLME | FILLME |
| Worker Wave Test | yes | FILLME | FILLME | FILLME |
| Domain Coverage Test | yes | FILLME | FILLME | FILLME |
| Language And Locale Test | yes | FILLME | FILLME | FILLME |
| Entity And Terminology Test | yes | FILLME | FILLME | FILLME |
| Search Craft Floor Test | yes | FILLME | FILLME | FILLME |
| Search Result Triage Test | yes | FILLME | FILLME | FILLME |
| Search Bias And Retrieval Trap Test | yes | FILLME | FILLME | FILLME |
| Selection And Inclusion Test | yes | FILLME | FILLME | FILLME |
| Access And Retrieval Test | yes | FILLME | FILLME | FILLME |
| Source-Opened Follow-Up Test | yes | FILLME | FILLME | FILLME |
| Source Coverage Floor Test | yes | FILLME | FILLME | FILLME |
| Source Lineage Map Test | yes | FILLME | FILLME | FILLME |
| Source Quality Audit Test | yes | FILLME | FILLME | FILLME |
| Corroboration And Triangulation Test | yes | FILLME | FILLME | FILLME |
| Consensus And Disagreement Test | yes | FILLME | FILLME | FILLME |
| Source Incentive And Bias Test | yes | FILLME | FILLME | FILLME |
| Source Manipulation And Adversarial Provenance Test | yes | FILLME | FILLME | FILLME |
| Quantitative And Measurement Test | conditional | FILLME | FILLME | FILLME |
| Currentness And Version Audit Test | yes | FILLME | FILLME | FILLME |
| Reproducibility And Refresh Test | yes | FILLME | FILLME | FILLME |
| Evidence Location Audit Test | yes | FILLME | FILLME | FILLME |
| Quotation And Context Test | yes | FILLME | FILLME | FILLME |
| Absence Evidence Test | yes | FILLME | FILLME | FILLME |
| Claim Risk Triage Test | yes | FILLME | FILLME | FILLME |
| Claim Traceability Test | yes | FILLME | FILLME | FILLME |
| Inference Boundary Test | yes | FILLME | FILLME | FILLME |
| Assumption And Sensitivity Test | yes | FILLME | FILLME | FILLME |
| Conflict Resolution Test | yes | FILLME | FILLME | FILLME |
| Confidence Calibration Test | yes | FILLME | FILLME | FILLME |
| Synthesis Traceability Test | yes | FILLME | FILLME | FILLME |
| Adversarial Review Test | yes | FILLME | FILLME | FILLME |
| Stop Rule Audit Test | yes | FILLME | FILLME | FILLME |
| Atomic Claim Decomposition Test | conditional | FILLME | FILLME | FILLME |
| Distortion Pattern Audit Test | yes | FILLME | FILLME | FILLME |
| Claim Support Test | yes | FILLME | FILLME | FILLME |
| Snippet Leakage Test | yes | FILLME | FILLME | FILLME |
| Source-Family Coverage Test | yes | FILLME | FILLME | FILLME |
| Lead Ledger / EXPAND Test | yes | FILLME | FILLME | FILLME |
| Expansion Frontier Test | yes | FILLME | FILLME | FILLME |
| Frontier Queue Convergence Test | yes | FILLME | FILLME | FILLME |
| Coverage Debt Test | yes | FILLME | FILLME | FILLME |
| Currentness Test | conditional | FILLME | FILLME | FILLME |
| Counterevidence Test | yes | FILLME | FILLME | FILLME |
| Provenance / Lineage Test | yes | FILLME | FILLME | FILLME |
| Verified-Claim Gate Test | conditional | FILLME | FILLME | FILLME |
| Method / Data Test | conditional | FILLME | FILLME | FILLME |
| Synthesis Overreach Test | yes | FILLME | FILLME | FILLME |
| Deliverable Readability Test | yes | FILLME | FILLME | FILLME |

## Confidence

FILLME

## Open Questions

FILLME
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", required=True)
    parser.add_argument("--request", required=True)
    parser.add_argument("--scope", required=True)
    parser.add_argument("--root", default=".")
    parser.add_argument("--as-of", default=None)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    record_dir = root / "gigantum-humeris" / "research"
    prefix = next_prefix(record_dir)
    path = record_dir / f"{prefix:03d}-{slugify(args.topic)}.md"
    as_of = args.as_of or datetime.now().astimezone().strftime("%Y-%m-%d %H:%M %Z")
    record = build_record(args.topic, args.request, args.scope, as_of)

    if args.dry_run:
        print(path)
        return 0

    record_dir.mkdir(parents=True, exist_ok=True)
    if path.exists():
        print(f"record already exists: {path}", file=sys.stderr)
        return 1
    path.write_text(record, encoding="utf-8")
    print(path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
