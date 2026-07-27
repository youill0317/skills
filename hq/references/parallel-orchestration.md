# Parallel orchestration

Use this reference to turn an evolving conversation into safe concurrent work.

## Build the work graph

Track each work unit by a stable name, goal, dependencies, read/write scope, owner, success criteria, and current state. A unit is ready when its inputs and authority are available.

- Split by independently verifiable outcome, not by arbitrary size.
- Dispatch independent read-only discovery immediately during brainstorming.
- Start downstream work from sufficient partial results; do not impose a global barrier.
- Keep one available child slot for urgent verification, recovery, or a newly discovered branch when capacity permits.
- Assign one primary owner per work unit. Do not duplicate ordinary work merely to increase concurrency.
- Use independent duplicate analysis only for high-risk decisions, genuine alternative comparison, or conflict resolution.

## Worker assignment

Include this contract in every dispatch:

```text
Goal:
Context and inputs:
Scope and ownership:
Read/write authority:
Dependencies:
Success criteria:
Required evidence:
Stop and report conditions:
Report format: Outcome / Work completed / Evidence / Artifacts / Risks or blockers / Next action
Do not spawn subagents unless HQ explicitly authorizes it.
```

Pass only the context needed to work independently. When selecting a child model or effort, use a bounded `fork_turns` value or `none` and include the required context explicitly.

## Mutation and ownership

- Keep brainstorming and feasibility workers read-only until the user authorizes change.
- Before parallel mutation, partition files or mutable resources into non-overlapping ownership sets.
- If safe ownership cannot be established, serialize the writers.
- A reviewer may read another worker's files but must not modify them unless HQ reassigns ownership.
- Treat existing and unrelated worktree changes as user-owned.

## Steering

- Send new constraints to every affected running worker promptly.
- Preserve unaffected workers when the user changes direction.
- Interrupt obsolete, unauthorized, or unsafe work.
- If a result reveals a new independent question, dispatch it without waiting for the rest of the batch.
- If a worker drifts, correct it before completion. If the worker is already idle, continue the same responsibility with `followup_task` rather than creating a replacement.
- On failure, classify the cause before retrying: missing context, missing evidence, tool/runtime failure, permission boundary, dependency, or reasoning failure.

## Common patterns

### Brainstorming

Keep discussing goals and tradeoffs while separate read-only workers inspect the codebase, official sources, and current tests. Merge findings at natural decision points.

### Implementation

Convert the accepted design into non-overlapping implementation units, test analysis, and documentation checks. Run safe units concurrently, then assign an independent reviewer.

### Debugging

Fan out logs, recent changes, runtime configuration, and suspect code paths. Use early findings to launch reproduction or focused verification. Do not collapse conflicting diagnoses without a reviewer.

### Direction change

Forward additive constraints, redirect reusable work, interrupt only obsolete branches, and rebuild downstream dependencies. Tell the user only when a material transition occurs.

## Completion

Accept a worker result only when its evidence satisfies the stated success criteria. Repair gaps in the same worker thread where practical. Integrate conclusions, not raw transcripts, and expose residual uncertainty.
