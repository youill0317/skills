#!/usr/bin/env python3
"""Validate a single Markdown research record.

Usage:
  python research/scripts/validate_record.py path/to/NNN-topic.md

This checks structure and required gates only. It does not verify the truth of
sources or claims; the research process and verifier lanes do that.
"""

from __future__ import annotations

from pathlib import Path
import argparse
import re
import sys


REQUIRED_SECTIONS = [
    "Answer",
    "Key Findings",
    "Evidence Maturity Dashboard",
    "Decision Usefulness Matrix",
    "Comparison And Evaluation Audit",
    "Question Coverage Audit",
    "Tool Capability Audit",
    "Search Matrix",
    "Diversified Search Batch Plan",
    "Domain Coverage Matrix",
    "Language And Locale Audit",
    "Entity And Terminology Audit",
    "Worker Wave Plan",
    "Search Craft Log",
    "Search Result Triage",
    "Search Bias And Retrieval Trap Audit",
    "Selection And Inclusion Audit",
    "Access And Retrieval Audit",
    "Wave Log",
    "Lead Ledger",
    "Source-Opened Follow-Up Audit",
    "Expansion Frontier Audit",
    "Coverage Debt",
    "Sources",
    "Source Coverage",
    "Saturation Metrics",
    "Source Lineage Map",
    "Source Quality Audit",
    "Corroboration And Triangulation Audit",
    "Consensus And Disagreement Audit",
    "Source Incentive And Bias Audit",
    "Source Manipulation And Adversarial Provenance Audit",
    "Quantitative And Measurement Audit",
    "Currentness And Version Audit",
    "Reproducibility And Refresh Audit",
    "Observation Manifest",
    "Evidence Location Audit",
    "Quotation And Context Audit",
    "Absence Evidence Audit",
    "Claim Ledger",
    "Claim Risk Triage",
    "Claim Traceability Matrix",
    "Inference Boundary Audit",
    "Assumption And Sensitivity Audit",
    "Conflict Resolution Matrix",
    "Confidence Calibration",
    "Synthesis Traceability Audit",
    "Adversarial Review",
    "Stop Rule Audit",
    "Distortion Pattern Audit",
    "Evidence",
    "Counterevidence / Uncertainty",
    "What I Checked",
    "What I Did Not Check",
    "Search Path",
    "Leads Followed",
    "Dead Ends",
    "Verification Notes",
    "Coverage Gates",
    "Acceptance Tests",
    "Confidence",
    "Open Questions",
]


REQUIRED_METADATA = [
    r"^Date:\s+\S+",
    r"^User request:\s+\S+",
    r"^Scope:\s+\S+",
]


REQUIRED_COVERAGE_GATES = [
    "saturation completeness",
    "question coverage audit",
    "saturation metrics",
    "search matrix",
    "diversified search batch plan",
    "decision usefulness",
    "evidence maturity dashboard",
    "comparison and evaluation audit",
    "tool capability audit",
    "domain coverage matrix",
    "language and locale audit",
    "entity and terminology audit",
    "search craft floors",
    "search result triage",
    "search bias and retrieval trap audit",
    "selection and inclusion audit",
    "access and retrieval audit",
    "source-count and source-diversity floor",
    "lane coverage",
    "worker-wave coverage",
    "source lineage map",
    "source quality audit",
    "corroboration and triangulation audit",
    "consensus and disagreement audit",
    "source incentive and bias audit",
    "source manipulation and adversarial provenance audit",
    "quantitative and measurement audit",
    "currentness and version audit",
    "reproducibility and refresh audit",
    "evidence location audit",
    "quotation and context audit",
    "absence evidence audit",
    "claim risk triage",
    "claim traceability matrix",
    "inference boundary audit",
    "assumption and sensitivity audit",
    "conflict resolution matrix",
    "confidence calibration",
    "synthesis traceability audit",
    "adversarial review",
    "stop rule audit",
    "distortion pattern audit",
    "scout",
    "target",
    "snowball",
    "EXPAND lead loop",
    "frontier queue convergence",
    "lead ledger",
    "expansion frontier audit",
    "frontier extraction",
    "coverage debt cleared or downgraded",
    "counter-search",
    "gap pass",
    "source audit",
    "claim verification audit",
    "currentness audit",
    "contradiction and gap audit",
    "source-lineage audit",
    "verified-claim gate",
    "synthesis-overreach audit",
]


