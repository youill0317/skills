#!/usr/bin/env python3
"""Verify the research skill's hard contract.

This is a maintenance check for the skill package, not part of a research run.
It fails if edits remove the two governing requirements or the sections that
make the skill stronger than ordinary deep-research prompts.
"""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]


CHECKS: dict[str, list[str]] = {
    "SKILL.md": [
        "Maximum-saturation evidence research with a single Markdown record",
        "Always drive the available web/search/connectors to their practical limit",
        "always use the strongest available research protocol",
        "produce exactly one Markdown research record",
        "No Mode/Routing Guardrail",
        "do not introduce quick, deep, academic, lightweight",
        "Under-research is the primary failure mode",
        "One explicit research request maps to one Markdown record",
        "Do not create multiple sibling records",
        "High-volume research does not relax this contract",
        "sidecar artifacts",
        "Saturation-Orchestration Requirements",
        "Saturation Metrics",
        "Expansion Frontier Audit",
        "Absence Evidence Audit",
        "Quotation And Context Audit",
        "Question Coverage Audit",
        "Entity And Terminology Audit",
        "Inference Boundary Audit",
        "Assumption And Sensitivity Audit",
        "Conflict Resolution Matrix",
        "Harness Max-Use Rule",
        "frontier queue",
        "query_matrix.py --topic",
        "--format batches",
        "Search-Tool Maximization",
        "batch independent search queries",
        "minimum three-pass diversified search portfolio",
        "search counts alone never prove saturation",
        "after opening any high-value source",
        "every high-value opened source represented",
        "official/source-of-truth",
        "frontier-expansion plus blocked-source-recovery",
        "Preserve the generated execution sub-batches",
        "numeric active tool limit",
        "SB1",
        "web-search-harness-maximization.md",
        "Do not ask the user to choose a research depth",
        "worker-wave plan",
        "thin lane result",
        "coverage debt",
        "EXPAND lead loop",
        "counter-search",
        "verified-claim gate",
        "third-party skills, plugins, repos, scripts, prompts",
    ],
    "references/research-process.md": [
        "Search Craft Floors",
        "There are no research modes",
        "Do not introduce quick, deep, academic, lightweight",
        "Domain references add cumulative gates",
        "Dispatch independent discovery queries in batches",
        "web-search-harness-maximization.md",
        "at least two search cycles per major theme",
        "12+ for narrow research, 25+ for broad or",
        "50+ for very broad diligence",
        "Prior-Record Reuse",
        "Atomic Claim Verification",
        "Worker-Wave Pressure And Coverage Debt",
        "thin lane result",
        "Coverage Debt",
        "Expansion Frontier Audit",
        "Frontier Queue And Convergence",
        "frontier queue convergence",
        "Search Ladder",
        "Lead Expansion Rules",
        "EXPAND is a loop, not a single pass",
        "Verified-Claim Gate",
        "Saturation Completeness Gate",
        "Saturation Metrics",
        "Expansion Frontier Audit",
        "Absence Evidence Audit",
        "Quotation And Context Audit",
        "Question Coverage Audit",
        "Entity And Terminology Audit",
        "Inference Boundary Audit",
        "Assumption And Sensitivity Audit",
        "Conflict Resolution Matrix",
        "Stop Rule",
    ],
    "references/research-record-template.md": [
        "Do not create a topic folder",
        "Evidence Maturity Dashboard",
        "Decision Usefulness Matrix",
        "Comparison And Evaluation Audit",
        "Question Coverage Audit",
        "Entity And Terminology Audit",
        "Tool Capability Audit",
        "batch / parallel diversified search",
        "source retrieval fallback",
        "Search Matrix",
        "Final Status",
        "Diversified Search Batch Plan",
        "SB1",
        "tool-limit note",
        "sub-batches of up to tool-limit",
        "Domain Coverage Matrix",
        "Language And Locale Audit",
        "Worker Wave Plan",
        "Search Craft Log",
        "Search Result Triage",
        "Search Bias And Retrieval Trap Audit",
        "Selection And Inclusion Audit",
        "Access And Retrieval Audit",
        "Prior Record Check",
        "Wave Log",
        "Lead Ledger",
        "Source-Opened Follow-Up Audit",
        "Expansion Frontier Audit",
        "Coverage Debt",
        "Worker Wave Test",
        "Question Coverage Test",
        "Unanswered rows do not pass final validation",
        "Search Matrix Completion Test",
        "Saturation Metrics Test",
        "Entity And Terminology Test",
        "Decision Usefulness Test",
        "Evidence Maturity Dashboard Test",
        "Comparison And Evaluation Test",
        "Tool Capability Test",
        "Diversified Search Batch Test",
        "execution sub-batches",
        "tool-limit notes",
        "Domain Coverage Test",
        "Language And Locale Test",
        "Search Result Triage Test",
        "Search Bias And Retrieval Trap Test",
        "Selection And Inclusion Test",
        "Access And Retrieval Test",
        "Source-Opened Follow-Up Test",
        "Source Lineage Map",
        "Source Lineage Map Test",
        "Source Quality Audit",
        "Source Quality Audit Test",
        "Corroboration And Triangulation Audit",
        "Consensus And Disagreement Audit",
        "Corroboration And Triangulation Test",
        "Consensus And Disagreement Test",
        "Source Incentive And Bias Audit",
        "Source Manipulation And Adversarial Provenance Audit",
        "Source Incentive And Bias Test",
        "Source Manipulation And Adversarial Provenance Test",
        "Quantitative And Measurement Audit",
        "Quantitative And Measurement Test",
        "Currentness And Version Audit",
        "Currentness And Version Audit Test",
        "Reproducibility And Refresh Audit",
        "Reproducibility And Refresh Test",
        "Evidence Location Audit",
        "Evidence Location Audit Test",
        "Quotation And Context Audit",
        "Quotation And Context Test",
        "Expansion Frontier Audit",
        "Expansion Frontier Test",
        "Frontier Queue Convergence Test",
        "frontier queue convergence",
        "Absence Evidence Audit",
        "Absence Evidence Test",
        "Source Coverage",
        "Saturation Metrics",
        "Observation Manifest",
        "Claim Ledger",
        "final validation requires every Claim Ledger decision",
        "Final Claim Traceability decisions cannot remain `unresolved`",
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
        "Atomic Claim Decomposition",
        "Verified Claims",
        "Coverage Debt Test",
        "Coverage Gates",
        "Acceptance Tests",
        "Required rows that remain `fail` do not pass final validation",
        "concrete reason, evidence/location, remediation",
    ],
    "references/subagent-orchestration.md": [
        "single-record contract",
        "lane floors",
        "first wave together",
        "worker-wave discipline",
        "thin worker output",
        "coverage debt",
        "default stop-when-answered behavior does not apply",
        "include an `## EXPAND` tail",
        "include `## CLAIMS`",
        "EXPAND Follow-Up",
        "frontier queue convergence audit",
        "frontier queue convergence",
        "verified-claim audit",
    ],
    "references/acceptance-tests.md": [
        "Single Markdown Record Test",
        "Required tests that remain `fail` do not pass final validation",
        "concrete reason, evidence/location, remediation",
        "Saturation Protocol Test",
        "Question Coverage Test",
        "Search Matrix Completion Test",
        "Saturation Metrics Test",
        "Metrics that remain `not met` do not pass final validation",
        "Decision Usefulness Test",
        "Evidence Maturity Dashboard Test",
        "Comparison And Evaluation Test",
        "Tool Capability Test",
        "Diversified Search Batch Test",
        "Domain Coverage Test",
        "Language And Locale Test",
        "Search Craft Floor Test",
        "Source Coverage Floor Test",
        "Source Lineage Map Test",
        "Source Quality Audit Test",
        "Quantitative And Measurement Test",
        "Currentness And Version Audit Test",
        "Evidence Location Audit Test",
        "Quotation And Context Test",
        "Absence Evidence Test",
        "Claim Risk Triage Test",
        "Claim Traceability Test",
        "Unresolved final Claim Ledger or Claim Traceability decisions do not pass final validation",
        "Inference Boundary Test",
        "Assumption And Sensitivity Test",
        "Conflict Resolution Test",
        "Confidence Calibration Test",
        "Synthesis Traceability Test",
        "Adversarial Review Test",
        "Stop Rule Audit Test",
        "Stop-rule rows",
        "Atomic Claim Decomposition Test",
        "Distortion Pattern Audit Test",
        "Worker Wave Test",
        "Search Result Triage Test",
        "Search Bias And Retrieval Trap Test",
        "Access And Retrieval Test",
        "Source-Opened Follow-Up Test",
        "Lead Ledger / EXPAND Test",
        "Open actions or unresolved final lead outcomes do not pass final validation",
        "Expansion Frontier Test",
        "Planned frontier rows do not pass final validation",
        "Frontier Queue Convergence Test",
        "Coverage Debt Test",
        "Open coverage debt rows do not pass final validation",
        "Verified-Claim Gate Test",
    ],
    "references/quality-rubric.md": [
        "of one Markdown research record",
        "skips the search matrix, lane plan, EXPAND lead loop",
        "frontier queue convergence",
        "high-risk non-code claim is stated firmly without passing",
        "Search saturation and reproducibility",
    ],
    "references/professional-research-quality.md": [
        "Search Craft Log and Wave Log include scout, target, snowball, EXPAND, counter-search",
        "Saturation Metrics",
        "Absence Evidence",
        "Question Coverage Audit",
        "Entity And Terminology Audit",
        "Inference Boundary Audit",
        "Conflict Resolution Matrix",
        "Quantitative And Measurement Audit",
        "Source Incentive And Bias Audit",
        "Source Manipulation And Adversarial Provenance Audit",
        "Claim Ledger",
        "Lead Ledger",
        "Expansion Frontier Audit",
        "Frontier Queue Convergence",
        "Decision Usefulness",
        "Comparison And Evaluation Audit",
        "Tool Capability Audit",
        "Access And Retrieval",
        "Currentness And Version Audit",
        "Reproducibility And Refresh Audit",
        "Evidence Location Audit",
        "Quotation And Context Audit",
        "Language And Locale Audit",
        "Source Lineage Mapping",
        "Claim Risk Triage",
        "Did the record prove harness max-use",
        "diversified batch execution with numeric sub-batches",
        "Distortion Pattern Audit",
        "Confidence Calibration",
        "Synthesis Traceability Audit",
        "Corroboration And Triangulation Audit",
        "Consensus And Disagreement Audit",
        "Adversarial Review",
        "Stop Rule Audit",
    ],
    "references/qa-iteration-loop.md": [
        "single record",
        "## Search Craft Log",
        "## Tool Capability Audit",
        "## Diversified Search Batch Plan",
        "## Lead Ledger",
        "## Source-Opened Follow-Up Audit",
        "Frontier Queue Convergence",
        "## Claim Ledger",
        "harness max-use",
        "search-pressure gap pass",
    ],
    "references/sample-scenarios.md": [
        "one Markdown record",
        "## Search Matrix",
        "frontier queue convergence",
        "## Claim Ledger",
    ],
    "references/final-deliverable-standards.md": [
        "consolidated into one Markdown research",
        "high-risk non-code claims stated firmly have a verified-claim gate result",
        "search matrix, lane coverage, EXPAND leads, counter-search",
        "frontier queue convergence",
        "harness max-use is visible",
        "numeric tool limits and execution sub-batches",
        "claiming saturation without showing actual query diversity",
        "source coverage is adequate for the scope",
        "Synthesis Traceability Audit",
    ],
    "references/evidence-needs-core.md": [
        "Evidence Needs Core",
        "authoritative-record",
        "lead-expansion",
        "source-retrieval",
        "counterevidence",
        "claim-provenance",
        "source-retrieval decision",
    ],
    "references/query-and-source-patterns.md": [
        "Query And Source Patterns",
        "query_matrix.py",
        "--format batches",
        "frontier-expansion",
        "blocked-source-recovery",
        "expansive-research.md",
    ],
    "references/expansive-research.md": [
        "Expansive Research",
        "not a separate mode",
        "single Markdown research record",
        "frontier queue item",
        "blocked-source",
        "frontier queue convergence",
    ],
    "references/scholarly-search-and-literature-review.md": [
        "Scholarly Search And Literature Review",
        "scholarly frontier queue",
        "blocked full text",
        "backward and forward citation chasing",
        "retraction or expression-of-concern",
    ],
    "references/source-provenance-and-archives.md": [
        "Source Provenance And Archives",
        "authorized alternates",
        "open frontier item",
        "Archive Capture Reliability",
        "Mutable Internal Sources",
    ],
    "references/current-events.md": [
        "Current Events",
        "current-event frontier queue",
        "as-of timestamp",
        "corrections, retractions, denials",
    ],
    "references/data-statistics-and-surveys.md": [
        "Data, Statistics, And Surveys",
        "source-retrieval frontier items",
        "denominator",
        "methodology notes",
        "decision-ready",
    ],
    "references/profiles-and-identity.md": [
        "Profiles And Identity",
        "identity frontier queue",
        "same-name and lookalike exclusions",
        "source-retrieval frontier items",
        "impersonation",
    ],
    "references/multilingual-research.md": [
        "Multilingual And Local-Language Research",
        "multilingual frontier queue",
        "native-script",
        "local-language frontier",
        "translation differences",
    ],
    "references/policy-regulatory-legal.md": [
        "Policy, Regulatory, And Legal Landscape",
        "policy/legal frontier queue",
        "source-retrieval frontier items",
        "authority hierarchy",
        "applicability per jurisdiction",
    ],
    "references/competitive-market-analysis.md": [
        "Competitive And Market Analysis",
        "market frontier queue",
        "source-retrieval",
        "blocked reports",
        "comparison",
    ],
    "references/public-sentiment-and-behavior.md": [
        "Public Sentiment And Behavior Traces",
        "behavior-trace frontier queue",
        "source-retrieval",
        "Sampling And Manipulation Checks",
        "representativeness",
    ],
    "references/source-verification.md": [
        "Third-Party Skill, Prompt, Plugin, And Script Safety",
        "Blocked Source Recovery",
        "Atomic Claims And Distortion Patterns",
        "evidence strength",
        "Do not execute third-party code",
        "Treat a skill's description, trigger language, README",
    ],
    "references/high-stakes-domain-protocols.md": [
        "High-Stakes Domain Protocols",
        "Cross-Domain Rule",
        "frontier queue leads",
        "owner/SME review",
        "Clinical / Medical",
        "Financial / Investment Diligence",
        "OSINT / Investigative Research",
        "Security / Technical Diligence",
    ],
    "references/competitive-baselines.md": [
        "Competitive Baselines",
        "code-yeongyu/oh-my-openagent",
        "orhoncan/oneshot-academic-research-skill",
        "realnaka/claim-verification",
        "frontier queue convergence",
        "Expansion Frontier Audit",
        "Superset Scorecard",
        "Web Search Harness Playbook",
        "Diversified Batch Portfolio",
        "No Sidecar Spillover",
        "Sidecar control",
        "Mode Regression Guardrail",
        "quick/deep/academic",
        "minimum three-pass portfolio",
        "frontier-expansion plus blocked-source-recovery",
        "Single Markdown Record",
        "Do not copy mode routing",
    ],
    "references/enterprise-research-operations.md": [
        "Enterprise Research Operations",
        "single Markdown research record",
        "frontier queue convergence",
        "permission-aware",
        "Decision Matrix",
        "Quality Gates",
    ],
    "references/enterprise-search-and-synthesis.md": [
        "Enterprise Search And Knowledge Synthesis",
        "Research records belong at",
        "frontier queue",
        "Enterprise Frontier Queue",
        "not accessible",
        "Decision-use status",
    ],
    "references/web-search-harness-maximization.md": [
        "Web Search Harness Maximization",
        "Harness Max-Use Rule",
        "Batch Search Discipline",
        "query_matrix.py --format batches",
        "Minimum Search Pressure Before Synthesis",
        "Search counts alone do not satisfy this floor",
        "Frontier Queue Discipline",
        "Query Portfolio",
        "Saturation Metrics",
        "Expansion Frontier Audit",
        "Absence Evidence",
        "Source Opening Ladder",
        "Open, Find, And Extract",
        "Source-Opened Follow-Up Rule",
        "Every high-value opened source should create follow-up search pressure",
        "Expansion Waves",
        "Currentness And Supersession",
        "Counterevidence Search",
        "Search Output Triage",
        "Record Integration",
        "Failure Modes",
    ],
    "agents/openai.yaml": [
        "Run maximum-saturation research into one Markdown record",
        "no weaker modes or routing",
        "batch/parallel diversified search",
        "source-open/fetch",
        "frontier queue convergence",
        "disambiguate entities and terminology",
        "evidence selection and inclusion",
        "corroboration and triangulation",
        "consensus and disagreement",
        "comparison and evaluation criteria",
        "question coverage audit",
        "audit source incentives",
        "quantitative claims",
        "currentness and version status",
        "inference boundaries",
        "assumption sensitivity",
        "material conflicts",
        "synthesis traceability",
        "refresh triggers",
    ],
    "scripts/validate_record.py": [
        "Validate a single Markdown research record",
        "REQUIRED_METADATA",
        "REQUIRED_SECTIONS",
        "REQUIRED_COVERAGE_GATES",
        "REQUIRED_PHRASES",
        "Diversified Search Batch Plan",
        "| Lane | Claim / Subquestion | Evidence Need | Source Families | Query / Path Patterns | Counter-Search | Final Status |",
        "| Batch | Source Families To Mix | Purpose | Record Integration |",
        "REQUIRED_ACCEPTANCE_TESTS",
        "REQUIRED_SATURATION_METRICS",
        "REQUIRED_BATCH_INTEGRATION_TARGETS",
        "REQUIRED_TOOL_CAPABILITY_ROWS",
        "ALLOWED_LEAD_ACTIONS",
        "ALLOWED_SOURCE_OPENED_FOLLOW_UP_ACTIONS",
        "ALLOWED_COVERAGE_DEBT_STATUS",
        "ALLOWED_SEARCH_MATRIX_FINAL_STATUS",
        "required acceptance test",
        "weak blocked/not-applicable evidence or remediation",
        "Question Coverage Audit row remains unanswered in final record",
        "Search Matrix lane remains planned/running instead of closed",
        "Tool Capability Audit missing required capability row",
        "Tool Capability Audit capability remains planned instead of resolved",
        "Lead Ledger has invalid or open action",
        "Lead Ledger outcome remains unresolved instead of closed or downgraded",
        "Source-Opened Follow-Up Audit must include at least one row",
        "Source-Opened Follow-Up Audit action remains planned/open/unresolved instead of closed, followed, blocked, or downgraded",
        "Claim Ledger must include at least one claim row",
        "Claim Ledger decision remains unresolved instead of use, downgrade, exclude, or insufficient",
        "Claim Traceability Matrix final decision remains unresolved instead of use, downgrade, exclude, or insufficient",
        "Coverage Debt row remains open instead of cleared, blocked, or downgraded",
        "Stop Rule Audit remains not satisfied in final record",
        "Saturation Metrics row remains not met in final record",
        "Domain Coverage Matrix row remains planned instead of resolved",
        "Language And Locale Audit row remains planned instead of resolved",
        "Expansion Frontier Audit frontier remains planned instead of closed",
        "Diversified Search Batch Test",
        "Diversified Search Batch Plan must include at least three batch rows",
        "Diversified Search Batch Plan row missing record integration mapping",
        "Diversified Search Batch Plan missing execution sub-batch details",
        "Diversified Search Batch Plan missing query count details",
        "Diversified Search Batch Plan missing numeric tool-limit detail",
        "Diversified Search Batch Plan missing SB execution group labels",
        "Diversified Search Batch Plan missing official/source-of-truth family",
        "Diversified Search Batch Plan missing counterevidence family",
        "Diversified Search Batch Plan missing currentness family",
        "Diversified Search Batch Plan missing provenance/source-lineage family",
        "Diversified Search Batch Plan missing frontier-expansion family",
        "Diversified Search Batch Plan missing blocked-source-recovery family",
        "Saturation Metrics missing required metric",
        "Expansion Frontier Test",
        "Frontier Queue Convergence Test",
        "Synthesis Traceability Test",
        "Decision Usefulness Test",
        "Evidence Maturity Dashboard Test",
        "Comparison And Evaluation Test",
        "Question Coverage Test",
        "Saturation Metrics Test",
        "Tool Capability Test",
        "Domain Coverage Test",
        "Planned domain rows do not pass final validation",
        "Language And Locale Test",
        "Planned language/locale rows do not pass final validation",
        "Entity And Terminology Test",
        "Selection And Inclusion Test",
        "Coverage Debt Test",
        "Source Lineage Map Test",
        "Corroboration And Triangulation Test",
        "Consensus And Disagreement Test",
        "Claim Traceability Test",
        "Inference Boundary Test",
        "Assumption And Sensitivity Test",
        "Conflict Resolution Test",
        "Claim Risk Triage Test",
        "Source Quality Audit Test",
        "Source Incentive And Bias Test",
        "Source Manipulation And Adversarial Provenance Test",
        "Quantitative And Measurement Test",
        "Currentness And Version Audit Test",
        "Reproducibility And Refresh Test",
        "Evidence Location Audit Test",
        "Quotation And Context Test",
        "Absence Evidence Test",
        "ALLOWED_SATURATION_METRIC_STATUS",
        "ALLOWED_QUOTATION_CONTEXT_STATUS",
        "ALLOWED_EXPANSION_FRONTIER_STATUS",
        "ALLOWED_SYNTHESIS_TRACE_STATUS",
        "ALLOWED_ASSUMPTION_SENSITIVITY_STATUS",
        "ALLOWED_ABSENCE_RESULT",
        "ALLOWED_QUESTION_COVERAGE_STATUS",
        "ALLOWED_INFERENCE_BOUNDARY_STATUS",
        "ALLOWED_CONFLICT_RESOLUTION",
        "Confidence Calibration Test",
        "Adversarial Review Test",
        "Stop Rule Audit Test",
        "Distortion Pattern Audit Test",
        "ALLOWED_TEST_RESULTS",
        "ALLOWED_TRIAGE_CLASSES",
        "ALLOWED_SEARCH_BIAS_STATUS",
        "ALLOWED_SELECTION_STATUS",
        "ALLOWED_LINEAGE_STATUS",
        "ALLOWED_TRACE_DECISIONS",
        "ALLOWED_SOURCE_QUALITY_STATUS",
        "ALLOWED_CORROBORATION_STATUS",
        "ALLOWED_CONSENSUS_DISAGREEMENT_STATUS",
        "ALLOWED_SOURCE_INCENTIVE_STATUS",
        "ALLOWED_MANIPULATION_PROVENANCE_STATUS",
        "ALLOWED_QUANTITATIVE_STATUS",
        "ALLOWED_CLAIM_TRIAGE_PRIORITY",
        "ALLOWED_CALIBRATED_CONFIDENCE",
        "ALLOWED_ADVERSARIAL_OUTCOME",
        "ALLOWED_STOP_RULE_STATUS",
        "ALLOWED_DISTORTION_STATUS",
        "ALLOWED_DOMAIN_COVERAGE_STATUS",
        "ALLOWED_LANGUAGE_LOCALE_STATUS",
        "ALLOWED_ENTITY_TERMINOLOGY_STATUS",
        "ALLOWED_RETRIEVAL_STATUS",
        "ALLOWED_CURRENTNESS_STATUS",
        "ALLOWED_REPRODUCIBILITY_STATUS",
        "ALLOWED_EVIDENCE_LOCATION_STATUS",
        "ALLOWED_DECISION_STATUS",
        "ALLOWED_EVIDENCE_MATURITY_STATUS",
        "ALLOWED_COMPARISON_EVALUATION_STATUS",
        "ALLOWED_TOOL_CAPABILITY_STATUS",
        "parse_markdown_rows",
        "Acceptance Tests",
        "FORBIDDEN_SIDECAR_PATTERNS",
        "FORBIDDEN_SIBLING_NAMES",
        "frontier-queue",
        "worker-waves",
        "validation-results",
        "tool-limit",
        "text_without_urls",
        'lstrip("\\ufeff")',
        "RECORD_FILENAME_PATTERN",
        "Research record validation passed.",
    ],
    "scripts/audit_record_consistency.py": [
        "Audit cross-section references inside one Markdown research record",
        "Research record consistency audit passed.",
        "EF",
        "Saturation Metrics",
        "Claim Traceability Matrix",
        "Synthesis Traceability Audit",
        "Question Coverage Audit",
        "Entity And Terminology Audit",
        "Inference Boundary Audit",
        "Conflict Resolution Matrix",
        "Source Lineage Map",
        "Access And Retrieval Audit",
        "Expansion Frontier Audit",
        "Corroboration And Triangulation Audit",
        "Consensus And Disagreement Audit",
        "Quotation And Context Audit",
        "Absence Evidence Audit",
        "Quantitative And Measurement Audit",
        "Source Incentive And Bias Audit",
        "Source Manipulation And Adversarial Provenance Audit",
        "Reproducibility And Refresh Audit",
        "Selection And Inclusion Audit",
        "unknown frontier reference",
        "unknown source reference",
        "unknown claim reference",
    ],
    "scripts/scaffold_record.py": [
        "Create one Markdown research record scaffold",
        "gigantum-humeris",
        "research",
        "FILLME",
        "Coverage Debt",
        "Expansion Frontier Audit",
        "Evidence Maturity Dashboard",
        "Decision Usefulness Matrix",
        "Comparison And Evaluation Audit",
        "Question Coverage Audit",
        "Resolve every unanswered question coverage row",
        "Tool Capability Audit",
        "batch / parallel diversified search",
        "source retrieval fallback",
        "Diversified Search Batch Plan",
        "frontier-expansion / blocked-source-recovery",
        "Domain Coverage Matrix",
        "Language And Locale Audit",
        "Entity And Terminology Audit",
        "Worker Wave Plan",
        "Search Result Triage",
        "Lead Ledger",
        "Close every material lead",
        "Search Bias And Retrieval Trap Audit",
        "Selection And Inclusion Audit",
        "Access And Retrieval Audit",
        "Source Lineage Map",
        "Source Quality Audit",
        "Corroboration And Triangulation Audit",
        "Consensus And Disagreement Audit",
        "Source Incentive And Bias Audit",
        "Source Manipulation And Adversarial Provenance Audit",
        "Quantitative And Measurement Audit",
        "Reproducibility And Refresh Audit",
        "Saturation Metrics",
        "Expansion Frontier Audit",
        "Frontier Queue Convergence Test",
        "frontier queue convergence",
        "Currentness And Version Audit",
        "Evidence Location Audit",
        "Quotation And Context Audit",
        "Absence Evidence Audit",
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
        "Acceptance Tests",
        "Diversified Search Batch Test",
        "12+ / 25+ / 50+",
    ],
    "scripts/plan_research.py": [
        "Generate a maximum-saturation research lane and worker-wave plan",
        "single research record",
        "Diversified Search Batch Plan",
        "query_matrix.py --topic",
        "--format batches",
        "Evidence Maturity Dashboard",
        "Decision Usefulness Matrix",
        "Comparison And Evaluation Audit",
        "Question Coverage Audit",
        "Tool Capability Audit",
        "batch / parallel diversified search",
        "source retrieval fallback",
        "frontier-expansion",
        "blocked-source-recovery",
        "Final Status",
        "SB1",
        "numeric tool-limit notes",
        "sub-batches of up to tool-limit",
        "Resolve every Search Matrix lane",
        "Resolve every planned capability row",
        "Resolve every planned domain row",
        "Resolve every planned language/locale row",
        "Resolve every planned expansion frontier row",
        "Resolve every open coverage debt row",
        "Resolve every not satisfied stop-rule row",
        "Search Matrix",
        "Domain Coverage Matrix",
        "Language And Locale Audit",
        "Entity And Terminology Audit",
        "Worker Wave Plan",
        "Search Result Triage",
        "Search Bias And Retrieval Trap Audit",
        "Access And Retrieval Audit",
        "Coverage Debt",
        "Expansion Frontier Audit",
        "Source Lineage Map",
        "Source Quality Audit",
        "Corroboration And Triangulation Audit",
        "Consensus And Disagreement Audit",
        "Quantitative And Measurement Audit",
        "Saturation Metrics",
        "Expansion Frontier Audit",
        "frontier queue convergence",
        "Currentness And Version Audit",
        "Evidence Location Audit",
        "Quotation And Context Audit",
        "Absence Evidence Audit",
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
        "claim verification audit",
        "source-lineage audit",
        "synthesis-overreach audit",
    ],
    "scripts/query_matrix.py": [
        "Generate high-yield query families",
        "BATCH_FAMILY_ORDER",
        "BATCH_PURPOSES",
        "BATCH_INTEGRATION_TARGETS",
        "STRATEGIC_BATCH_PHASES",
        "diversified_batches",
        "strategic_record_batches",
        "execution_sub_batches",
        "batch_purpose_with_sub_batches",
        "batch_record_integration",
        "batch-size",
        "batches",
        "official-primary",
        "implementation-code",
        "standards-specs",
        "legal-regulatory",
        "market-competitive",
        "public-sentiment",
        "security-advisory",
        "counterevidence",
        "source-lineage",
        "provenance-archive",
        "frontier-expansion",
        "blocked-source-recovery",
        "github-oss",
        "dataset-method",
    ],
}


