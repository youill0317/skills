# Parallel orchestration

Use this reference to turn an evolving conversation into safe concurrent work.

## Build the work graph

Track each work unit by a stable name, goal, dependencies, read/write scope, owner, success criteria, and current state. A unit is ready when its inputs and authority are available.

- Size a unit so one worker can finish and verify one coherent outcome in one turn: one question, one implementation surface, or one validation surface. Do not split merely by directory, step count, or token budget.
- Give each unit one goal and one deliverable. If a prompt contains independent goals, fan them out into separate units.
- Name each dependency as a deliverable plus required evidence, not merely “wait for worker X.”
- Dispatch independent read-only discovery immediately during brainstorming.
- Launch every ready independent unit before the first wait; never use `spawn → wait → spawn` for work that was ready together.
- Release downstream work from sufficient verified inputs; do not impose a global barrier. If a prerequisite exposes a stable interface or decision early, release only the dependent work that relies on that stable portion.
- Keep one available child slot for urgent verification, recovery, or a newly discovered branch when capacity permits.
- Assign one primary owner per work unit. Do not duplicate ordinary work merely to increase concurrency.
- Use independent duplicate analysis only for high-risk decisions, genuine alternative comparison, or conflict resolution.

## Worker assignment

Include this contract in every dispatch:

```text
Goal:
Context and inputs:
Owned paths or resources:
Read/write authority:
Evidence-gated dependencies:
Success criteria:
Verification commands and expected results:
Expected downstream handoff facts:
Stop and report conditions:
Report format: Outcome / Work completed / Evidence / Artifacts / Risks or blockers / Next action
Do not spawn subagents unless HQ explicitly authorizes it.
If scope must expand: stop and report the required paths or resources and why; do not edit them.
```

Use a stable name for the outcome, not the activity: prefer `auth-token-refresh-tests` to `inspect-auth`. Pass only the context needed to work independently. When selecting a child model or effort, use a bounded `fork_turns` value or `none` and include the required context explicitly.

## Mutation and ownership

- Keep brainstorming and feasibility workers read-only until the user authorizes change.
- Before parallel mutation, inspect applicable instructions and current dirty paths, then partition exact files or mutable resources into non-overlapping ownership sets.
- A worker may edit only its declared paths and files it creates within that boundary.
- Treat shared contracts, generated outputs, lockfiles, central registries, migrations, snapshots, and integration tests as separately owned resources. Assign one integration owner or serialize them.
- If safe ownership cannot be established, serialize the writers.
- A reviewer may read another worker's files but must not modify them unless HQ reassigns ownership.
- If work requires an unowned path, the worker must stop and request expansion. HQ resolves the overlap and explicitly transfers or extends ownership before any edit.
- Ownership ends only after HQ accepts the evidence. Keep repairs with the same owner unless HQ explicitly transfers the paths.
- Treat existing and unrelated worktree changes as user-owned.

## Ephemeral handoff briefs

After accepting a result that unlocks other work, extract only:

- verified conventions or facts;
- decisions and their rationale;
- affected paths and stable interfaces;
- successful verification commands;
- failures, gotchas, or prohibited approaches;
- unresolved assumptions.

Send the relevant brief to each newly ready worker. Keep it in conversation context only: do not create status files, global memory, a task dashboard, or forward raw transcripts and unverified speculation.

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

A unit is complete only when its stated outcome and required evidence are both present. For changes, require exact files changed, verification commands run, and observed results; a description of edits is not evidence.

After all relevant units complete, run or delegate integration verification across the combined acceptance criteria, cross-owner interfaces, and relevant test or build surface. Keep the verifier read-only unless ownership is explicitly reassigned.

Repair missing evidence or failed criteria in the same worker thread where practical. Accept no final synthesis until every acceptance criterion is evidenced or explicitly recorded as unresolved.
