# `list_skills`

## Purpose

Enumerate installed skills and their available reference files.

## Input Shape

`list_skills` takes no parameters.

```json
{}
```

## Output Shape

Representative result:

```json
{
  "skills": [
    {
      "id": "mcp-search",
      "name": "mcp-search",
      "description": "Guide for the `mcp_search` server and its tools.",
      "references": [
        "references/brave.md",
        "references/tavily.md"
      ]
    }
  ],
  "count": 1,
  "warnings": []
}
```

## Interpretation Notes

- Use `list_skills` as the default first step before choosing direct MCP tools for a non-trivial task.
- `id` is the value used as `skill_id` in `run_skill`.
- `id` is a skill ID such as `mcp-search`; it is not the same as an MCP server name such as `mcp_search`.
- `references` lists files that may be passed through `reference_paths`.
- Discovery is metadata-only. It does not load the skill body or references.
