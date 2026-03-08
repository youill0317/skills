---
name: mcp-subagent
description: Guide for the `mcp_subagent` server and its tools. Use when users ask how to inspect agents, delegate tasks, run multi-perspective analysis, choose agent targets, or structure `mcp_subagent` calls and examples.
---

# Mission

Operate `mcp_subagent` reliably for delegation and structured multi-agent work.

## Scope

1. Cover `list_agents`, `delegate_task`, and `perspectives_task`.
2. Explain how to choose an agent and how to write self-contained tasks.
3. Explain what context to pass and what to omit.
4. Clarify the shape of the returned JSON payloads.

## Operating Rules

1. Use `list_agents` before delegation when available agents or tool access are unclear.
2. Keep delegated tasks self-contained.
3. Pass only essential `context`.
4. Use `perspectives_task` when the same topic should be challenged from fixed creative, critical, and logical viewpoints.
5. Treat subagent output as structured intermediate material, not final presentation.

## Tool Coverage

- `list_agents`
- `delegate_task`
- `perspectives_task`

## Resource Loading

- Load `references/list-agents.md` for agent inspection.
- Load `references/delegate-task.md` for targeted delegation.
- Load `references/perspectives-task.md` for fixed multi-perspective runs.
- Load `references/task-writing-guide.md` for task and context construction.
