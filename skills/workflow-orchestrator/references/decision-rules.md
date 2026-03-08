# Routing Decision Rules

# Default Rule

- start with `list_skills` before direct MCP tool use on non-trivial tasks
- use `run_skill` to load the relevant skill before choosing tools or parameters

## Choose `mcp-search` When

- facts are external
- recency matters
- citations or URLs are required
- academic paper metadata is required

## Choose `mcp-obsidian` When

- the evidence lives in local markdown
- file paths are unknown
- note links or backlinks matter
- section-level reading is enough

## Choose `mcp-skills` When

- you are starting discovery and need to see the installed skills
- you do not know which skill to read
- you need `reference_paths`
- you need guide vs script execution behavior

## Choose `mcp-subagent` When

- delegation is part of the task
- multiple viewpoints are valuable
- one agent should work in parallel from a self-contained brief

## Choose Work-Product Skills When

- the task is now about answering, summarizing, reporting, planning, paper drafting, or presentation design rather than tool operation
