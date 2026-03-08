# `list_agents`

## Purpose

Discover available agents, their roles, providers, connected MCP servers, and exposed tools.

## Input Shape

`list_agents` takes no parameters.

```json
{}
```

## Output Shape

Representative result:

```json
{
  "status": "success",
  "agents": {
    "researcher": {
      "description": "Research and web-search specialist agent.",
      "provider": "anthropic",
      "model": "claude-sonnet-4-20250514",
      "available_tools": [
        "mcp_search__brave_web_search",
        "mcp_skills__list_skills"
      ],
      "mcp_servers": [
        {
          "name": "mcp_search",
          "status": "connected"
        }
      ]
    }
  },
  "server_health": {}
}
```

## Interpretation Notes

- Use this before `delegate_task` when agent/tool mapping is unknown.
- `available_tools` uses the server-prefixed form `<server_name>__<tool_name>`.
- `available_tools` is the fastest way to see whether an agent can search, read vault files, or access skills.
