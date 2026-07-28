# Subagent routing

Apply these rules only to subagents. Never set or infer the root model or root reasoning effort.

## Defaults

| Work | Preferred model | Effort |
|---|---|---|
| Targeted read-only code mapping, symbol lookup, pattern search, and test discovery | `gpt-5.3-codex-spark` | `medium` |
| Narrow, fully specified, low-risk coding iteration with quick verification | `gpt-5.3-codex-spark` | `medium` |
| Broad code, file, documentation, log, and large-test-result scans | `gpt-5.6-terra` | `medium` |
| Read-heavy synthesis and dependency analysis | `gpt-5.6-terra` | `medium`, or `xhigh` under the gates below |
| Implementation, refactoring, debugging, architecture, and ordinary review | `gpt-5.6-sol` | `medium` |
| Security, destructive-risk analysis, difficult multi-cause failure, or materially costly judgment | `gpt-5.6-sol` | `xhigh` |

Limit subagent routing to `gpt-5.3-codex-spark`, `gpt-5.6-terra`, and `gpt-5.6-sol`, with only `medium` and `xhigh`. Spark is `medium`-only. Never request or invent another model identifier or effort. An explicit user choice overrides the defaults only when it stays inside this allowlist and the current runtime supports the pair, unless the user explicitly changes the HQ routing policy itself.

## Choose XHigh

Start with `xhigh` only for a high-risk decision, a complex cross-system design, a difficult multi-cause failure, or an independent final judgment where an error is materially costly.

Otherwise start with `medium` and escalate once only when:

1. the output fails an explicit success criterion or verification;
2. missing context, evidence, tools, permissions, and dependencies have been ruled out or repaired; and
3. the remaining failure is genuinely reasoning-bound.

`xhigh` is not a model-selection shortcut. Keep Terra on `xhigh` only when the same read-heavy task needs unusually deep synthesis. Reassign to Sol `medium` or `xhigh` when the task has become implementation, architecture, or complex technical judgment. Never request Spark `xhigh`.

Independent review alone is not a reason to use `xhigh`. Keep ordinary implementation review on Sol `medium`; use `xhigh` only when the review itself meets the high-risk or reasoning-failure criteria above.

## Capability fallback

- Inspect the callable `spawn_agent` schema or tool description before every override. Treat a model-effort pair as usable only when the current runtime exposes or documents it; do not infer availability from product documentation alone.
- Model and effort overrides require a non-`all` context fork; provide the necessary context in the task prompt.
- If Spark `medium` is unavailable, use Terra `medium` for read-heavy exploration or Sol `medium` for coding.
- If Terra is unavailable, use Sol `medium`.
- If Sol is unavailable, use Terra `medium` only for read-only or bounded low-risk work. Report demanding implementation or high-risk judgment as lacking a compliant route; do not silently inherit or change the root model.
- If `xhigh` is unsupported, use the same model at `medium`, decompose the task or add an independent reviewer, and report the fallback on the next material transition.
- If no allowlisted supported pair fits, do not set an override and do not spawn that unit under this policy.
- Do not select a custom agent whose pinned model or effort falls outside the allowlist.

## Retry and reassignment

- Repair the prompt or dependency instead of raising effort when the failure is not reasoning-bound.
- Retry the same responsibility once after correcting the cause.
- After a failed corrected retry, re-plan the unit or reassign it to the appropriate model; do not loop.
- Use a separate reviewer for conflicting results or material changes rather than escalating every worker.
