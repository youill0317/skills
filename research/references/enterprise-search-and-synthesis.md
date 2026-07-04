# Enterprise Search And Knowledge Synthesis

Use these patterns only when the user explicitly asks for internal or connected-source research and the needed sources are authorized in the current session. In Gigantum-Humeris workspaces, MCP-backed local access must stay within the current workspace and the user-configured global markdown wiki path. Research records belong at `gigantum-humeris/research/<NNN-topic>.md`.

## Source-Family Planning Map

Before searching broadly, map likely source families. This is a planning aid,
not a replacement for durable `## Sources`, `## Evidence`, and `## Evidence
Ledger` sections in the single research record.

| Source family | Good for | Watch for |
|---|---|---|
| Docs/wiki | canonical policy, decisions, specs | stale pages, outdated owners |
| Tickets/issues | implementation history, edge cases | partial context, duplicate tickets |
| Chat/meeting notes | rationale, objections, unresolved questions | informal claims, missing decisions |
| Repositories | actual behavior, configs, tests | local changes, dead code |
| CRM/support | customer impact, objections, frequency | anecdotal bias, privacy constraints |
| BI/analytics/finance | operating metrics, revenue, usage, cohort behavior | dashboard definitions, stale extracts, access limits |
| Security/compliance/legal | risk, controls, incidents, obligations, approvals | privilege, regulated data, incomplete applicability |

## Enterprise Lane Presets

Use these lane presets when internal or connected sources are part of the
research question:

| Lane | Source Families | Strong Evidence | Weak Evidence |
|---|---|---|---|
| source-of-truth docs | policy, approved specs, canonical docs | current owner-approved doc or decision record | stale wiki page, orphaned notes |
| implementation reality | repos, configs, tests, releases, logs | merged code, production config, release tag, verified runtime behavior | roadmap, PR discussion, unmerged branch |
| decision history | decision records, meeting notes, tickets | approved decision record with owner/date | chat recollection, unresolved meeting discussion |
| customer/support impact | CRM/support, aggregated cases, customer research | aggregate metrics with denominator and segment | isolated anecdote or single ticket |
| risk/compliance/security | legal, security, compliance, incidents | governing policy, control record, official finding | informal interpretation without owner review |
| stale-doc/counterevidence | archives, superseded docs, conflicting tickets | later superseding source or direct contradiction | vague objection without record |

## Permission And Access Boundary

Use only sources, connectors, and paths that are currently authorized and available in the session. Do not search arbitrary local folders, private systems, chats, support records, CRM records, or personal data unless the user requested that source family and access is authorized. Before treating a missing result as evidence, distinguish:

- searched and accessible
- relevant but not accessible
- accessible but outside the user's requested scope
- not searched because it would expose unnecessary sensitive records