COMPETITIVE_BASELINE: dict[str, dict[str, list[str]]] = {
    "ulw-research saturation": {
        "SKILL.md": [
            "Saturation-Orchestration Requirements",
            "worker-wave plan",
            "EXPAND lead loop",
            "Search-Tool Maximization",
            "web-search-harness-maximization.md",
        ],
        "references/subagent-orchestration.md": [
            "first wave together",
            "worker-wave discipline",
            "thin worker output",
            "include an `## EXPAND` tail",
            "EXPAND Follow-Up",
        ],
        "references/research-process.md": [
            "EXPAND is a loop, not a single pass",
            "Expansion Frontier Audit",
            "at least two expansion waves",
            "Worker-Wave Pressure And Coverage Debt",
            "coverage debt item",
        ],
    },
    "academic deep research": {
        "references/research-process.md": [
            "at least two search cycles per major theme",
            "For academic or scholarly research",
            "Read full text or relevant",
        ],
        "references/research-record-template.md": [
            "scholarly full text / methods",
        ],
    },
    "discovery research breadth": {
        "SKILL.md": [
            "state-of-the-art research should usually inspect 50 or more",
        ],
        "references/research-process.md": [
            "50+ for very broad diligence",
            "Source count never overrides",
        ],
        "references/acceptance-tests.md": [
            "Source Coverage Floor Test",
        ],
    },
    "claim verification": {
        "references/research-process.md": [
            "Atomic Claim Verification",
            "Verified-Claim Gate",
        ],
        "references/source-verification.md": [
            "Atomic Claims And Distortion Patterns",
            "misattribution",
            "circular citation",
            "inference upgraded to fact",
            "unverified magnitude",
            "evidence strength",
            "synthesis integrity",
        ],
    },
    "github and oss research": {
        "SKILL.md": [
            "for GitHub/OSS research",
            "commit/tag/release-pinned evidence",
        ],
        "references/research-process.md": [
            "For OSS ecosystem research",
            "repository search, code search, package registries",
            "prefer pinned commit/tag or",
        ],
    },
    "prior record reuse": {
        "SKILL.md": [
            "Use prior records only as leads",
        ],
        "references/research-process.md": [
            "Prior-Record Reuse",
            "Treat prior conclusions as leads",
        ],
        "references/research-record-template.md": [
            "Prior Record Check",
        ],
    },
    "single markdown governance": {
        "SKILL.md": [
            "produce exactly one Markdown research record",
            "Do not create multiple sibling records",
            "python research/scripts/scaffold_record.py",
            "python research/scripts/plan_research.py",
            "python research/scripts/query_matrix.py",
            "python research/scripts/validate_record.py <record-path>",
            "python research/scripts/audit_record_consistency.py <record-path>",
        ],
        "references/acceptance-tests.md": [
            "Single Markdown Record Test",
        ],
        "references/quality-rubric.md": [
            "of one Markdown research record",
        ],
        "scripts/validate_record.py": [
            "Validate a single Markdown research record",
            "missing section",
            "record filename must match <NNN-ascii-slug>.md",
            "sidecar artifact reference violates single-record contract",
            "sibling directory violates single-record contract",
            "sibling non-Markdown artifact violates single-record contract",
        ],
    },
    "third party skill safety": {
        "SKILL.md": [
            "when researching third-party skills",
        ],
        "references/source-verification.md": [
            "Third-Party Skill, Prompt, Plugin, And Script Safety",
            "Do not execute third-party code",
        ],
    },
    "competitive analysis evidence": {
        "references/competitive-baselines.md": [
            "ulw-research",
            "Expansion Frontier Audit",
            "academic-deep-research",
            "Deep_Deep_Research_Skill",
            "research-skill",
            "claim-verification",
            "Deep_Research_SKILL.md",
            "Research Planner",
            "Superset Scorecard",
            "Web Search Harness Playbook",
            "Question Coverage Audit",
            "Entity And Terminology Audit",
            "Search bias and retrieval traps",
        "Selection and inclusion",
            "Conflict resolution",
            "Source incentive and bias",
        "Source manipulation and adversarial provenance",
            "Quantitative measurement",
            "Reproducibility and refresh",
            "Decision usefulness",
        "Comparison and evaluation",
        "Consensus and disagreement",
            "Harness capability use",
            "Domain coverage",
            "Language and locale coverage",
            "Entity and terminology disambiguation",
            "Source retrieval",
            "Evidence location precision",
            "Saturation metrics",
            "Expansion frontier",
            "Absence evidence",
            "source lineage map",
            "source quality audit",
            "quantitative and measurement audit",
            "currentness and version audit",
            "evidence location audit",
            "claim risk triage",
            "distortion pattern audit",
            "claim traceability matrix",
            "inference boundary audit",
            "conflict resolution matrix",
            "confidence calibration",
            "adversarial review",
            "stop-rule audit",
            "This local skill must keep the extracted strengths",
        ],
    },
}


