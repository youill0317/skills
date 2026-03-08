---
name: workflow-orchestrator
description: Orchestrate multi-skill workflows across MCP main skills and work-product skills. Use when the user asks what skills to chain, what order to read them in, or how to combine `mcp_search`, `mcp_obsidian`, `mcp_skills`, `mcp_subagent`, and output-oriented skills for one task.
---

# Mission

Choose the right skill chain and reading order when a task spans multiple MCPs or multiple stages.

## Scope

1. Route between MCP main skills and work-product skills.
2. Focus on sequencing and handoff boundaries.
3. Do not duplicate provider-specific parameter catalogs from MCP main skills.
4. Do not replace the detailed writing rules of work-product skills.

## Core Workflow

1. Start with `list_skills` and identify whether the task needs external web data, local markdown evidence, delegation, or deliverable writing.
2. Read `mcp-skills` first when the task is about skill discovery, `skill_id` selection, `reference_paths`, or `run_skill` behavior itself.
3. Read the relevant MCP main skill before direct tool use.
4. Chain into work-product skills only after evidence collection or routing is settled.
5. Keep the number of loaded skills minimal.

## Common Chains

- Web research then report: `mcp-skills` -> `mcp-search` -> `report-writer`
- Vault discovery then Q&A: `mcp-skills` -> `mcp-obsidian` -> `document-qa`
- Vault discovery then summary: `mcp-skills` -> `mcp-obsidian` -> `document-summary`
- Multi-agent investigation: `mcp-skills` -> `mcp-subagent` -> optional work-product skill
- Planning with evidence gathering: `mcp-skills` -> `mcp-search` or `mcp-obsidian` -> `plan-skill`

## Resource Loading

- Load `references/chaining-patterns.md` for concrete chain templates.
- Load `references/decision-rules.md` for routing rules and stage boundaries.