Record searched systems and relevant inaccessible systems in the synthesis. Do
not request, export, or expose sensitive records unless they are necessary for
the user's stated purpose. Mark evidence gaps caused by permissions as `not
accessible`, not `not found`.

For each internal or connected source family, record:

| Field | Values |
|---|---|
| Access Basis | user-provided / connector-authorized / workspace-local / explicitly approved / denied / unclear |
| Sensitivity | public / internal / confidential / personal / regulated / legally sensitive / privileged |
| Minimum Necessary | yes / no / unclear |
| Redistribution | unrestricted / internal only / restricted / do not quote / metadata only |
| Exclusion Reason | out of scope / not authorized / unnecessary sensitive data / unavailable / not searched |

Do not infer permission from connector visibility alone. If source sensitivity or
access basis is unclear, use non-sensitive alternatives first and record the
gap.

## Search Strategy

1. Start with entity names, project codenames, filenames, and exact phrases.
2. Add synonyms only after finding the dominant vocabulary used by the organization.
3. Search for decisions and objections separately: `approved`, `rejected`, `blocked`, `risk`, `tradeoff`, `follow-up`.
4. Track source lineage so one repeated claim from the same document chain is not mistaken for independent corroboration.
5. Prefer current canonical docs for policy or process, and raw records for examples or frequency.
6. Maintain a frontier queue: every material object ID, linked document,
   ticket, repository reference, dashboard, owner, meeting, customer segment,
   blocked source family, contradiction, and stale-doc path is followed,
   closed, blocked with confidence effect, or marked unable to change the
   decision before synthesis.

For enterprise systems, prefer exact object identifiers over broad keyword
search when available: document title, ticket ID, pull request number, commit
SHA, dashboard name, metric ID, meeting date, account segment, case ID, release
tag, policy ID, control ID, or owner/team name.

## Freshness Pass

For internal synthesis, check source freshness before finalizing:

- docs/wiki: owner, last modified date, archived/superseded status, linked
  canonical page, and open comments
- tickets/issues: status, resolution, assignee, linked duplicates, close date,
  reopen history, and release or milestone
- chat/meeting notes: meeting date, participants, whether a decision was made,
  and whether a later doc/ticket supersedes the discussion
- repositories: merged commit date, branch status, release tag, test/config
  reality, and whether code is dead or behind a flag
- CRM/support: case lifecycle, account/segment, support status, duplicate cases,
  privacy constraints, and whether the record reflects one customer or a pattern

State an as-of timestamp when the internal answer depends on current status.

For mutable connector-backed sources, record the source system, owner when
visible, version/revision ID when available, retrieved timestamp, and whether
the inspected material was original, export, cached view, excerpt, or summary.

## Synthesis

For each important claim, record:

| Claim | Decision/provenance | Best source | Supporting sources | Counterevidence | Date/version/status | Owner/team | Confidence | Action implication |
|---|---|---|---|---|---|---|---|---|

Confidence should reflect source authority, recency, independence, and whether the source directly answers the question.

Also assign `Decision-use status` for claims that affect an enterprise action:

- `usable`: evidence is adequate for the scoped decision
- `usable with caveats`: evidence supports the decision only under stated
  assumptions, limits, or pending owner checks
- `requires owner review`: a business, legal, security, data, finance, or
  compliance owner must review before operational use
- `not decision-ready`: evidence is too weak, inaccessible, sensitive, stale,
  conflicting, or outside scope for the decision

Separate proposed, approved, implemented, rolled back, and merely discussed
decisions. Do not flatten discussion notes into decisions unless a source shows
approval or implementation.

## Internal Conflict Handling

When internal sources conflict:

1. Group evidence by system, owner, date, and lineage.
2. Prefer current source-of-truth docs for policy, process, and intended design.
3. Prefer merged code, configs, tests, logs, or releases for actual behavior.
4. Prefer ticket state and release/milestone data for implementation status.
5. Prefer CRM/support records for customer impact, frequency, and objections,
   while accounting for anecdotal and privacy limits.
6. Treat chat and meeting notes as rationale or leads unless they are the only
   available decision record.
7. Preserve unresolved conflicts with owner, date, and action needed.

## Enterprise Source Hierarchy

When internal sources conflict, apply the hierarchy that matches the claim:

| Claim Type | Prefer | Treat As Weaker |
|---|---|---|
| policy/process | canonical policy, approved decision record, named owner update | meeting notes, chat, copied wiki page |
| implementation status | production config/log/release, merged code, tests, release tag | roadmap, PR discussion, unmerged branch |
| customer impact | aggregate CRM/support metrics with denominator, user research method notes | isolated ticket, anecdotal sales/support comment |
| finance/business | audited or governed BI dashboard, official finance model, filing | copied spreadsheet, slide claim, chat estimate |
| security/compliance | governing control, incident record, policy, official owner response | informal interpretation, partial checklist |
| strategy/roadmap | approved strategy/roadmap record, owner statement with date | brainstorm, draft, meeting discussion |

When none of the preferred sources are accessible, label the conclusion with the
source-family gap and avoid presenting the weaker source as authoritative.

## Enterprise Frontier Queue

For internal or connected-source research, frontier queue convergence is part
of permission-aware saturation. Record material leads from object links,
owners, mentions, duplicate tickets, dashboard definitions, code references,
meeting follow-ups, stale-doc supersession paths, support clusters, and blocked
systems in the single research record. Close each lead as followed,
duplicate-lineage, blocked by access/sensitivity, out of scope, low quality,
superseded, or unable to change the decision. If a blocked internal source
family could materially change a decision, downgrade decision-use status or mark
owner review required.
