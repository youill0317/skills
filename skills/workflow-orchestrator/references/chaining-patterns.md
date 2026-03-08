# Chaining Patterns

## Pattern 1: External Research

1. `list_skills`
2. `run_skill` for `mcp-search`
3. Use `mcp_search` tools
4. Optional second `run_skill` for `report-writer`, `paper-writing`, or `presentation-design`

## Pattern 2: Vault-Backed Answer

1. `list_skills`
2. `run_skill` for `mcp-obsidian`
3. Use `mcp_obsidian` tools to discover and read evidence
4. A later `run_skill` for `document-qa` or `document-summary`

## Pattern 3: Subagent-Assisted Investigation

1. `list_skills`
2. `run_skill` for `mcp-subagent`
3. Inspect agents with `list_agents` if needed
4. Run `delegate_task` or `perspectives_task`
5. Hand off results to a later writing or planning skill if needed

## Pattern 4: Skill Discovery Problem

1. `list_skills`
2. `run_skill` for `mcp-skills`
3. Use `list_skills` output to choose the next skill
4. Call `run_skill` for the selected MCP main or work-product skill
