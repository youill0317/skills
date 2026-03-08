# `run_skill` Guide Mode

## Default Behavior

Guide mode compiles the selected `SKILL.md` body and any explicitly loaded references.

One `run_skill` call loads one skill. If the workflow needs multiple skills, call `run_skill` again for the next skill in the chain.

## Required Arguments

```json
{
  "skill_id": "mcp-search",
  "task": "Choose the best `mcp_search` tool for academic paper lookup."
}
```

Required fields:

- `skill_id`
- `task`

Optional fields:

- `inputs`
- `reference_paths`
- `execution`

Notes:

- `skill_id` must match the installed skill ID from `list_skills`.
- MCP server names such as `mcp_search` are not valid substitutes for skill IDs such as `mcp-search`.

## Example With Inputs And References

```json
{
  "skill_id": "mcp-search",
  "task": "Show how to call Tavily extraction on known URLs.",
  "inputs": {
    "audience": "developer",
    "need_examples": true
  },
  "reference_paths": [
    "references/tavily.md"
  ]
}
```

## Output Shape

Representative result:

```json
{
  "skill_id": "mcp-search",
  "skill_name": "mcp-search",
  "skill_description": "Guide for the `mcp_search` server and its tools.",
  "compiled_instructions": "# Skill: ...",
  "available_references": [
    "references/tavily.md"
  ],
  "loaded_references": [
    {
      "path": "references/tavily.md",
      "bytes": 1234
    }
  ],
  "warnings": []
}
```