REQUIRED_PHRASES = [
    "| Claim ID | Claim | Type | Risk | Support | Counterevidence | Currentness / Version | Verified-Claim Gate | Confidence | Decision |",
    "| Decision / Use Case | Options / Actions | Criteria | Evidence Link | Risks / Tradeoffs | What Would Change This | Status |",
    "| Maturity ID | Item | Type | Linked Claims / Questions | Required Gate Cluster | Current Maturity | Blocking Debt / Weakest Link | Decision / Synthesis Effect |",
    "| Evaluation ID | Options / Entities | Criteria / Axes | Weight / Priority | Evidence Links | Missing / Non-Comparable Data | Tradeoffs / Sensitivity | Status | Decision Effect |",
    "| Question ID | User Need / Subquestion | Answer Status | Evidence / Claim Links | Residual Gap | Final Answer Location |",
    "| Capability | Status | Use / Reason | Limits / Fallback | Record Impact |",
    "| Lane | Claim / Subquestion | Evidence Need | Source Families | Query / Path Patterns | Counter-Search | Final Status |",
    "| Batch | Source Families To Mix | Purpose | Record Integration |",
    "| Domain / Protocol | Applicability | Required Source Families | Status | Notes / Exclusions |",
    "| Locale / Language | Applicability | Native Terms / Aliases | Local Source Families | Status | Confidence Impact |",
    "| Entity / Term | Ambiguity Risk | Included Identifiers / Aliases | Exclusion Terms / Lookalikes | Verification Sources | Status | Confidence Effect |",
    "| Lead ID | Raised From | Lead | Why It Matters | Action | Outcome |",
    "| Follow-Up ID | Source / Observation | Extracted Lead | Lead Type | Follow-Up Search / Connector Path | Action | Outcome / Confidence Effect |",
    "| Frontier ID | Raised From | Seed / Source | Extracted Frontier | Lead Type | Query / Connector Pass | Status | Outcome / Confidence Effect |",
    "| Debt ID | Raised From | Gap / Missing Coverage | Why It Matters | Follow-Up Owner / Pass | Status | Confidence Effect |",
    "| Wave | Purpose | Lanes / Passes | Execution | Completion Criteria |",
    "| Lane | Cycle | Query / Path | Operator / Angle | Source Family | Integrated Finding | Next Lead / Gap |",
    "| Result ID | Lane / Query | Result / URL / Path | Classification | Reason | Follow-Up |",
    "| Trap ID | Lane / Query / Source Family | Potential Trap | Diagnostic Check | Mitigation / Alternate Path | Evidence / Follow-Up Links | Status | Confidence Effect |",
    "| Evidence Set | Inclusion Criteria | Exclusion / Downrank Criteria | Included Sources | Excluded / Downranked Results | Selection Risk | Mitigation | Status | Confidence Effect |",
    "| Retrieval ID | Target Source / Lead | Primary Access Path | Alternate Paths Tried | Retrieval Status | Evidence Use | Confidence Impact |",
    "| Scope / Family | Target | Inspected | Notes |",
    "| Metric | Target / Floor | Actual | Status | Evidence / Record Link | Confidence Effect |",
    "| Lineage ID | Upstream Source / Origin | Member Sources | Independence Status | Claims Affected | Notes |",
    "| Source ID | Authority | Directness | Currentness | Method / Data Quality | Lineage | Overall Status | Confidence Effect |",
    "| Claim ID | Primary / Governing Support | Independent Corroboration | Counterevidence / Limitation | Method / Data Check | Lineage Diversity | Status | Confidence Effect |",
    "| Consensus ID | Claim / Question | Source Community / Field | Consensus Signal | Disagreement / Minority View | Evidence Links | Recency / Scope Limits | Status | Confidence Effect |",
    "| Source / Lineage | Incentive / Bias Risk | Funding / Affiliation / Stake | Disclosure Status | Mitigation / Corroboration | Status | Confidence Effect |",
    "| Manipulation ID | Source / Claim / Community | Manipulation Risk | Authenticity / Provenance Check | Coordination / Amplification Check | Safety / Injection Check | Evidence Links | Status | Confidence Effect |",
    "| Claim / Metric | Value | Unit / Denominator | Population / Scope | Period / Vintage | Method / Source | Uncertainty / Comparability | Status | Confidence Effect |",
    "| Claim / Source | Currentness Need | Evidence Date / Version | Latest / Supersession Check | Status | Confidence Effect |",
    "| Item | Reproduction Path | Stable Locator / Version | Volatility / Refresh Trigger | Last Checked | Refresh Action | Status | Confidence Effect |",
    "| Claim / Observation | Source ID | Required Locator | Locator Present? | Location Detail | Confidence Effect |",
    "| Claim / Question | Search Boundary | Source Families Checked | Absence Result | Inference Allowed | Confidence Effect |",
    "| Claim ID | Decision Impact | Error Risk | Verification Priority | Required Checks | Escalation / Downgrade Rule |",
    "| Claim ID | Final Decision | Observations | Sources | Lineages | Verification Gates | Counterevidence / Debt | Confidence Effect |",
    "| Claim ID | Observation Base | Inference Type | Required Assumptions | Boundary / Not Supported | Status | Confidence Effect |",
    "| Assumption ID | Claim / Decision | Assumption / Variable | Plausible Range / Alternative | Evidence / Test | Sensitivity | Status | Confidence Effect |",
    "| Conflict ID | Claims / Observations | Conflict Type | Evidence On Each Side | Adjudication Basis | Resolution | Confidence Effect |",
    "| Claim ID | Evidence Strength | Consistency | Directness | Currentness | Lineage Independence | Method / Data Quality | Counterevidence / Debt | Calibrated Confidence | Rationale |",
    "| Output Item | Final Section | Claim Links | Evidence / Source Links | Confidence | Unresolved Limits / Debt | Status | Required Revision |",
    "| Review ID | Claim / Finding Challenged | Challenge | Evidence Checked | Result | Outcome | Synthesis Effect |",
    "| Item | Scope | Stop Criteria Checked | Status | Remaining Gap | Confidence Impact |",
    "| Claim / Source | Pattern Checked | Finding | Status | Claim Effect |",
    "| Test | Required? | Result | Evidence / Location | Remediation |",
    "Single Markdown Record Test",
    "Saturation Protocol Test",
    "Question Coverage Test",
    "Search Matrix Completion Test",
    "Saturation Metrics Test",
    "Decision Usefulness Test",
    "Evidence Maturity Dashboard Test",
    "Comparison And Evaluation Test",
    "Tool Capability Test",
    "Diversified Search Batch Test",
    "Worker Wave Test",
    "Domain Coverage Test",
    "Language And Locale Test",
    "Entity And Terminology Test",
    "Claim Support Test",
    "Search Result Triage Test",
    "Search Bias And Retrieval Trap Test",
    "Selection And Inclusion Test",
    "Access And Retrieval Test",
    "Source Lineage Map Test",
    "Source Quality Audit Test",
    "Corroboration And Triangulation Test",
    "Consensus And Disagreement Test",
    "Source Incentive And Bias Test",
    "Source Manipulation And Adversarial Provenance Test",
    "Quantitative And Measurement Test",
    "Currentness And Version Audit Test",
    "Reproducibility And Refresh Test",
    "Evidence Location Audit Test",
    "Quotation And Context Test",
    "Absence Evidence Test",
    "Claim Risk Triage Test",
    "Claim Traceability Test",
    "Inference Boundary Test",
    "Assumption And Sensitivity Test",
    "Conflict Resolution Test",
    "Confidence Calibration Test",
    "Synthesis Traceability Test",
    "Adversarial Review Test",
    "Stop Rule Audit Test",
    "Distortion Pattern Audit Test",
    "Synthesis Overreach Test",
    "12+ / 25+ / 50+",
]


REQUIRED_ACCEPTANCE_TESTS = [
    "Single Markdown Record Test",
    "Saturation Protocol Test",
    "Question Coverage Test",
    "Search Matrix Completion Test",
    "Saturation Metrics Test",
    "Decision Usefulness Test",
    "Evidence Maturity Dashboard Test",
    "Comparison And Evaluation Test",
    "Tool Capability Test",
    "Diversified Search Batch Test",
    "Worker Wave Test",
    "Domain Coverage Test",
    "Language And Locale Test",
    "Entity And Terminology Test",
    "Search Craft Floor Test",
    "Search Result Triage Test",
    "Search Bias And Retrieval Trap Test",
    "Selection And Inclusion Test",
    "Access And Retrieval Test",
    "Source-Opened Follow-Up Test",
    "Source Coverage Floor Test",
    "Source Lineage Map Test",
    "Source Quality Audit Test",
    "Corroboration And Triangulation Test",
    "Consensus And Disagreement Test",
    "Source Incentive And Bias Test",
    "Source Manipulation And Adversarial Provenance Test",
    "Quantitative And Measurement Test",
    "Currentness And Version Audit Test",
    "Reproducibility And Refresh Test",
    "Evidence Location Audit Test",
    "Quotation And Context Test",
    "Absence Evidence Test",
    "Claim Risk Triage Test",
    "Claim Traceability Test",
    "Inference Boundary Test",
    "Assumption And Sensitivity Test",
    "Conflict Resolution Test",
    "Confidence Calibration Test",
    "Synthesis Traceability Test",
    "Adversarial Review Test",
    "Stop Rule Audit Test",
    "Coverage Debt Test",
    "Distortion Pattern Audit Test",
    "Claim Support Test",
    "Snippet Leakage Test",
    "Source-Family Coverage Test",
    "Lead Ledger / EXPAND Test",
    "Expansion Frontier Test",
    "Frontier Queue Convergence Test",
    "Counterevidence Test",
    "Provenance / Lineage Test",
    "Synthesis Overreach Test",
    "Deliverable Readability Test",
]


