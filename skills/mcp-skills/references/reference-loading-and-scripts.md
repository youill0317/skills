# Reference Loading And Script Execution

## `reference_paths`

References do not load automatically.

Rules:

- Every path must be under `references/`.
- Pass only the files needed for the current task.
- Invalid or oversized reference requests appear in `warnings`.
- Check `loaded_references` to confirm what was actually included.

### Example

```json
{
  "skill_id": "workflow-orchestrator",
  "task": "Route a vault-backed report workflow.",
  "reference_paths": [
    "references/chaining-patterns.md"
  ]
}
```

## `execution.mode`

Allowed modes:

- `guide`
- `run_script`

### Script Example

```json
{
  "skill_id": "document-qa",
  "task": "Echo the task for smoke testing.",
  "execution": {
    "mode": "run_script",
    "script": "scripts/echo-task.js",
    "args": [
      "--format",
      "json"
    ]
  }
}
```

## Result Interpretation

- `script_result` appears only for `run_script`.
- `warnings` may indicate skipped references or blocked script usage.
- `available_references` and `loaded_references` are not the same thing.
