# Subagents

Assign each lane one bounded evidence need, claim set, source family,
jurisdiction, dataset, version, counterevidence path, or provenance path. Give it
only the question, scope, access boundary, and required return fields. Do not
leak an expected conclusion. Pre-screen candidate locators and do not assign
artifacts that are clearly unrelated to the lane's material need.

Require message-only returns containing:

- sources inspected with stable locators and evidence locations;
- observations separated from inference;
- material leads, counterevidence, blocked access, and confidence limits.

Keep one main-agent-owned research record. Subagents must not create or edit it.
The main agent must verify every underlying source used by a final claim. After
parallel lanes return, synthesize before opening another lane. Add one only when
a returned lead remains material and reachable inside the authorized boundary.