REQUIRED_SATURATION_METRICS = [
    "distinct search queries",
    "inspected relevant sources or records",
    "expansion waves",
    "frontier queue convergence",
    "counter-search passes",
    "local-language or jurisdictional sweeps",
    "material high-value leads closed",
]


REQUIRED_BATCH_INTEGRATION_TARGETS = [
    "search craft log",
    "search result triage",
    "lead ledger",
    "expansion frontier audit",
    "access and retrieval audit",
    "coverage debt",
    "currentness and version audit",
    "source lineage map",
    "claim ledger",
    "saturation metrics",
]


REQUIRED_TOOL_CAPABILITY_ROWS = [
    "web search",
    "batch / parallel diversified search",
    "source open / fetch",
    "source retrieval fallback",
    "subagents / parallel lanes",
]


ALLOWED_SEARCH_MATRIX_FINAL_STATUS = {
    "complete",
    "blocked",
    "superseded",
    "not applicable",
    "not-applicable",
}


ALLOWED_LEAD_ACTIONS = {
    "followed",
    "duplicate",
    "duplicate-lineage",
    "blocked",
    "low quality",
    "low-quality",
    "out of scope",
    "out-of-scope",
    "not applicable",
    "not-applicable",
}


ALLOWED_SOURCE_OPENED_FOLLOW_UP_ACTIONS = {
    "followed",
    "closed",
    "blocked",
    "duplicate",
    "duplicate-lineage",
    "low quality",
    "low-quality",
    "out of scope",
    "out-of-scope",
    "no leads",
    "none",
    "not applicable",
    "not-applicable",
    "planned",
    "open",
    "unresolved",
}


ALLOWED_COVERAGE_DEBT_STATUS = {
    "open",
    "cleared",
    "blocked",
    "downgraded",
    "not applicable",
    "not-applicable",
}


ALLOWED_TEST_RESULTS = {
    "pass",
    "fail",
    "blocked",
    "not applicable",
    "not-applicable",
}


ALLOWED_TRIAGE_CLASSES = {
    "open-now",
    "lead",
    "duplicate-lineage",
    "context-only",
    "dead-end",
}

ALLOWED_SEARCH_BIAS_STATUS = {
    "bias-mitigated",
    "bias mitigated",
    "bounded",
    "trap-found",
    "trap found",
    "blocked",
    "not applicable",
    "not-applicable",
}

ALLOWED_SELECTION_STATUS = {
    "balanced",
    "bounded",
    "biased",
    "incomplete",
    "blocked",
    "not applicable",
    "not-applicable",
}


ALLOWED_LINEAGE_STATUS = {
    "original",
    "independent",
    "same-lineage",
    "mirror",
    "unclear",
}


ALLOWED_TRACE_DECISIONS = {
    "use",
    "downgrade",
    "exclude",
    "unresolved",
    "insufficient",
}


ALLOWED_CLAIM_LEDGER_DECISIONS = {
    "use",
    "downgrade",
    "exclude",
    "unresolved",
    "insufficient",
}


ALLOWED_VERIFIED_CLAIM_GATE = {
    "pass",
    "fail",
    "blocked",
    "not applicable",
    "not-applicable",
}


ALLOWED_INFERENCE_BOUNDARY_STATUS = {
    "supported",
    "bounded",
    "overreach",
    "speculative",
    "blocked",
    "not applicable",
    "not-applicable",
}


ALLOWED_ASSUMPTION_SENSITIVITY_STATUS = {
    "stable",
    "sensitive",
    "decision-changing",
    "decision changing",
    "untested",
    "blocked",
    "not applicable",
    "not-applicable",
}


ALLOWED_CONFLICT_RESOLUTION = {
    "prefer",
    "bound",
    "split",
    "unresolved",
    "insufficient",
    "not applicable",
    "not-applicable",
}


ALLOWED_SOURCE_QUALITY_STATUS = {
    "strong",
    "usable",
    "limited",
    "weak",
    "exclude",
}


ALLOWED_CORROBORATION_STATUS = {
    "triangulated",
    "partially corroborated",
    "partially-corroborated",
    "single-source",
    "single source",
    "contradicted",
    "blocked",
    "not applicable",
    "not-applicable",
}

ALLOWED_CONSENSUS_DISAGREEMENT_STATUS = {
    "consensus",
    "dominant consensus",
    "dominant-consensus",
    "mixed",
    "contested",
    "fringe",
    "unclear",
    "blocked",
    "not applicable",
    "not-applicable",
}

ALLOWED_SOURCE_INCENTIVE_STATUS = {
    "clear",
    "disclosed",
    "mitigated",
    "conflicted",
    "unknown",
    "blocked",
    "not applicable",
    "not-applicable",
}

ALLOWED_MANIPULATION_PROVENANCE_STATUS = {
    "clear",
    "mitigated",
    "suspected",
    "found",
    "blocked",
    "not applicable",
    "not-applicable",
}

ALLOWED_QUANTITATIVE_STATUS = {
    "verified",
    "bounded",
    "inconsistent",
    "opaque",
    "blocked",
    "not applicable",
    "not-applicable",
}


ALLOWED_CLAIM_TRIAGE_PRIORITY = {
    "high",
    "medium",
    "low",
}


ALLOWED_CALIBRATED_CONFIDENCE = {
    "high",
    "medium",
    "low",
    "insufficient",
}


ALLOWED_ADVERSARIAL_OUTCOME = {
    "upheld",
    "revised",
    "downgraded",
    "unresolved",
    "insufficient",
}


ALLOWED_STOP_RULE_STATUS = {
    "satisfied",
    "blocked",
    "not satisfied",
    "not applicable",
    "not-applicable",
}


ALLOWED_DISTORTION_STATUS = {
    "clear",
    "found",
    "unresolved",
    "not applicable",
    "not-applicable",
}


ALLOWED_DOMAIN_COVERAGE_STATUS = {
    "planned",
    "searched",
    "covered",
    "blocked",
    "not applicable",
    "not-applicable",
}


ALLOWED_LANGUAGE_LOCALE_STATUS = {
    "planned",
    "searched",
    "covered",
    "blocked",
    "not applicable",
    "not-applicable",
}


ALLOWED_ENTITY_TERMINOLOGY_STATUS = {
    "resolved",
    "bounded",
    "ambiguous",
    "blocked",
    "not applicable",
    "not-applicable",
}


ALLOWED_RETRIEVAL_STATUS = {
    "retrieved",
    "alternate retrieved",
    "alternate-retrieved",
    "blocked",
    "not applicable",
    "not-applicable",
}


ALLOWED_CURRENTNESS_STATUS = {
    "current",
    "stale",
    "superseded",
    "unknown",
    "not applicable",
    "not-applicable",
}


ALLOWED_REPRODUCIBILITY_STATUS = {
    "reproducible",
    "bounded",
    "volatile",
    "blocked",
    "not applicable",
    "not-applicable",
}


ALLOWED_EVIDENCE_LOCATION_STATUS = {
    "yes",
    "no",
    "blocked",
    "not applicable",
    "not-applicable",
}


