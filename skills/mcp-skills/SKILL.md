---
name: mcp-skills
description: Guide for the `mcp_skills` server and its tools. Use when users ask how to discover installed skills, call `run_skill`, pass `reference_paths`, use script execution modes, or interpret `mcp_skills` results.
---

# Mission

Operate `mcp_skills` precisely so skill discovery, reference loading, and script execution behave predictably.

## Scope

1. Cover `list_skills` and `run_skill`.
2. Explain `reference_paths`, `inputs`, and `execution` usage.
3. Clarify that references do not load automatically.
4. Clarify when `run_script` is allowed and how results are returned.

## Operating Rules

1. Use `list_skills` first as the default discovery step before direct MCP tool use on non-trivial tasks.
2. Use `run_skill` in `guide` mode by default.
3. Each `run_skill` call loads exactly one `skill_id`; multi-skill workflows are built by calling `run_skill` multiple times in sequence.
4. Pass only the needed `reference_paths`.
5. Use `run_script` only for allow-listed scripts under the target skill.
6. Read warnings and `loaded_references` instead of assuming every requested file loaded.

## Tool Coverage

- `list_skills`
- `run_skill`

## Resource Loading

- Load `references/list-skills.md` for discovery behavior.
- Load `references/run-skill-guide.md` for guide mode arguments and examples.
- Load `references/reference-loading-and-scripts.md` for `reference_paths`, `execution`, and result interpretation.
