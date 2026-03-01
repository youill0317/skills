---
name: plan-skill
description: Create decision-complete execution plans for tasks and projects. Use when the user asks for planning, scoping, implementation breakdown, sequencing, risk handling, testing strategy, or acceptance criteria before execution.
---

# Mission

Produce actionable plans that leave no implementation decisions unresolved.

## Core Rules

1. Define goal, success criteria, and audience.
2. Separate in-scope and out-of-scope items.
3. Capture constraints, dependencies, and assumptions.
4. Specify interfaces or I/O changes when relevant.
5. Break work into ordered steps with completion conditions.
6. Include testing strategy and acceptance criteria.
7. Identify risks and concrete mitigations.

## Planning Workflow

1. Normalize the request into a clear objective statement.
2. Extract known facts and unknowns.
3. Resolve discoverable unknowns before planning.
4. Lock major technical decisions and defaults.
5. Draft implementation steps with ownership and order.
6. Define verification scenarios for normal and failure paths.
7. Finalize assumptions and unresolved questions explicitly.

## Output Standard

Always include:

1. Title
2. Brief summary
3. API/interface or behavior changes
4. Step-by-step implementation plan
5. Test cases and scenarios
6. Risks and mitigations
7. Explicit assumptions/defaults

## Resource Loading

- Load `references/plan-template.md` for the full plan skeleton.
- Load `references/decision-rules.md` for decision-complete quality checks.