ALLOWED_QUOTATION_CONTEXT_STATUS = {
    "clear",
    "bounded",
    "distorted",
    "unresolved",
    "blocked",
    "not applicable",
    "not-applicable",
}


ALLOWED_EXPANSION_FRONTIER_STATUS = {
    "planned",
    "searched",
    "followed",
    "duplicate-lineage",
    "duplicate lineage",
    "low-quality",
    "low quality",
    "blocked",
    "out-of-scope",
    "out of scope",
    "not applicable",
    "not-applicable",
}


ALLOWED_SATURATION_METRIC_STATUS = {
    "met",
    "not met",
    "not-met",
    "blocked",
    "not applicable",
    "not-applicable",
}


ALLOWED_SYNTHESIS_TRACE_STATUS = {
    "ready",
    "caveated",
    "revise",
    "blocked",
    "exclude",
    "not applicable",
    "not-applicable",
}


ALLOWED_ABSENCE_RESULT = {
    "found",
    "not found",
    "not-found",
    "mixed",
    "blocked",
    "not applicable",
    "not-applicable",
}


ALLOWED_DECISION_STATUS = {
    "actionable",
    "caveated",
    "not decision-ready",
    "not-decision-ready",
    "not applicable",
    "not-applicable",
}

ALLOWED_EVIDENCE_MATURITY_STATUS = {
    "mature",
    "caveated",
    "immature",
    "blocked",
    "not applicable",
    "not-applicable",
}


ALLOWED_COMPARISON_EVALUATION_STATUS = {
    "comparable",
    "partially comparable",
    "partially-comparable",
    "non-comparable",
    "non comparable",
    "biased",
    "blocked",
    "not applicable",
    "not-applicable",
}


ALLOWED_QUESTION_COVERAGE_STATUS = {
    "answered",
    "partially answered",
    "partially-answered",
    "unanswered",
    "blocked",
    "out of scope",
    "out-of-scope",
    "not applicable",
    "not-applicable",
}


ALLOWED_TOOL_CAPABILITY_STATUS = {
    "planned",
    "used",
    "blocked",
    "unavailable",
    "not applicable",
    "not-applicable",
}


PLACEHOLDER_PATTERNS = [
    r"\bTODO\b",
    r"\bTBD\b",
    r"\bFILLME\b",
    r"\btool-limit\b",
    r"<Topic>",
    r"\.\.\.",
]


FORBIDDEN_SIDECAR_PATTERNS = [
    r"(?<![\w.-])(brief|sources|notes|claim-graph|source-ledger|observation-manifest|verification-log|batch-plan|frontier-queue|worker-waves|search-triage|coverage-debt|validation-results)\.md(?![\w.-])",
    r"(?<![\w.-])(screenshots|sources|claims|notes|batches|frontier|workers|audits|validation)/",
]


FORBIDDEN_SIBLING_NAMES = {
    "brief.md",
    "sources.md",
    "notes.md",
    "claim-graph.md",
    "source-ledger.md",
    "observation-manifest.md",
    "verification-log.md",
    "batch-plan.md",
    "frontier-queue.md",
    "worker-waves.md",
    "search-triage.md",
    "coverage-debt.md",
    "validation-results.md",
}


RECORD_FILENAME_PATTERN = re.compile(r"^\d{3}-[a-z0-9][a-z0-9-]*\.md$")


def normalize(text: str) -> str:
    return " ".join(text.split())


def has_heading(text: str, heading: str) -> bool:
    pattern = re.compile(rf"^##\s+{re.escape(heading)}\s*$", re.MULTILINE)
    return bool(pattern.search(text))