FORBIDDEN_IN_CORE = [
    "ULW-RESEARCH MODE ENABLED",
    "ultraresearch",
    "OpenCode-only tools",
    ".omo/ulw-research",
    "quick research mode",
    "deep research mode",
    "academic research mode",
    "lightweight research mode",
    "economy research mode",
    "lite research mode",
    "fast research mode",
    "basic research mode",
    "standard research mode",
    "quick mode",
    "deep mode",
    "academic mode",
    "mode selector",
    "mode selection",
    "routing table",
    "choose a research mode",
    "select a research mode",
    "select a research depth",
    "choose depth",
    "select depth",
]


def run_script(script_name: str, args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(ROOT / "scripts" / script_name), *args],
        check=False,
        capture_output=True,
        text=True,
    )


def add_process_failure(
    failures: list[str],
    label: str,
    result: subprocess.CompletedProcess[str],
) -> None:
    output = "\n".join(part for part in [result.stdout, result.stderr] if part).strip()
    failures.append(f"{label} failed with exit {result.returncode}: {output}")


def run_dynamic_smoke_tests(failures: list[str]) -> None:
    with tempfile.TemporaryDirectory(prefix="research-contract-") as tmp:
        tmp_root = Path(tmp)
        scaffold = run_script(
            "scaffold_record.py",
            [
                "--topic",
                "Verifier smoke",
                "--request",
                "test request",
                "--scope",
                "test scope",
                "--root",
                str(tmp_root),
            ],
        )
        if scaffold.returncode != 0:
            add_process_failure(failures, "scaffold_record smoke", scaffold)
            return

        record_path = Path(scaffold.stdout.strip().splitlines()[-1])
        if not record_path.exists():
            failures.append(f"scaffold_record smoke did not create record: {record_path}")
            return

        template_validation = run_script(
            "validate_record.py",
            [str(record_path), "--allow-placeholders"],
        )
        if template_validation.returncode != 0:
            add_process_failure(
                failures,
                "validate_record placeholder-allowed smoke",
                template_validation,
            )

        unfinished_validation = run_script("validate_record.py", [str(record_path)])
        unfinished_output = unfinished_validation.stdout + unfinished_validation.stderr
        if unfinished_validation.returncode == 0 or "FILLME" not in unfinished_output:
            failures.append(
                "validate_record smoke should reject unfinished scaffold with FILLME"
            )

        complete_text = record_path.read_text(encoding="utf-8").replace("FILLME", "pass")
        complete_text = complete_text.replace("tool-limit", "4")
        complete_text = complete_text.replace(
            " | planned | pass | pass | pass |",
            " | used | pass | pass | pass |",
        )
        complete_text = complete_text.replace(
            "| L1 | pass | pass | pass | pass | pass | planned |",
            "| L1 | pass | pass | pass | pass | pass | complete |",
        )
        complete_text = complete_text.replace(
            "| Q1 | pass | unanswered | C1 / D1 | pass | Answer / Open Questions |",
            "| Q1 | pass | answered | C1 / D1 | none | Answer |",
        )
        complete_text = complete_text.replace(
            "| EF1 | W1 / S1 / R1 / LD1 | pass | pass | source | pass | planned | pass |",
            "| EF1 | W1 / S1 / R1 / LD1 | pass | pass | source | pass | followed | pass |",
        )
        closed_lines: list[str] = []
        current_section = ""
        for line in complete_text.splitlines():
            if line.startswith("## "):
                current_section = line
            if current_section in {
                "## Domain Coverage Matrix",
                "## Language And Locale Audit",
            }:
                line = line.replace(" | planned | ", " | covered | ")
            if current_section == "## Coverage Debt":
                line = line.replace(" | open | ", " | cleared | ")
            if current_section == "## Stop Rule Audit":
                line = line.replace(" | not satisfied | ", " | satisfied | ")
            if current_section == "## Saturation Metrics":
                line = line.replace(" | not met | ", " | blocked | ")
            if current_section == "## Source-Opened Follow-Up Audit":
                line = line.replace(" | unresolved | ", " | blocked | ")
            if current_section == "## Claim Ledger":
                line = line.replace(" | unresolved |", " | insufficient |")
            if current_section == "## Claim Traceability Matrix":
                line = line.replace(
                    "| C1 | unresolved | O1 | S1 | G1 | pass | D1 | insufficient |",
                    "| C1 | insufficient | O1 | S1 | G1 | pass | D1 | insufficient |",
                )
            closed_lines.append(line)
        complete_text = "\n".join(closed_lines)
        complete_path = record_path.with_name("002-complete-record.md")
        complete_path.write_text(complete_text, encoding="utf-8")
        complete_validation = run_script("validate_record.py", [str(complete_path)])
        if complete_validation.returncode != 0:
            add_process_failure(
                failures,
                "validate_record complete-record smoke",
                complete_validation,
            )

        consistency_validation = run_script(
            "audit_record_consistency.py",
            [str(complete_path)],
        )
        if consistency_validation.returncode != 0:
            add_process_failure(
                failures,
                "audit_record_consistency complete-record smoke",
                consistency_validation,
            )

        invalid_consistency_path = record_path.with_name("003-invalid-consistency.md")
        invalid_consistency_text = complete_text.replace(
            "| C1 | insufficient | O1 | S1 | G1 | pass | D1 | insufficient |",
            "| C1 | insufficient | O1 | S999 | G1 | pass | D1 | insufficient |",
            1,
        )
        invalid_consistency_path.write_text(invalid_consistency_text, encoding="utf-8")
        invalid_consistency = run_script(
            "audit_record_consistency.py",
            [str(invalid_consistency_path)],
        )
        invalid_consistency_output = (
            invalid_consistency.stdout + invalid_consistency.stderr
        )
        if (
            invalid_consistency.returncode == 0
            or "unknown source reference" not in invalid_consistency_output
        ):
            failures.append(
                "audit_record_consistency smoke should reject unknown source references"
            )

        invalid_frontier_consistency_path = record_path.with_name(
            "003-invalid-frontier-consistency.md"
        )
        invalid_frontier_consistency_text = complete_text.replace(
            "| frontier queue convergence | latest EXPAND or gap cycle produces no new high-value leads, or all remaining material leads are closed, blocked, duplicate-lineage, out of scope, low quality, or confidence-downgraded | 0 | blocked | not run yet | insufficient until frontier convergence is documented |",
            "| frontier queue convergence | latest EXPAND or gap cycle produces no new high-value leads, or all remaining material leads are closed, blocked, duplicate-lineage, out of scope, low quality, or confidence-downgraded | 0 | blocked | EF999 | insufficient until frontier convergence is documented |",
            1,
        )
        invalid_frontier_consistency_path.write_text(
            invalid_frontier_consistency_text,
            encoding="utf-8",
        )
        invalid_frontier_consistency = run_script(
            "audit_record_consistency.py",
            [str(invalid_frontier_consistency_path)],
        )
        invalid_frontier_consistency_output = (
            invalid_frontier_consistency.stdout + invalid_frontier_consistency.stderr
        )
        if (
            invalid_frontier_consistency.returncode == 0
            or "unknown frontier reference" not in invalid_frontier_consistency_output
        ):
            failures.append(
                "audit_record_consistency smoke should reject unknown frontier references"
            )

        invalid_acceptance_path = record_path.with_name("003-invalid-acceptance.md")
        invalid_acceptance_text = complete_text.replace(
            "| Single Markdown Record Test | yes | pass | pass | pass |",
            "| Single Markdown Record Test | yes | maybe | pass | pass |",
            1,
        )
        invalid_acceptance_path.write_text(invalid_acceptance_text, encoding="utf-8")
        invalid_acceptance = run_script(
            "validate_record.py",
            [str(invalid_acceptance_path)],
        )
        invalid_acceptance_output = invalid_acceptance.stdout + invalid_acceptance.stderr
        if invalid_acceptance.returncode == 0 or "invalid result" not in invalid_acceptance_output:
            failures.append(
                "validate_record smoke should reject invalid acceptance test result"
            )

        invalid_decision_path = record_path.with_name("003-invalid-decision.md")
        invalid_decision_text = complete_text.replace(
            "| not applicable | not applicable | not applicable | C1 | pass | pass | not applicable |",
            "| not applicable | not applicable | not applicable | C1 | pass | pass | maybe |",
            1,
        )
        invalid_decision_path.write_text(invalid_decision_text, encoding="utf-8")
        invalid_decision = run_script(
            "validate_record.py",
            [str(invalid_decision_path)],
        )
        invalid_decision_output = invalid_decision.stdout + invalid_decision.stderr
        if invalid_decision.returncode == 0 or "invalid status" not in invalid_decision_output:
            failures.append(
                "validate_record smoke should reject invalid decision usefulness status"
            )

        invalid_comparison_path = record_path.with_name("003-invalid-comparison-evaluation.md")
        invalid_comparison_text = complete_text.replace(
            "| EV1 | not applicable | not applicable | not applicable | C1 / S1 / O1 / D1 | not applicable | AS1 / none | not applicable | no recommendation |",
            "| EV1 | not applicable | not applicable | not applicable | C1 / S1 / O1 / D1 | not applicable | AS1 / none | maybe | no recommendation |",
        )
        invalid_comparison_path.write_text(invalid_comparison_text, encoding="utf-8")
        invalid_comparison = subprocess.run(
            [
                sys.executable,
                str(ROOT / "scripts" / "validate_record.py"),
                str(invalid_comparison_path),
            ],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        invalid_comparison_output = invalid_comparison.stdout + invalid_comparison.stderr
        if invalid_comparison.returncode == 0 or "invalid status" not in invalid_comparison_output:
            failures.append(
                "validate_record smoke should reject invalid comparison and evaluation status"
            )

        invalid_question_path = record_path.with_name("003-invalid-question.md")
        invalid_question_text = complete_text.replace(
            "| Q1 | pass | answered | C1 / D1 | none | Answer |",
            "| Q1 | pass | maybe | C1 / D1 | none | Answer |",
            1,
        )
        invalid_question_path.write_text(invalid_question_text, encoding="utf-8")
        invalid_question = run_script(
            "validate_record.py",
            [str(invalid_question_path)],
        )
        invalid_question_output = invalid_question.stdout + invalid_question.stderr
        if invalid_question.returncode == 0 or "invalid answer status" not in invalid_question_output:
            failures.append(
                "validate_record smoke should reject invalid question coverage status"
            )

        invalid_tool_path = record_path.with_name("003-invalid-tool.md")
        invalid_tool_text = complete_text.replace(
            "| web search | used | pass | pass | pass |",
            "| web search | maybe | pass | pass | pass |",
            1,
        )
        invalid_tool_path.write_text(invalid_tool_text, encoding="utf-8")
        invalid_tool = run_script(
            "validate_record.py",
            [str(invalid_tool_path)],
        )
        invalid_tool_output = invalid_tool.stdout + invalid_tool.stderr
        if invalid_tool.returncode == 0 or "invalid status" not in invalid_tool_output:
            failures.append(
                "validate_record smoke should reject invalid tool capability status"
            )

        invalid_domain_path = record_path.with_name("003-invalid-domain.md")
        invalid_domain_text = complete_text.replace(
            "| official / primary | uncertain | governing records, official docs, filings, standards, releases | covered | pass |",
            "| official / primary | uncertain | governing records, official docs, filings, standards, releases | maybe | pass |",
            1,
        )
        invalid_domain_path.write_text(invalid_domain_text, encoding="utf-8")
        invalid_domain = run_script(
            "validate_record.py",
            [str(invalid_domain_path)],
        )
        invalid_domain_output = invalid_domain.stdout + invalid_domain.stderr
        if invalid_domain.returncode == 0 or "invalid status" not in invalid_domain_output:
            failures.append(
                "validate_record smoke should reject invalid domain coverage status"
            )

        invalid_locale_path = record_path.with_name("003-invalid-locale.md")
        invalid_locale_text = complete_text.replace(
            "| global / English / local language | uncertain | pass | local official, local media, registries, databases, forums, archives | covered | pass |",
            "| global / English / local language | uncertain | pass | local official, local media, registries, databases, forums, archives | maybe | pass |",
            1,
        )
        invalid_locale_path.write_text(invalid_locale_text, encoding="utf-8")
        invalid_locale = run_script(
            "validate_record.py",
            [str(invalid_locale_path)],
        )
        invalid_locale_output = invalid_locale.stdout + invalid_locale.stderr
        if invalid_locale.returncode == 0 or "invalid status" not in invalid_locale_output:
            failures.append(
                "validate_record smoke should reject invalid language and locale status"
            )

        invalid_entity_path = record_path.with_name("003-invalid-entity.md")
        invalid_entity_text = complete_text.replace(
            "| pass | pass | pass | pass | S1 / source family | blocked | insufficient |",
            "| pass | pass | pass | pass | S1 / source family | maybe | insufficient |",
            1,
        )
        invalid_entity_path.write_text(invalid_entity_text, encoding="utf-8")
        invalid_entity = run_script(
            "validate_record.py",
            [str(invalid_entity_path)],
        )
        invalid_entity_output = invalid_entity.stdout + invalid_entity.stderr
        if invalid_entity.returncode == 0 or "invalid status" not in invalid_entity_output:
            failures.append(
                "validate_record smoke should reject invalid entity and terminology status"
            )

        invalid_retrieval_path = record_path.with_name("003-invalid-retrieval.md")
        invalid_retrieval_text = complete_text.replace(
            "| AR1 | S1 | direct URL | archive, PDF, API, browser, mirror, package, cached copy, cited excerpt | blocked | lead only | insufficient |",
            "| AR1 | S1 | direct URL | archive, PDF, API, browser, mirror, package, cached copy, cited excerpt | maybe | lead only | insufficient |",
            1,
        )
        invalid_retrieval_path.write_text(invalid_retrieval_text, encoding="utf-8")
        invalid_retrieval = run_script(
            "validate_record.py",
            [str(invalid_retrieval_path)],
        )
        invalid_retrieval_output = invalid_retrieval.stdout + invalid_retrieval.stderr
        if invalid_retrieval.returncode == 0 or "invalid retrieval status" not in invalid_retrieval_output:
            failures.append(
                "validate_record smoke should reject invalid access and retrieval status"
            )

        invalid_triage_path = record_path.with_name("003-invalid-triage.md")
        invalid_triage_text = complete_text.replace(
            "| R1 | L1 | pass | open-now | pass | pass |",
            "| R1 | L1 | pass | maybe | pass | pass |",
            1,
        )
        invalid_triage_path.write_text(invalid_triage_text, encoding="utf-8")
        invalid_triage = run_script(
            "validate_record.py",
            [str(invalid_triage_path)],
        )
        invalid_triage_output = invalid_triage.stdout + invalid_triage.stderr
        if invalid_triage.returncode == 0 or "invalid classification" not in invalid_triage_output:
            failures.append(
                "validate_record smoke should reject invalid search result triage classification"
            )

        invalid_selection_path = record_path.with_name("003-invalid-selection.md")
        invalid_selection_text = complete_text.replace(
            "| pass | pass | pass | S1 | R1 / LD1 | pass | pass | incomplete | insufficient |",
            "| pass | pass | pass | S1 | R1 / LD1 | pass | pass | maybe | insufficient |",
            1,
        )
        invalid_selection_path.write_text(invalid_selection_text, encoding="utf-8")
        invalid_selection = run_script(
            "validate_record.py",
            [str(invalid_selection_path)],
        )
        invalid_selection_output = invalid_selection.stdout + invalid_selection.stderr
        if invalid_selection.returncode == 0 or "invalid status" not in invalid_selection_output:
            failures.append(
                "validate_record smoke should reject invalid selection and inclusion status"
            )

        invalid_lineage_path = record_path.with_name("003-invalid-lineage.md")
        invalid_lineage_text = complete_text.replace(
            "| G1 | pass | S1 | unclear | C1 | pass |",
            "| G1 | pass | S1 | maybe | C1 | pass |",
            1,
        )
        invalid_lineage_path.write_text(invalid_lineage_text, encoding="utf-8")
        invalid_lineage = run_script(
            "validate_record.py",
            [str(invalid_lineage_path)],
        )
        invalid_lineage_output = invalid_lineage.stdout + invalid_lineage.stderr
        if invalid_lineage.returncode == 0 or "invalid independence status" not in invalid_lineage_output:
            failures.append(
                "validate_record smoke should reject invalid source lineage independence status"
            )

        invalid_quality_path = record_path.with_name("003-invalid-quality.md")
        invalid_quality_text = complete_text.replace(
            "| S1 | unknown | indirect | unknown | opaque | unclear | weak | downgrades C1 |",
            "| S1 | unknown | indirect | unknown | opaque | unclear | maybe | downgrades C1 |",
            1,
        )
        invalid_quality_path.write_text(invalid_quality_text, encoding="utf-8")
        invalid_quality = run_script(
            "validate_record.py",
            [str(invalid_quality_path)],
        )
        invalid_quality_output = invalid_quality.stdout + invalid_quality.stderr
        if invalid_quality.returncode == 0 or "invalid overall status" not in invalid_quality_output:
            failures.append(
                "validate_record smoke should reject invalid source quality overall status"
            )

        invalid_corroboration_path = record_path.with_name("003-invalid-corroboration.md")
        invalid_corroboration_text = complete_text.replace(
            "| C1 | none | none | not searched | not applicable | unclear | blocked | insufficient |",
            "| C1 | none | none | not searched | not applicable | unclear | maybe | insufficient |",
            1,
        )
        invalid_corroboration_path.write_text(
            invalid_corroboration_text,
            encoding="utf-8",
        )
        invalid_corroboration = run_script(
            "validate_record.py",
            [str(invalid_corroboration_path)],
        )
        invalid_corroboration_output = (
            invalid_corroboration.stdout + invalid_corroboration.stderr
        )
        if invalid_corroboration.returncode == 0 or "invalid status" not in invalid_corroboration_output:
            failures.append(
                "validate_record smoke should reject invalid corroboration and triangulation status"
            )

        invalid_incentive_path = record_path.with_name("003-invalid-incentive.md")
        invalid_incentive_text = complete_text.replace(
            "| S1 / G1 | unknown | unknown | unclear | independent corroboration required | unknown | downgrades C1 |",
            "| S1 / G1 | unknown | unknown | unclear | independent corroboration required | maybe | downgrades C1 |",
            1,
        )
        invalid_incentive_path.write_text(invalid_incentive_text, encoding="utf-8")
        invalid_incentive = run_script(
            "validate_record.py",
            [str(invalid_incentive_path)],
        )
        invalid_incentive_output = invalid_incentive.stdout + invalid_incentive.stderr
        if invalid_incentive.returncode == 0 or "invalid status" not in invalid_incentive_output:
            failures.append(
                "validate_record smoke should reject invalid source incentive and bias status"
            )

        invalid_quantitative_path = record_path.with_name("003-invalid-quantitative.md")
        invalid_quantitative_text = complete_text.replace(
            "| C1 / not applicable | not applicable | not applicable | not applicable | not applicable | not applicable | not applicable | not applicable | none |",
            "| C1 / not applicable | not applicable | not applicable | not applicable | not applicable | not applicable | not applicable | maybe | none |",
            1,
        )
        invalid_quantitative_path.write_text(invalid_quantitative_text, encoding="utf-8")
        invalid_quantitative = run_script(
            "validate_record.py",
            [str(invalid_quantitative_path)],
        )
        invalid_quantitative_output = invalid_quantitative.stdout + invalid_quantitative.stderr
        if invalid_quantitative.returncode == 0 or "invalid status" not in invalid_quantitative_output:
            failures.append(
                "validate_record smoke should reject invalid quantitative and measurement status"
            )

        invalid_currentness_path = record_path.with_name("003-invalid-currentness.md")
        invalid_currentness_text = complete_text.replace(
            "| C1 / S1 | current | unknown | blocked | unknown | insufficient |",
            "| C1 / S1 | current | unknown | blocked | maybe | insufficient |",
            1,
        )
        invalid_currentness_path.write_text(invalid_currentness_text, encoding="utf-8")
        invalid_currentness = run_script(
            "validate_record.py",
            [str(invalid_currentness_path)],
        )
        invalid_currentness_output = invalid_currentness.stdout + invalid_currentness.stderr
        if invalid_currentness.returncode == 0 or "invalid status" not in invalid_currentness_output:
            failures.append(
                "validate_record smoke should reject invalid currentness/version status"
            )

        invalid_repro_path = record_path.with_name("003-invalid-reproducibility.md")
        invalid_repro_text = "\n".join(
            line.replace(" | blocked | insufficient |", " | maybe | insufficient |")
            if line.startswith("| whole record / C1 / S1 |")
            else line
            for line in complete_text.splitlines()
        )
        invalid_repro_path.write_text(invalid_repro_text, encoding="utf-8")
        invalid_repro = run_script(
            "validate_record.py",
            [str(invalid_repro_path)],
        )
        invalid_repro_output = invalid_repro.stdout + invalid_repro.stderr
        if invalid_repro.returncode == 0 or "invalid status" not in invalid_repro_output:
            failures.append(
                "validate_record smoke should reject invalid reproducibility and refresh status"
            )

        invalid_saturation_path = record_path.with_name("003-invalid-saturation.md")
        invalid_saturation_text = complete_text.replace(
            "| distinct search queries | at least 10 per important web lane when web search exists | 0 | blocked | not run yet | insufficient until executed |",
            "| distinct search queries | at least 10 per important web lane when web search exists | 0 | maybe | not run yet | insufficient until executed |",
            1,
        )
        invalid_saturation_path.write_text(invalid_saturation_text, encoding="utf-8")
        invalid_saturation = run_script(
            "validate_record.py",
            [str(invalid_saturation_path)],
        )
        invalid_saturation_output = invalid_saturation.stdout + invalid_saturation.stderr
        if invalid_saturation.returncode == 0 or "invalid status" not in invalid_saturation_output:
            failures.append(
                "validate_record smoke should reject invalid saturation metric status"
            )

        missing_saturation_metric_path = record_path.with_name("003-missing-saturation-metric.md")
        missing_saturation_metric_text = complete_text.replace(
            "| frontier queue convergence | latest EXPAND or gap cycle produces no new high-value leads, or all remaining material leads are closed, blocked, duplicate-lineage, out of scope, low quality, or confidence-downgraded | 0 | blocked | not run yet | insufficient until frontier convergence is documented |\n",
            "",
            1,
        )
        missing_saturation_metric_path.write_text(
            missing_saturation_metric_text,
            encoding="utf-8",
        )
        missing_saturation_metric = run_script(
            "validate_record.py",
            [str(missing_saturation_metric_path)],
        )
        missing_saturation_metric_output = (
            missing_saturation_metric.stdout + missing_saturation_metric.stderr
        )
        if (
            missing_saturation_metric.returncode == 0
            or "missing required metric" not in missing_saturation_metric_output
        ):
            failures.append(
                "validate_record smoke should reject missing required saturation metrics"
            )

        invalid_frontier_path = record_path.with_name("003-invalid-expansion-frontier.md")
        invalid_frontier_text = complete_text.replace(
            "| EF1 | W1 / S1 / R1 / LD1 | pass | pass | source | pass | followed | pass |",
            "| EF1 | W1 / S1 / R1 / LD1 | pass | pass | source | pass | maybe | pass |",
            1,
        )
        invalid_frontier_path.write_text(invalid_frontier_text, encoding="utf-8")
        invalid_frontier = run_script(
            "validate_record.py",
            [str(invalid_frontier_path)],
        )
        invalid_frontier_output = invalid_frontier.stdout + invalid_frontier.stderr
        if invalid_frontier.returncode == 0 or "invalid status" not in invalid_frontier_output:
            failures.append(
                "validate_record smoke should reject invalid expansion frontier status"
            )

        invalid_location_path = record_path.with_name("003-invalid-location.md")
        invalid_location_text = complete_text.replace(
            "| C1 / O1 | S1 | page / section / table / line / timestamp / field / tag / issue / docket | no | pass | insufficient |",
            "| C1 / O1 | S1 | page / section / table / line / timestamp / field / tag / issue / docket | maybe | pass | insufficient |",
            1,
        )
        invalid_location_path.write_text(invalid_location_text, encoding="utf-8")
        invalid_location = run_script(
            "validate_record.py",
            [str(invalid_location_path)],
        )
        invalid_location_output = invalid_location.stdout + invalid_location.stderr
        if invalid_location.returncode == 0 or "invalid locator status" not in invalid_location_output:
            failures.append(
                "validate_record smoke should reject invalid evidence location status"
            )

        invalid_quotation_path = record_path.with_name("003-invalid-quotation-context.md")
        invalid_quotation_text = complete_text.replace(
            "| C1 / O1 | S1 | unknown | pass | pass | unresolved | context missing | unresolved | insufficient |",
            "| C1 / O1 | S1 | unknown | pass | pass | unresolved | context missing | maybe | insufficient |",
            1,
        )
        invalid_quotation_path.write_text(invalid_quotation_text, encoding="utf-8")
        invalid_quotation = run_script(
            "validate_record.py",
            [str(invalid_quotation_path)],
        )
        invalid_quotation_output = invalid_quotation.stdout + invalid_quotation.stderr
        if invalid_quotation.returncode == 0 or "invalid status" not in invalid_quotation_output:
            failures.append(
                "validate_record smoke should reject invalid quotation and context status"
            )

        invalid_absence_path = record_path.with_name("003-invalid-absence.md")
        invalid_absence_text = complete_text.replace(
            "| C1 | pass | official / primary / dataset / scholarly / archive / local-language / repository / counter-search | blocked | no absence inference until searched | insufficient |",
            "| C1 | pass | official / primary / dataset / scholarly / archive / local-language / repository / counter-search | maybe | no absence inference until searched | insufficient |",
            1,
        )
        invalid_absence_path.write_text(invalid_absence_text, encoding="utf-8")
        invalid_absence = run_script(
            "validate_record.py",
            [str(invalid_absence_path)],
        )
        invalid_absence_output = invalid_absence.stdout + invalid_absence.stderr
        if invalid_absence.returncode == 0 or "invalid absence result" not in invalid_absence_output:
            failures.append(
                "validate_record smoke should reject invalid absence evidence result"
            )

        invalid_risk_path = record_path.with_name("003-invalid-risk.md")
        invalid_risk_text = complete_text.replace(
            "| C1 | high | high | high | primary source, counter-search, currentness, lineage, method/data, adversarial review | downgrade or mark insufficient if required checks fail |",
            "| C1 | high | high | maybe | primary source, counter-search, currentness, lineage, method/data, adversarial review | downgrade or mark insufficient if required checks fail |",
            1,
        )
        invalid_risk_path.write_text(invalid_risk_text, encoding="utf-8")
        invalid_risk = run_script(
            "validate_record.py",
            [str(invalid_risk_path)],
        )
        invalid_risk_output = invalid_risk.stdout + invalid_risk.stderr
        if invalid_risk.returncode == 0 or "invalid verification priority" not in invalid_risk_output:
            failures.append(
                "validate_record smoke should reject invalid claim risk triage priority"
            )

        invalid_trace_path = record_path.with_name("003-invalid-trace.md")
        invalid_trace_text = complete_text.replace(
            "| C1 | insufficient | O1 | S1 | G1 | pass | D1 | insufficient |",
            "| C1 | maybe | O1 | S1 | G1 | pass | D1 | insufficient |",
            1,
        )
        invalid_trace_path.write_text(invalid_trace_text, encoding="utf-8")
        invalid_trace = run_script(
            "validate_record.py",
            [str(invalid_trace_path)],
        )
        invalid_trace_output = invalid_trace.stdout + invalid_trace.stderr
        if invalid_trace.returncode == 0 or "invalid final decision" not in invalid_trace_output:
            failures.append(
                "validate_record smoke should reject invalid claim traceability final decision"
            )

        invalid_inference_path = record_path.with_name("003-invalid-inference.md")
        invalid_inference_text = complete_text.replace(
            "| C1 | O1 / S1 | bounded inference | pass | pass | blocked | insufficient |",
            "| C1 | O1 / S1 | bounded inference | pass | pass | maybe | insufficient |",
            1,
        )
        invalid_inference_path.write_text(invalid_inference_text, encoding="utf-8")
        invalid_inference = run_script(
            "validate_record.py",
            [str(invalid_inference_path)],
        )
        invalid_inference_output = invalid_inference.stdout + invalid_inference.stderr
        if invalid_inference.returncode == 0 or "invalid status" not in invalid_inference_output:
            failures.append(
                "validate_record smoke should reject invalid inference boundary status"
            )

        invalid_assumption_path = record_path.with_name("003-invalid-assumption-sensitivity.md")
        invalid_assumption_text = complete_text.replace(
            "| AS1 | C1 / decision | pass | pass | S1 / O1 / D1 | high | untested | insufficient |",
            "| AS1 | C1 / decision | pass | pass | S1 / O1 / D1 | high | maybe | insufficient |",
            1,
        )
        invalid_assumption_path.write_text(
            invalid_assumption_text,
            encoding="utf-8",
        )
        invalid_assumption = run_script(
            "validate_record.py",
            [str(invalid_assumption_path)],
        )
        invalid_assumption_output = invalid_assumption.stdout + invalid_assumption.stderr
        if invalid_assumption.returncode == 0 or "invalid status" not in invalid_assumption_output:
            failures.append(
                "validate_record smoke should reject invalid assumption and sensitivity status"
            )

        invalid_conflict_path = record_path.with_name("003-invalid-conflict.md")
        invalid_conflict_text = complete_text.replace(
            "| CF1 | C1 / O1 | none | no material conflict checked yet | pass | unresolved | insufficient |",
            "| CF1 | C1 / O1 | none | no material conflict checked yet | pass | maybe | insufficient |",
            1,
        )
        invalid_conflict_path.write_text(invalid_conflict_text, encoding="utf-8")
        invalid_conflict = run_script(
            "validate_record.py",
            [str(invalid_conflict_path)],
        )
        invalid_conflict_output = invalid_conflict.stdout + invalid_conflict.stderr
        if invalid_conflict.returncode == 0 or "invalid resolution" not in invalid_conflict_output:
            failures.append(
                "validate_record smoke should reject invalid conflict resolution"
            )

        invalid_confidence_path = record_path.with_name("003-invalid-confidence.md")
        invalid_confidence_text = complete_text.replace(
            "| C1 | weak | unresolved | indirect | unknown | unclear | opaque | D1 | insufficient | pass |",
            "| C1 | weak | unresolved | indirect | unknown | unclear | opaque | D1 | maybe | pass |",
            1,
        )
        invalid_confidence_path.write_text(invalid_confidence_text, encoding="utf-8")
        invalid_confidence = run_script(
            "validate_record.py",
            [str(invalid_confidence_path)],
        )
        invalid_confidence_output = invalid_confidence.stdout + invalid_confidence.stderr
        if (
            invalid_confidence.returncode == 0
            or "invalid calibrated confidence" not in invalid_confidence_output
        ):
            failures.append(
                "validate_record smoke should reject invalid calibrated confidence"
            )

        invalid_synthesis_trace_path = record_path.with_name("003-invalid-synthesis-trace.md")
        invalid_synthesis_trace_text = complete_text.replace(
            "| ST1 | Answer / Key Findings | C1 | S1 / O1 | insufficient | D1 | blocked | keep final synthesis caveated until traceability passes |",
            "| ST1 | Answer / Key Findings | C1 | S1 / O1 | insufficient | D1 | maybe | keep final synthesis caveated until traceability passes |",
            1,
        )
        invalid_synthesis_trace_path.write_text(
            invalid_synthesis_trace_text,
            encoding="utf-8",
        )
        invalid_synthesis_trace = run_script(
            "validate_record.py",
            [str(invalid_synthesis_trace_path)],
        )
        invalid_synthesis_trace_output = (
            invalid_synthesis_trace.stdout + invalid_synthesis_trace.stderr
        )
        if (
            invalid_synthesis_trace.returncode == 0
            or "invalid status" not in invalid_synthesis_trace_output
        ):
            failures.append(
                "validate_record smoke should reject invalid synthesis traceability status"
            )

        invalid_adversarial_path = record_path.with_name("003-invalid-adversarial.md")
        invalid_adversarial_text = complete_text.replace(
            "| A1 | C1 | pass | pass | unresolved | unresolved | lowers C1 to insufficient |",
            "| A1 | C1 | pass | pass | unresolved | maybe | lowers C1 to insufficient |",
            1,
        )
        invalid_adversarial_path.write_text(invalid_adversarial_text, encoding="utf-8")
        invalid_adversarial = run_script(
            "validate_record.py",
            [str(invalid_adversarial_path)],
        )
        invalid_adversarial_output = invalid_adversarial.stdout + invalid_adversarial.stderr
        if (
            invalid_adversarial.returncode == 0
            or "invalid outcome" not in invalid_adversarial_output
        ):
            failures.append(
                "validate_record smoke should reject invalid adversarial review outcome"
            )

        invalid_stop_path = record_path.with_name("003-invalid-stop.md")
        invalid_stop_text = complete_text.replace(
            "| SR1 | C1 | lanes, source families, EXPAND, counter-search, currentness, lineage, quality, traceability, calibration, adversarial review | satisfied | D1 | insufficient |",
            "| SR1 | C1 | lanes, source families, EXPAND, counter-search, currentness, lineage, quality, traceability, calibration, adversarial review | maybe | D1 | insufficient |",
            1,
        )
        invalid_stop_path.write_text(invalid_stop_text, encoding="utf-8")
        invalid_stop = run_script(
            "validate_record.py",
            [str(invalid_stop_path)],
        )
        invalid_stop_output = invalid_stop.stdout + invalid_stop.stderr
        if invalid_stop.returncode == 0 or "invalid status" not in invalid_stop_output:
            failures.append(
                "validate_record smoke should reject invalid stop-rule audit status"
            )

        invalid_distortion_path = record_path.with_name("003-invalid-distortion.md")
        invalid_distortion_text = complete_text.replace(
            "| C1 / S1 | stale, misattribution, conflation, circular citation, inference upgraded to fact, magnitude drift, quote distortion, translation drift, cherry-pick, survivorship bias | pass | unresolved | insufficient |",
            "| C1 / S1 | stale, misattribution, conflation, circular citation, inference upgraded to fact, magnitude drift, quote distortion, translation drift, cherry-pick, survivorship bias | pass | maybe | insufficient |",
            1,
        )
        invalid_distortion_path.write_text(invalid_distortion_text, encoding="utf-8")
        invalid_distortion = run_script(
            "validate_record.py",
            [str(invalid_distortion_path)],
        )
        invalid_distortion_output = invalid_distortion.stdout + invalid_distortion.stderr
        if invalid_distortion.returncode == 0 or "invalid status" not in invalid_distortion_output:
            failures.append(
                "validate_record smoke should reject invalid distortion pattern status"
            )

        sidecar_path = record_path.with_name("004-sidecar-record.md")
        sidecar_path.write_text(
            complete_text + "\nLocal sidecar: sources/raw.md\n",
            encoding="utf-8",
        )
        sidecar_validation = run_script("validate_record.py", [str(sidecar_path)])
        sidecar_output = sidecar_validation.stdout + sidecar_validation.stderr
        if sidecar_validation.returncode == 0 or "sidecar artifact" not in sidecar_output:
            failures.append("validate_record smoke should reject local sidecar references")

        url_path = record_path.with_name("005-url-record.md")
        url_path.write_text(
            complete_text + "\nReference URL: https://example.com/sources/page\n",
            encoding="utf-8",
        )
        url_validation = run_script("validate_record.py", [str(url_path)])
        if url_validation.returncode != 0:
            add_process_failure(
                failures,
                "validate_record URL false-positive smoke",
                url_validation,
            )

        sibling_dir = record_path.parent / "sources"
        sibling_dir.mkdir(exist_ok=True)
        sibling_validation = run_script("validate_record.py", [str(url_path)])
        sibling_output = sibling_validation.stdout + sibling_validation.stderr
        if sibling_validation.returncode == 0 or "sibling directory" not in sibling_output:
            failures.append("validate_record smoke should reject sibling sidecar directories")

        sibling_dir.rmdir()
        sibling_file = record_path.parent / "artifact.json"
        sibling_file.write_text("{}", encoding="utf-8")
        sibling_file_validation = run_script("validate_record.py", [str(url_path)])
        sibling_file_output = sibling_file_validation.stdout + sibling_file_validation.stderr
        if (
            sibling_file_validation.returncode == 0
            or "sibling non-Markdown artifact" not in sibling_file_output
        ):
            failures.append("validate_record smoke should reject sibling non-Markdown artifacts")

        query_matrix = run_script(
            "query_matrix.py",
            [
                "--topic",
                "agent research skills",
                "--entities",
                "Codex",
                "--jurisdictions",
                "global",
                "--languages",
                "Korean",
            ],
        )
        if query_matrix.returncode != 0:
            add_process_failure(failures, "query_matrix smoke", query_matrix)
        else:
            query_output = query_matrix.stdout
            for expected in [
                "official-primary",
                "counterevidence",
                "provenance-archive",
                "github-oss",
                "dataset-method",
                "implementation-code",
                "legal-regulatory",
                "source-lineage",
                "frontier-expansion",
                "blocked-source-recovery",
            ]:
                if expected not in query_output:
                    failures.append(f"query_matrix smoke missing family {expected!r}")

        query_batches = run_script(
            "query_matrix.py",
            [
                "--topic",
                "agent research skills",
                "--entities",
                "Codex",
                "--jurisdictions",
                "global",
                "--languages",
                "Korean",
                "--format",
                "batches",
                "--batch-size",
                "4",
            ],
        )
        if query_batches.returncode != 0:
            add_process_failure(failures, "query_matrix batch smoke", query_batches)
        else:
            batch_output = query_batches.stdout
            for expected in [
                "| Batch | Source Families To Mix | Purpose | Record Integration |",
                "frontier-expansion",
                "blocked-source-recovery",
                "alternate retrieval for blocked sources",
                "sub-batches of up to",
                "Expansion Frontier Audit",
                "Coverage Debt",
            ]:
                if expected not in batch_output:
                    failures.append(f"query_matrix batch smoke missing {expected!r}")

        plan_research = run_script(
            "plan_research.py",
            [
                "--topic",
                "agent research skills",
                "--request",
                "compare research skills",
                "--scope",
                "maximum-saturation comparison",
                "--domains",
                "technical,academic",
                "--entities",
                "Codex",
                "--jurisdictions",
                "global",
                "--languages",
                "Korean",
            ],
        )
        if plan_research.returncode != 0:
            add_process_failure(failures, "plan_research smoke", plan_research)
        else:
            plan_output = plan_research.stdout
            for expected in [
                "## Evidence Maturity Dashboard",
                "## Decision Usefulness Matrix",
                "## Comparison And Evaluation Audit",
                "## Question Coverage Audit",
                "## Tool Capability Audit",
                "## Search Matrix",
                "## Diversified Search Batch Plan",
                "--format batches",
                "frontier-expansion",
                "blocked-source-recovery",
                "## Domain Coverage Matrix",
                "## Language And Locale Audit",
                "## Entity And Terminology Audit",
                "## Worker Wave Plan",
                "## Search Result Triage",
                "## Search Bias And Retrieval Trap Audit",
                "## Selection And Inclusion Audit",
                "## Access And Retrieval Audit",
                "## Expansion Frontier Audit",
                "frontier queue convergence",
                "## Coverage Debt",
                "## Source Lineage Map",
                "## Source Quality Audit",
                "## Corroboration And Triangulation Audit",
                "## Consensus And Disagreement Audit",
                "## Source Incentive And Bias Audit",
                "## Source Manipulation And Adversarial Provenance Audit",
                "## Quantitative And Measurement Audit",
                "## Saturation Metrics",
                "## Currentness And Version Audit",
                "## Reproducibility And Refresh Audit",
                "## Evidence Location Audit",
                "## Quotation And Context Audit",
                "## Absence Evidence Audit",
                "## Claim Risk Triage",
                "## Claim Traceability Matrix",
                "## Inference Boundary Audit",
                "## Assumption And Sensitivity Audit",
                "## Conflict Resolution Matrix",
                "## Confidence Calibration",
                "## Synthesis Traceability Audit",
                "## Adversarial Review",
                "## Stop Rule Audit",
                "## Distortion Pattern Audit",
                "claim verification audit",
                "synthesis-overreach audit",
            ]:
                if expected not in plan_output:
                    failures.append(f"plan_research smoke missing {expected!r}")


def main() -> int:
    failures: list[str] = []

    def contains(text: str, needle: str) -> bool:
        normalized_text = " ".join(text.split())
        normalized_needle = " ".join(needle.split())
        return normalized_needle in normalized_text

    for relative_path, needles in CHECKS.items():
        path = ROOT / relative_path
        if not path.exists():
            failures.append(f"missing file: {relative_path}")
            continue
        text = path.read_text(encoding="utf-8")
        for needle in needles:
            if not contains(text, needle):
                failures.append(f"{relative_path}: missing {needle!r}")

    for relative_path in [
        "SKILL.md",
        "references/research-process.md",
        "references/research-record-template.md",
        "references/subagent-orchestration.md",
    ]:
        text = (ROOT / relative_path).read_text(encoding="utf-8")
        for forbidden in FORBIDDEN_IN_CORE:
            if contains(text, forbidden):
                failures.append(f"{relative_path}: forbidden mode/routing residue {forbidden!r}")

    for baseline_name, file_checks in COMPETITIVE_BASELINE.items():
        for relative_path, needles in file_checks.items():
            path = ROOT / relative_path
            if not path.exists():
                failures.append(f"{baseline_name}: missing file {relative_path}")
                continue
            text = path.read_text(encoding="utf-8")
            for needle in needles:
                if not contains(text, needle):
                    failures.append(
                        f"{baseline_name}: {relative_path} missing {needle!r}"
                    )

    run_dynamic_smoke_tests(failures)

    if failures:
        print("Research skill contract verification failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Research skill contract verification passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
