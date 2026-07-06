#!/usr/bin/env python3
"""Verify the research skill's current hard contract.

This maintenance check intentionally guards the small set of invariants that
make the skill a maximum-saturation research skill. It should not reintroduce
the old template-heavy structure by checking for long section inventories.
"""

from __future__ import annotations

from pathlib import Path
import re
import sys

from script_io import force_utf8_stdio


force_utf8_stdio()


ROOT = Path(__file__).resolve().parents[1]


REQUIRED_SKILL_SECTIONS = [
    "# Research",
    "## Product Contract",
    "## Outcome First",
    "## Research Execution",
    "## Evidence Rules",
    "## Record Shape",
    "## Stop Rule",
    "## Verification Loop",
    "## References",
]


REQUIRED_SKILL_CONTRACT = [
    "This skill has one behavior: maximum-saturation research",
    "Do not offer, infer, or follow quick/deep/lightweight modes",
    "Do not ask the user to choose depth",
    "Produce exactly one Markdown research record",
    "Search across every authorized source family",
    "Inspect source bodies or connector records",
    "Treat search snippets, AI summaries, citations found in other summaries, and subagent conclusions as leads only",
    "Expand useful leads",
    "Counter-search",
    "Verify every important claim",
    "The final synthesis must make it clear which claims are well-supported, contested, uncertain, outdated, or unsupported",
    "Do not let formatting, tables, or boilerplate displace source inspection, lead expansion, or claim verification",
    "Stop only when all of these are true",
    "Tool, time, access, or context limits do not authorize a weaker research mode",
    "Load extra references only when they materially help",
    "The instructions in this `SKILL.md` govern if a reference or helper script is stale, narrower, or more format-heavy",
]


REQUIRED_REFERENCES = [
    "references/research-process.md",
    "references/evidence-needs-core.md",
    "references/query-and-source-patterns.md",
    "references/source-verification.md",
    "references/subagent-orchestration.md",
    "references/web-search-harness-maximization.md",
    "references/research-record-template.md",
]


REQUIRED_HELPER_SCRIPTS = [
    "scripts/plan_research.py",
    "scripts/query_matrix.py",
    "scripts/scaffold_record.py",
    "scripts/validate_record.py",
    "scripts/audit_record_consistency.py",
    "scripts/validate_research_record.py",
    "scripts/markdown_record.py",
    "scripts/research_taxonomy.py",
    "scripts/script_io.py",
]


REQUIRED_AGENT_CONTRACT = [
    "maximum-saturation evidence research",
    "Do not use quick/deep/lightweight modes",
    "inspect sources, expand leads, counter-search, verify claims",
    "one Markdown record",
]


MODE_HEADING_RE = re.compile(
    r"^#{1,6}\s+(quick|deep|lightweight|academic|standard)\b",
    re.IGNORECASE | re.MULTILINE,
)
FORBIDDEN_CONTRACT_PATTERNS = [
    (
        re.compile(r"^#{1,6}\s+.*\b(quick|lightweight)\b", re.IGNORECASE | re.MULTILINE),
        "mode-like heading",
    ),
    (
        re.compile(r"\b(quick|lightweight)\s+research\s+mode\b", re.IGNORECASE),
        "mode-like research path",
    ),
    (
        re.compile(r"\bcreate\s+.*\b(brief|sources|notes)\.md\b", re.IGNORECASE),
        "sidecar Markdown deliverable",
    ),
    (
        re.compile(r"\bmultiple\s+Markdown\s+research\s+records\b", re.IGNORECASE),
        "multiple-record deliverable",
    ),
]
SCAN_FOR_CONTRACT_DRIFT = [
    "SKILL.md",
    "references/research-process.md",
    "references/evidence-needs-core.md",
    "references/query-and-source-patterns.md",
    "references/source-verification.md",
    "references/subagent-orchestration.md",
    "references/web-search-harness-maximization.md",
    "references/research-record-template.md",
    "scripts/plan_research.py",
    "scripts/query_matrix.py",
    "scripts/scaffold_record.py",
    "scripts/validate_record.py",
    "scripts/audit_record_consistency.py",
    "scripts/validate_research_record.py",
    "scripts/markdown_record.py",
    "scripts/research_taxonomy.py",
    "scripts/script_io.py",
]


def normalized_contains(text: str, needle: str) -> bool:
    return " ".join(needle.split()) in " ".join(text.split())


def read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def scan_contract_drift(failures: list[str]) -> None:
    for relative_path in SCAN_FOR_CONTRACT_DRIFT:
        path = ROOT / relative_path
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for line_number, line in enumerate(text.splitlines(), start=1):
            normalized = line.lower()
            if "do not" in normalized or "not create" in normalized:
                continue
            for pattern, label in FORBIDDEN_CONTRACT_PATTERNS:
                if pattern.search(line):
                    failures.append(
                        f"{relative_path}:{line_number} contains forbidden {label}"
                    )


def main() -> int:
    failures: list[str] = []

    skill_path = ROOT / "SKILL.md"
    agent_path = ROOT / "agents" / "openai.yaml"

    if not skill_path.exists():
        failures.append("missing SKILL.md")
    else:
        skill_text = read("SKILL.md")
        for heading in REQUIRED_SKILL_SECTIONS:
            if heading not in skill_text:
                failures.append(f"SKILL.md missing section {heading!r}")
        for phrase in REQUIRED_SKILL_CONTRACT:
            if not normalized_contains(skill_text, phrase):
                failures.append(f"SKILL.md missing contract phrase {phrase!r}")
        if MODE_HEADING_RE.search(skill_text):
            failures.append("SKILL.md appears to define a mode-like heading")

    if not agent_path.exists():
        failures.append("missing agents/openai.yaml")
    else:
        agent_text = read("agents/openai.yaml")
        for phrase in REQUIRED_AGENT_CONTRACT:
            if not normalized_contains(agent_text, phrase):
                failures.append(f"agents/openai.yaml missing contract phrase {phrase!r}")

    for relative_path in REQUIRED_REFERENCES:
        if not (ROOT / relative_path).exists():
            failures.append(f"missing referenced helper: {relative_path}")
    for relative_path in REQUIRED_HELPER_SCRIPTS:
        if not (ROOT / relative_path).exists():
            failures.append(f"missing helper script: {relative_path}")

    scan_contract_drift(failures)

    if failures:
        print("Research skill contract verification failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Research skill contract verification passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