def section_body(text: str, heading: str) -> str:
    pattern = re.compile(
        rf"^##\s+{re.escape(heading)}\s*$"
        rf"(?P<body>.*?)(?=^##\s+|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(text)
    return match.group("body") if match else ""


def text_without_urls(text: str) -> str:
    return re.sub(r"https?://\S+", "", text)


def parse_markdown_rows(section: str) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in section.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|") or not stripped.endswith("|"):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if cells and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
            continue
        rows.append(cells)
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("record", help="Path to one Markdown research record")
    parser.add_argument(
        "--allow-placeholders",
        action="store_true",
        help="Allow TODO/TBD/ellipsis placeholders for template validation",
    )
    args = parser.parse_args()

    record = Path(args.record)
    failures: list[str] = []

    if not record.exists():
        failures.append(f"record does not exist: {record}")
    elif record.suffix.lower() != ".md":
        failures.append(f"record is not Markdown: {record}")
    elif not args.allow_placeholders and not RECORD_FILENAME_PATTERN.match(record.name):
        failures.append("record filename must match <NNN-ascii-slug>.md")

    if failures:
        for failure in failures:
            print(f"- {failure}")
        return 1

    text = record.read_text(encoding="utf-8").lstrip("\ufeff")
    normalized = normalize(text)

    if not re.search(r"^#\s+Research:", text, re.MULTILINE):
        failures.append("missing top-level '# Research: <Topic>' heading")

    for pattern in REQUIRED_METADATA:
        if not re.search(pattern, text, re.MULTILINE):
            failures.append(f"missing required metadata matching: {pattern}")

    for heading in REQUIRED_SECTIONS:
        if not has_heading(text, heading):
            failures.append(f"missing section: ## {heading}")

    for phrase in REQUIRED_PHRASES:
        if normalize(phrase) not in normalized:
            failures.append(f"missing required table/header phrase: {phrase}")

    lower = text.lower()
    for gate in REQUIRED_COVERAGE_GATES:
        if gate.lower() not in lower:
            failures.append(f"missing coverage gate: {gate}")

    if not args.allow_placeholders:
        acceptance_rows = parse_markdown_rows(section_body(text, "Acceptance Tests"))
        acceptance_by_name: dict[str, list[str]] = {}
        for row in acceptance_rows[1:]:
            if len(row) >= 3:
                acceptance_by_name[row[0]] = row
        for test_name in REQUIRED_ACCEPTANCE_TESTS:
            row = acceptance_by_name.get(test_name)
            if row is None:
                failures.append(f"missing acceptance test row: {test_name}")
                continue
            result = row[2].lower()
            if result not in ALLOWED_TEST_RESULTS:
                failures.append(
                    f"acceptance test {test_name!r} has invalid result {row[2]!r}"
                )
            if result == "fail":
                failures.append(
                    f"required acceptance test {test_name!r} remains failed in final record"
                )
            if result in {"blocked", "not applicable", "not-applicable"}:
                evidence = row[3].strip().lower() if len(row) > 3 else ""
                remediation = row[4].strip().lower() if len(row) > 4 else ""
                weak_values = {"", "pass", "none", "n/a", "na", "not applicable", "not-applicable"}
                if evidence in weak_values or remediation in weak_values:
                    failures.append(
                        f"acceptance test {test_name!r} has weak blocked/not-applicable evidence or remediation"
                    )

        maturity_rows = parse_markdown_rows(section_body(text, "Evidence Maturity Dashboard"))
        if len(maturity_rows) <= 1:
            failures.append("Evidence Maturity Dashboard must include at least one row")
        for row in maturity_rows[1:]:
            if len(row) < 8:
                failures.append("Evidence Maturity Dashboard row has too few columns")
                continue
            maturity = row[5].lower()
            if maturity not in ALLOWED_EVIDENCE_MATURITY_STATUS:
                failures.append(
                    f"Evidence Maturity Dashboard has invalid maturity {row[5]!r}"
                )

        decision_rows = parse_markdown_rows(section_body(text, "Decision Usefulness Matrix"))
        if len(decision_rows) <= 1:
            failures.append("Decision Usefulness Matrix must include at least one decision row")
        for row in decision_rows[1:]:
            if len(row) < 7:
                failures.append("Decision Usefulness Matrix row has too few columns")
                continue
            status = row[6].lower()
            if status not in ALLOWED_DECISION_STATUS:
                failures.append(
                    f"Decision Usefulness Matrix has invalid status {row[6]!r}"
                )

        comparison_rows = parse_markdown_rows(section_body(text, "Comparison And Evaluation Audit"))
        if len(comparison_rows) <= 1:
            failures.append("Comparison And Evaluation Audit must include at least one evaluation row")
        for row in comparison_rows[1:]:
            if len(row) < 9:
                failures.append("Comparison And Evaluation Audit row has too few columns")
                continue
            status = row[7].lower()
            if status not in ALLOWED_COMPARISON_EVALUATION_STATUS:
                failures.append(
                    f"Comparison And Evaluation Audit has invalid status {row[7]!r}"
                )

        question_rows = parse_markdown_rows(section_body(text, "Question Coverage Audit"))
        if len(question_rows) <= 1:
            failures.append("Question Coverage Audit must include at least one question row")
        for row in question_rows[1:]:
            if len(row) < 3:
                failures.append("Question Coverage Audit row has too few columns")
                continue
            status = row[2].lower()
            if not args.allow_placeholders and status == "unanswered":
                failures.append("Question Coverage Audit row remains unanswered in final record")
            if status not in ALLOWED_QUESTION_COVERAGE_STATUS:
                failures.append(
                    f"Question Coverage Audit has invalid answer status {row[2]!r}"
                )

        search_rows = parse_markdown_rows(section_body(text, "Search Matrix"))
        if len(search_rows) <= 1:
            failures.append("Search Matrix must include at least one lane row")
        for row in search_rows[1:]:
            if len(row) < 7:
                failures.append("Search Matrix row has too few columns")
                continue
            if args.allow_placeholders:
                continue
            status = row[6].lower()
            if status in {"planned", "running"}:
                failures.append("Search Matrix lane remains planned/running instead of closed")
            elif status not in ALLOWED_SEARCH_MATRIX_FINAL_STATUS:
                failures.append(f"Search Matrix has invalid final status {row[6]!r}")

        tool_rows = parse_markdown_rows(section_body(text, "Tool Capability Audit"))
        if len(tool_rows) <= 1:
            failures.append("Tool Capability Audit must include at least one capability row")
        tool_capabilities = "\n".join(row[0].lower() for row in tool_rows[1:] if row)
        for capability in REQUIRED_TOOL_CAPABILITY_ROWS:
            if capability not in tool_capabilities:
                failures.append(f"Tool Capability Audit missing required capability row: {capability}")
        for row in tool_rows[1:]:
            if len(row) < 2:
                failures.append("Tool Capability Audit row has too few columns")
                continue
            status = row[1].lower()
            if not args.allow_placeholders and status == "planned":
                failures.append("Tool Capability Audit capability remains planned instead of resolved")
            if status not in ALLOWED_TOOL_CAPABILITY_STATUS:
                failures.append(
                    f"Tool Capability Audit has invalid status {row[1]!r}"
                )

        batch_rows = parse_markdown_rows(section_body(text, "Diversified Search Batch Plan"))
        if len(batch_rows) <= 3:
            failures.append("Diversified Search Batch Plan must include at least three batch rows")
        batch_text = "\n".join(" | ".join(row).lower() for row in batch_rows[1:])
        for row in batch_rows[1:]:
            if len(row) < 4:
                failures.append("Diversified Search Batch Plan row has too few columns")
                continue
            integration = row[3].lower()
            if not any(target in integration for target in REQUIRED_BATCH_INTEGRATION_TARGETS):
                failures.append("Diversified Search Batch Plan row missing record integration mapping")
        if (
            "official-primary" not in batch_text
            and "official" not in batch_text
            and "source-of-truth" not in batch_text
        ):
            failures.append("Diversified Search Batch Plan missing official/source-of-truth family")
        if "counterevidence" not in batch_text:
            failures.append("Diversified Search Batch Plan missing counterevidence family")
        if "currentness" not in batch_text:
            failures.append("Diversified Search Batch Plan missing currentness family")
        if "provenance" not in batch_text and "source-lineage" not in batch_text:
            failures.append("Diversified Search Batch Plan missing provenance/source-lineage family")
        if "frontier-expansion" not in batch_text:
            failures.append("Diversified Search Batch Plan missing frontier-expansion family")
        if "blocked-source-recovery" not in batch_text:
            failures.append("Diversified Search Batch Plan missing blocked-source-recovery family")
        if not args.allow_placeholders:
            if "sub-batches" not in batch_text:
                failures.append("Diversified Search Batch Plan missing execution sub-batch details")
            if "queries" not in batch_text:
                failures.append("Diversified Search Batch Plan missing query count details")
            if not re.search(r"up to \d+", batch_text):
                failures.append("Diversified Search Batch Plan missing numeric tool-limit detail")
            if not re.search(r"\bsb\d+\b", batch_text):
                failures.append("Diversified Search Batch Plan missing SB execution group labels")

        domain_rows = parse_markdown_rows(section_body(text, "Domain Coverage Matrix"))
        if len(domain_rows) <= 1:
            failures.append("Domain Coverage Matrix must include at least one domain row")
        for row in domain_rows[1:]:
            if len(row) < 4:
                failures.append("Domain Coverage Matrix row has too few columns")
                continue
            status = row[3].lower()
            # Planned domain rows do not pass final validation.
            if not args.allow_placeholders and status == "planned":
                failures.append("Domain Coverage Matrix row remains planned instead of resolved")
            if status not in ALLOWED_DOMAIN_COVERAGE_STATUS:
                failures.append(
                    f"Domain Coverage Matrix has invalid status {row[3]!r}"
                )

        locale_rows = parse_markdown_rows(section_body(text, "Language And Locale Audit"))
        if len(locale_rows) <= 1:
            failures.append("Language And Locale Audit must include at least one locale row")
        for row in locale_rows[1:]:
            if len(row) < 5:
                failures.append("Language And Locale Audit row has too few columns")
                continue
            status = row[4].lower()
            # Planned language/locale rows do not pass final validation.
            if not args.allow_placeholders and status == "planned":
                failures.append("Language And Locale Audit row remains planned instead of resolved")
            if status not in ALLOWED_LANGUAGE_LOCALE_STATUS:
                failures.append(
                    f"Language And Locale Audit has invalid status {row[4]!r}"
                )

        entity_rows = parse_markdown_rows(section_body(text, "Entity And Terminology Audit"))
        if len(entity_rows) <= 1:
            failures.append("Entity And Terminology Audit must include at least one entity/term row")
        for row in entity_rows[1:]:
            if len(row) < 6:
                failures.append("Entity And Terminology Audit row has too few columns")
                continue
            status = row[5].lower()
            if status not in ALLOWED_ENTITY_TERMINOLOGY_STATUS:
                failures.append(
                    f"Entity And Terminology Audit has invalid status {row[5]!r}"
                )

        retrieval_rows = parse_markdown_rows(section_body(text, "Access And Retrieval Audit"))
        if len(retrieval_rows) <= 1:
            failures.append("Access And Retrieval Audit must include at least one retrieval row")
        for row in retrieval_rows[1:]:
            if len(row) < 5:
                failures.append("Access And Retrieval Audit row has too few columns")
                continue
            retrieval_status = row[4].lower()
            if retrieval_status not in ALLOWED_RETRIEVAL_STATUS:
                failures.append(
                    f"Access And Retrieval Audit has invalid retrieval status {row[4]!r}"
                )

        triage_rows = parse_markdown_rows(section_body(text, "Search Result Triage"))
        if len(triage_rows) <= 1:
            failures.append("Search Result Triage must include at least one result row")
        for row in triage_rows[1:]:
            if len(row) < 4:
                failures.append("Search Result Triage row has too few columns")
                continue
            classification = row[3].lower()
            if classification not in ALLOWED_TRIAGE_CLASSES:
                failures.append(
                    f"Search Result Triage has invalid classification {row[3]!r}"
                )

        lead_rows = parse_markdown_rows(section_body(text, "Lead Ledger"))
        if len(lead_rows) <= 1:
            failures.append("Lead Ledger must include at least one lead row")
        for row in lead_rows[1:]:
            if len(row) < 6:
                failures.append("Lead Ledger row has too few columns")
                continue
            action = row[4].lower()
            outcome = row[5].lower()
            if action not in ALLOWED_LEAD_ACTIONS:
                failures.append(f"Lead Ledger has invalid or open action {row[4]!r}")
            if not args.allow_placeholders and outcome == "unresolved":
                failures.append("Lead Ledger outcome remains unresolved instead of closed or downgraded")

        debt_rows = parse_markdown_rows(section_body(text, "Coverage Debt"))
        if len(debt_rows) <= 1:
            failures.append("Coverage Debt must include at least one debt row")
        for row in debt_rows[1:]:
            if len(row) < 7:
                failures.append("Coverage Debt row has too few columns")
                continue
            status = row[5].lower()
            if not args.allow_placeholders and status == "open":
                failures.append("Coverage Debt row remains open instead of cleared, blocked, or downgraded")
            if status not in ALLOWED_COVERAGE_DEBT_STATUS:
                failures.append(f"Coverage Debt has invalid status {row[5]!r}")

        search_bias_rows = parse_markdown_rows(section_body(text, "Search Bias And Retrieval Trap Audit"))
        if len(search_bias_rows) <= 1:
            failures.append("Search Bias And Retrieval Trap Audit must include at least one row")
        for row in search_bias_rows[1:]:
            if len(row) < 7:
                failures.append("Search Bias And Retrieval Trap Audit row has too few columns")
                continue
            status = row[6].lower()
            if status not in ALLOWED_SEARCH_BIAS_STATUS:
                failures.append(
                    f"Search Bias And Retrieval Trap Audit has invalid status {row[6]!r}"
                )

        selection_rows = parse_markdown_rows(section_body(text, "Selection And Inclusion Audit"))
        if len(selection_rows) <= 1:
            failures.append("Selection And Inclusion Audit must include at least one row")
        for row in selection_rows[1:]:
            if len(row) < 8:
                failures.append("Selection And Inclusion Audit row has too few columns")
                continue
            status = row[7].lower()
            if status not in ALLOWED_SELECTION_STATUS:
                failures.append(
                    f"Selection And Inclusion Audit has invalid status {row[7]!r}"
                )

        lineage_rows = parse_markdown_rows(section_body(text, "Source Lineage Map"))
        if len(lineage_rows) <= 1:
            failures.append("Source Lineage Map must include at least one lineage row")
        for row in lineage_rows[1:]:
            if len(row) < 4:
                failures.append("Source Lineage Map row has too few columns")
                continue
            status = row[3].lower()
            if status not in ALLOWED_LINEAGE_STATUS:
                failures.append(
                    f"Source Lineage Map has invalid independence status {row[3]!r}"
                )

        quality_rows = parse_markdown_rows(section_body(text, "Source Quality Audit"))
        if len(quality_rows) <= 1:
            failures.append("Source Quality Audit must include at least one source row")
        for row in quality_rows[1:]:
            if len(row) < 7:
                failures.append("Source Quality Audit row has too few columns")
                continue
            overall_status = row[6].lower()
            if overall_status not in ALLOWED_SOURCE_QUALITY_STATUS:
                failures.append(
                    f"Source Quality Audit has invalid overall status {row[6]!r}"
                )

        corroboration_rows = parse_markdown_rows(section_body(text, "Corroboration And Triangulation Audit"))
        if len(corroboration_rows) <= 1:
            failures.append("Corroboration And Triangulation Audit must include at least one claim row")
        for row in corroboration_rows[1:]:
            if len(row) < 7:
                failures.append("Corroboration And Triangulation Audit row has too few columns")
                continue
            status = row[6].lower()
            if status not in ALLOWED_CORROBORATION_STATUS:
                failures.append(
                    f"Corroboration And Triangulation Audit has invalid status {row[6]!r}"
                )

        consensus_rows = parse_markdown_rows(section_body(text, "Consensus And Disagreement Audit"))
        if len(consensus_rows) <= 1:
            failures.append("Consensus And Disagreement Audit must include at least one row")
        for row in consensus_rows[1:]:
            if len(row) < 9:
                failures.append("Consensus And Disagreement Audit row has too few columns")
                continue
            status = row[7].lower()
            if status not in ALLOWED_CONSENSUS_DISAGREEMENT_STATUS:
                failures.append(
                    f"Consensus And Disagreement Audit has invalid status {row[7]!r}"
                )

        incentive_rows = parse_markdown_rows(section_body(text, "Source Incentive And Bias Audit"))
        if len(incentive_rows) <= 1:
            failures.append("Source Incentive And Bias Audit must include at least one row")
        for row in incentive_rows[1:]:
            if len(row) < 6:
                failures.append("Source Incentive And Bias Audit row has too few columns")
                continue
            status = row[5].lower()
            if status not in ALLOWED_SOURCE_INCENTIVE_STATUS:
                failures.append(
                    f"Source Incentive And Bias Audit has invalid status {row[5]!r}"
                )

        manipulation_rows = parse_markdown_rows(section_body(text, "Source Manipulation And Adversarial Provenance Audit"))
        if len(manipulation_rows) <= 1:
            failures.append("Source Manipulation And Adversarial Provenance Audit must include at least one row")
        for row in manipulation_rows[1:]:
            if len(row) < 8:
                failures.append("Source Manipulation And Adversarial Provenance Audit row has too few columns")
                continue
            status = row[7].lower()
            if status not in ALLOWED_MANIPULATION_PROVENANCE_STATUS:
                failures.append(
                    f"Source Manipulation And Adversarial Provenance Audit has invalid status {row[7]!r}"
                )

        quantitative_rows = parse_markdown_rows(section_body(text, "Quantitative And Measurement Audit"))
        if len(quantitative_rows) <= 1:
            failures.append("Quantitative And Measurement Audit must include at least one row")
        for row in quantitative_rows[1:]:
            if len(row) < 8:
                failures.append("Quantitative And Measurement Audit row has too few columns")
                continue
            status = row[7].lower()
            if status not in ALLOWED_QUANTITATIVE_STATUS:
                failures.append(
                    f"Quantitative And Measurement Audit has invalid status {row[7]!r}"
                )

        currentness_rows = parse_markdown_rows(section_body(text, "Currentness And Version Audit"))
        if len(currentness_rows) <= 1:
            failures.append("Currentness And Version Audit must include at least one row")
        for row in currentness_rows[1:]:
            if len(row) < 5:
                failures.append("Currentness And Version Audit row has too few columns")
                continue
            status = row[4].lower()
            if status not in ALLOWED_CURRENTNESS_STATUS:
                failures.append(
                    f"Currentness And Version Audit has invalid status {row[4]!r}"
                )

        reproducibility_rows = parse_markdown_rows(section_body(text, "Reproducibility And Refresh Audit"))
        if len(reproducibility_rows) <= 1:
            failures.append("Reproducibility And Refresh Audit must include at least one row")
        for row in reproducibility_rows[1:]:
            if len(row) < 7:
                failures.append("Reproducibility And Refresh Audit row has too few columns")
                continue
            status = row[6].lower()
            if status not in ALLOWED_REPRODUCIBILITY_STATUS:
                failures.append(
                    f"Reproducibility And Refresh Audit has invalid status {row[6]!r}"
                )

        saturation_rows = parse_markdown_rows(section_body(text, "Saturation Metrics"))
        if len(saturation_rows) <= 1:
            failures.append("Saturation Metrics must include at least one metric row")
        metric_names = {
            normalize(row[0]).lower()
            for row in saturation_rows[1:]
            if row
        }
        for metric in REQUIRED_SATURATION_METRICS:
            if metric not in metric_names:
                failures.append(
                    f"Saturation Metrics missing required metric {metric!r}"
                )
        for row in saturation_rows[1:]:
            if len(row) < 4:
                failures.append("Saturation Metrics row has too few columns")
                continue
            status = row[3].lower()
            if not args.allow_placeholders and status in {"not met", "not-met"}:
                failures.append("Saturation Metrics row remains not met in final record")
            if status not in ALLOWED_SATURATION_METRIC_STATUS:
                failures.append(
                    f"Saturation Metrics has invalid status {row[3]!r}"
                )

        source_follow_rows = parse_markdown_rows(
            section_body(text, "Source-Opened Follow-Up Audit")
        )
        if len(source_follow_rows) <= 1:
            failures.append("Source-Opened Follow-Up Audit must include at least one row")
        for row in source_follow_rows[1:]:
            if len(row) < 7:
                failures.append("Source-Opened Follow-Up Audit row has too few columns")
                continue
            action = row[5].lower()
            if action not in ALLOWED_SOURCE_OPENED_FOLLOW_UP_ACTIONS:
                failures.append(
                    f"Source-Opened Follow-Up Audit has invalid action {row[5]!r}"
                )
            if not args.allow_placeholders and action in {"planned", "open", "unresolved"}:
                failures.append(
                    "Source-Opened Follow-Up Audit action remains planned/open/unresolved instead of closed, followed, blocked, or downgraded"
                )

        frontier_rows = parse_markdown_rows(section_body(text, "Expansion Frontier Audit"))
        if len(frontier_rows) <= 1:
            failures.append("Expansion Frontier Audit must include at least one row")
        for row in frontier_rows[1:]:
            if len(row) < 7:
                failures.append("Expansion Frontier Audit row has too few columns")
                continue
            status = row[6].lower()
            if not args.allow_placeholders and status == "planned":
                failures.append("Expansion Frontier Audit frontier remains planned instead of closed")
            if status not in ALLOWED_EXPANSION_FRONTIER_STATUS:
                failures.append(
                    f"Expansion Frontier Audit has invalid status {row[6]!r}"
                )

        location_rows = parse_markdown_rows(section_body(text, "Evidence Location Audit"))
        if len(location_rows) <= 1:
            failures.append("Evidence Location Audit must include at least one row")
        for row in location_rows[1:]:
            if len(row) < 4:
                failures.append("Evidence Location Audit row has too few columns")
                continue
            status = row[3].lower()
            if status not in ALLOWED_EVIDENCE_LOCATION_STATUS:
                failures.append(
                    f"Evidence Location Audit has invalid locator status {row[3]!r}"
                )

        quotation_rows = parse_markdown_rows(section_body(text, "Quotation And Context Audit"))
        if len(quotation_rows) <= 1:
            failures.append("Quotation And Context Audit must include at least one row")
        for row in quotation_rows[1:]:
            if len(row) < 8:
                failures.append("Quotation And Context Audit row has too few columns")
                continue
            status = row[7].lower()
            if status not in ALLOWED_QUOTATION_CONTEXT_STATUS:
                failures.append(
                    f"Quotation And Context Audit has invalid status {row[7]!r}"
                )

        absence_rows = parse_markdown_rows(section_body(text, "Absence Evidence Audit"))
        if len(absence_rows) <= 1:
            failures.append("Absence Evidence Audit must include at least one row")
        for row in absence_rows[1:]:
            if len(row) < 4:
                failures.append("Absence Evidence Audit row has too few columns")
                continue
            result = row[3].lower()
            if result not in ALLOWED_ABSENCE_RESULT:
                failures.append(
                    f"Absence Evidence Audit has invalid absence result {row[3]!r}"
                )

        claim_rows = parse_markdown_rows(section_body(text, "Claim Ledger"))
        if len(claim_rows) <= 1:
            failures.append("Claim Ledger must include at least one claim row")
        for row in claim_rows[1:]:
            if len(row) < 10:
                failures.append("Claim Ledger row has too few columns")
                continue
            gate = row[7].lower()
            confidence = row[8].lower()
            decision = row[9].lower()
            if gate not in ALLOWED_VERIFIED_CLAIM_GATE:
                failures.append(
                    f"Claim Ledger has invalid verified-claim gate {row[7]!r}"
                )
            if confidence not in ALLOWED_CALIBRATED_CONFIDENCE:
                failures.append(f"Claim Ledger has invalid confidence {row[8]!r}")
            if decision not in ALLOWED_CLAIM_LEDGER_DECISIONS:
                failures.append(f"Claim Ledger has invalid decision {row[9]!r}")
            if not args.allow_placeholders and decision == "unresolved":
                failures.append(
                    "Claim Ledger decision remains unresolved instead of use, downgrade, exclude, or insufficient"
                )

        risk_rows = parse_markdown_rows(section_body(text, "Claim Risk Triage"))
        if len(risk_rows) <= 1:
            failures.append("Claim Risk Triage must include at least one claim row")
        for row in risk_rows[1:]:
            if len(row) < 4:
                failures.append("Claim Risk Triage row has too few columns")
                continue
            priority = row[3].lower()
            if priority not in ALLOWED_CLAIM_TRIAGE_PRIORITY:
                failures.append(
                    f"Claim Risk Triage has invalid verification priority {row[3]!r}"
                )

        trace_rows = parse_markdown_rows(section_body(text, "Claim Traceability Matrix"))
        if len(trace_rows) <= 1:
            failures.append("Claim Traceability Matrix must include at least one claim row")
        for row in trace_rows[1:]:
            if len(row) < 2:
                failures.append("Claim Traceability Matrix row has too few columns")
                continue
            decision = row[1].lower()
            if decision not in ALLOWED_TRACE_DECISIONS:
                failures.append(
                    f"Claim Traceability Matrix has invalid final decision {row[1]!r}"
                )
            if not args.allow_placeholders and decision == "unresolved":
                failures.append(
                    "Claim Traceability Matrix final decision remains unresolved instead of use, downgrade, exclude, or insufficient"
                )

        inference_rows = parse_markdown_rows(section_body(text, "Inference Boundary Audit"))
        if len(inference_rows) <= 1:
            failures.append("Inference Boundary Audit must include at least one claim row")
        for row in inference_rows[1:]:
            if len(row) < 6:
                failures.append("Inference Boundary Audit row has too few columns")
                continue
            status = row[5].lower()
            if status not in ALLOWED_INFERENCE_BOUNDARY_STATUS:
                failures.append(
                    f"Inference Boundary Audit has invalid status {row[5]!r}"
                )

        assumption_rows = parse_markdown_rows(section_body(text, "Assumption And Sensitivity Audit"))
        if len(assumption_rows) <= 1:
            failures.append("Assumption And Sensitivity Audit must include at least one row")
        for row in assumption_rows[1:]:
            if len(row) < 7:
                failures.append("Assumption And Sensitivity Audit row has too few columns")
                continue
            status = row[6].lower()
            if status not in ALLOWED_ASSUMPTION_SENSITIVITY_STATUS:
                failures.append(
                    f"Assumption And Sensitivity Audit has invalid status {row[6]!r}"
                )

        conflict_rows = parse_markdown_rows(section_body(text, "Conflict Resolution Matrix"))
        if len(conflict_rows) <= 1:
            failures.append("Conflict Resolution Matrix must include at least one conflict row")
        for row in conflict_rows[1:]:
            if len(row) < 6:
                failures.append("Conflict Resolution Matrix row has too few columns")
                continue
            resolution = row[5].lower()
            if resolution not in ALLOWED_CONFLICT_RESOLUTION:
                failures.append(
                    f"Conflict Resolution Matrix has invalid resolution {row[5]!r}"
                )

        calibration_rows = parse_markdown_rows(section_body(text, "Confidence Calibration"))
        if len(calibration_rows) <= 1:
            failures.append("Confidence Calibration must include at least one claim row")
        for row in calibration_rows[1:]:
            if len(row) < 9:
                failures.append("Confidence Calibration row has too few columns")
                continue
            confidence = row[8].lower()
            if confidence not in ALLOWED_CALIBRATED_CONFIDENCE:
                failures.append(
                    f"Confidence Calibration has invalid calibrated confidence {row[8]!r}"
                )

        synthesis_rows = parse_markdown_rows(section_body(text, "Synthesis Traceability Audit"))
        if len(synthesis_rows) <= 1:
            failures.append("Synthesis Traceability Audit must include at least one row")
        for row in synthesis_rows[1:]:
            if len(row) < 7:
                failures.append("Synthesis Traceability Audit row has too few columns")
                continue
            status = row[6].lower()
            if status not in ALLOWED_SYNTHESIS_TRACE_STATUS:
                failures.append(
                    f"Synthesis Traceability Audit has invalid status {row[6]!r}"
                )

        adversarial_rows = parse_markdown_rows(section_body(text, "Adversarial Review"))
        if len(adversarial_rows) <= 1:
            failures.append("Adversarial Review must include at least one review row")
        for row in adversarial_rows[1:]:
            if len(row) < 6:
                failures.append("Adversarial Review row has too few columns")
                continue
            outcome = row[5].lower()
            if outcome not in ALLOWED_ADVERSARIAL_OUTCOME:
                failures.append(
                    f"Adversarial Review has invalid outcome {row[5]!r}"
                )

        stop_rows = parse_markdown_rows(section_body(text, "Stop Rule Audit"))
        if len(stop_rows) <= 1:
            failures.append("Stop Rule Audit must include at least one stop-rule row")
        for row in stop_rows[1:]:
            if len(row) < 4:
                failures.append("Stop Rule Audit row has too few columns")
                continue
            status = row[3].lower()
            if not args.allow_placeholders and status == "not satisfied":
                failures.append("Stop Rule Audit remains not satisfied in final record")
            if status not in ALLOWED_STOP_RULE_STATUS:
                failures.append(
                    f"Stop Rule Audit has invalid status {row[3]!r}"
                )

        distortion_rows = parse_markdown_rows(section_body(text, "Distortion Pattern Audit"))
        if len(distortion_rows) <= 1:
            failures.append("Distortion Pattern Audit must include at least one row")
        for row in distortion_rows[1:]:
            if len(row) < 4:
                failures.append("Distortion Pattern Audit row has too few columns")
                continue
            status = row[3].lower()
            if status not in ALLOWED_DISTORTION_STATUS:
                failures.append(
                    f"Distortion Pattern Audit has invalid status {row[3]!r}"
                )

    if not args.allow_placeholders:
        for sibling in record.parent.iterdir():
            if sibling == record:
                continue
            if sibling.is_dir():
                failures.append(
                    f"sibling directory violates single-record contract: {sibling.name}"
                )
            elif sibling.name.lower() in FORBIDDEN_SIBLING_NAMES:
                failures.append(
                    f"sibling sidecar file violates single-record contract: {sibling.name}"
                )
            elif sibling.suffix.lower() == ".md" and not RECORD_FILENAME_PATTERN.match(sibling.name):
                failures.append(
                    f"sibling markdown file must match <NNN-ascii-slug>.md: {sibling.name}"
                )
            elif sibling.suffix.lower() != ".md" and not sibling.name.startswith("."):
                failures.append(
                    f"sibling non-Markdown artifact violates single-record contract: {sibling.name}"
                )
        for pattern in PLACEHOLDER_PATTERNS:
            if re.search(pattern, text):
                failures.append(f"placeholder remains: {pattern}")
        sidecar_scan_text = text_without_urls(text).lower()
        for pattern in FORBIDDEN_SIDECAR_PATTERNS:
            if re.search(pattern, sidecar_scan_text):
                failures.append(f"sidecar artifact reference violates single-record contract: {pattern}")

    if failures:
        print("Research record validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Research record validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
