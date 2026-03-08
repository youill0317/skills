# Task Writing Guide For `mcp_subagent`

## Self-Contained Task Pattern

Good pattern:

```text
Goal + deliverable + constraints + evaluation criteria
```

Example:

```text
Compare Tavily and Exa for known-URL extraction. Return 3 findings, 2 tradeoffs, and 1 recommendation. Prefer concrete parameter differences. Do not write marketing language.
```

## Context Pattern

Use `context` only for:

- prior findings that matter
- constraints the agent must honor
- source material the agent cannot rediscover cheaply

Avoid putting the full task again into `context`.

## Agent Choice Pattern

- `researcher`: external evidence and search-heavy work
- `analyst`: vault-backed or document interpretation work
- `creative`: idea generation
- `critical`: risk and flaw finding
- `logical`: structure and synthesis
