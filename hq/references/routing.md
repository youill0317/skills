# Subagent routing

Apply these rules only to subagents. Never set or infer the root model or root reasoning effort.

## Defaults

| Work | Preferred model | Effort |
|---|---|---|
| Code, file, documentation, log, and test discovery | `gpt-5.6-terra` | `medium` |
| Read-heavy synthesis and dependency analysis | `gpt-5.6-terra` | `medium` |
| Implementation, refactoring, debugging, and review | `gpt-5.6-sol` | `medium` |
| Security, destructive-risk analysis, or other high-cost judgment | `gpt-5.6-sol` | `xhigh` |
| Narrow latency-sensitive coding iteration | Spark, only when exposed by the current spawn schema | `medium` |

Use only `medium` and `xhigh` for automatic routing. Do not automatically select `none`, `low`, `high`, or `max`. An explicit user choice for a subagent overrides these defaults when the runtime supports it.

## Choose XHigh

Start with `xhigh` only for a high-risk decision, a complex cross-system design, a difficult multi-cause failure, or an independent final judgment where an error is materially costly.

Otherwise start with `medium` and escalate once only when:

1. the output fails an explicit success criterion or verification;
2. missing context, evidence, tools, permissions, and dependencies have been ruled out or repaired; and
3. the remaining failure is genuinely reasoning-bound.

Keep Terra on `xhigh` only when the same read-heavy task needs deeper synthesis. Reassign to Sol `medium` or `xhigh` when the task has become implementation, architecture, or complex technical judgment.

Independent review alone is not a reason to use `xhigh`. Keep ordinary implementation review on Sol `medium`; use `xhigh` only when the review itself meets the high-risk or reasoning-failure criteria above.

## Capability fallback

- Inspect the current `spawn_agent` schema before requesting a model or effort override.
- Model and effort overrides require a non-`all` context fork; provide the necessary context in the task prompt.
- Use Spark only if the current schema exposes both the model and the required effort. Otherwise use Terra `medium` for exploration or Sol `medium` for coding.
- If `xhigh` is unsupported, use the same supported model at `medium` and report the fallback on the next material status transition.
- If the preferred model is unavailable, select the supported Terra/Sol role match at `medium`; never invent a model identifier.

## Retry and reassignment

- Repair the prompt or dependency instead of raising effort when the failure is not reasoning-bound.
- Retry the same responsibility once after correcting the cause.
- After a failed corrected retry, re-plan the unit or reassign it to the appropriate model; do not loop.
- Use a separate reviewer for conflicting results or material changes rather than escalating every worker.
