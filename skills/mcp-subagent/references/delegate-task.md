# `delegate_task`

## Purpose

Send one focused task to one chosen sub-agent.

## Input Shape

```json
{
  "agent_id": "researcher",
  "task": "Collect 3 reliable sources about model context protocol adoption and summarize the main differences.",
  "context": "Keep the answer evidence-first and note unresolved conflicts."
}
```

Fields:

- `agent_id`: required string
- `task`: required string
- `context`: optional string

## Task-Writing Rules

- Include the deliverable inside `task`.
- Do not assume the agent saw prior conversation unless you pass it.
- Keep `context` short and relevant.

## Output Shape

Representative result:

```json
{
  "status": "success",
  "agent_id": "researcher",
  "response": "{...json...}",
  "metadata": {
    "run_id": "abc123",
    "duration_ms": 5321,
    "stop_reason": "completed",
    "retries": 0,
    "iterations": 4,
    "tool_calls_made": 6,
    "tokens": {
      "input": 1200,
      "output": 600
    }
  }
}
```
