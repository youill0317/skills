# Decision Rules

Apply these checks before finalizing a plan.

## Decision-Complete Gate

A plan is complete only if:

1. No step requires the implementer to choose an unstated option.
2. Interfaces and outputs are specified where behavior changes.
3. Validation criteria are concrete and testable.
4. Risks are paired with mitigation actions.

## Ambiguity Handling

1. Classify unknowns:
   - discoverable facts
   - preference decisions
2. Resolve discoverable facts first.
3. For preference decisions, define defaults and mark assumptions.

## Sequencing Rules

1. Place dependency setup before dependent implementation.
2. Place safety checks before high-risk changes.
3. Place tests close to the behavior they verify.

## Quality Checks

1. Each implementation step has a completion condition.
2. Each major claim has a validation path.
3. Scope boundaries are explicit.
4. Rollback or mitigation path exists for high-impact risks.
