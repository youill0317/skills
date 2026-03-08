# `perspectives_task`

## Purpose

Run the fixed creative, critical, and logical agents in parallel on one shared topic.

## Input Shape

```json
{
  "task": "Assess the risks and opportunities of replacing workflow skills with MCP-named skills.",
  "context": "We want simpler maintenance and better MCP discoverability."
}
```

Fields:

- `task`: required string
- `context`: optional string

## When To Use

- Use when you want parallel ideation, critique, and logical structuring on the same topic.
- Do not use when you need one specialized tool-using agent with a narrow objective. Use `delegate_task` instead.

## Output Shape

Representative result:

```json
{
  "status": "success",
  "perspectives": [
    {
      "agent_id": "creative",
      "response": "{...json...}"
    },
    {
      "agent_id": "critical",
      "response": "{...json...}"
    },
    {
      "agent_id": "logical",
      "response": "{...json...}"
    }
  ],
  "total_tokens": {
    "input": 3000,
    "output": 1400
  }
}
```
