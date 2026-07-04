# Subagent Orchestration

Use this reference to run research as main-agent orchestration plus independent
research and verification lanes while preserving the single-record contract.

## Main Agent Role

The main agent owns framing, lane design, search matrix, claim inventory, source
IDs, source integration, lead expansion decisions, synthesis, confidence labels,
the final answer, and the single research record.

Research subagents collect evidence in parallel lanes. Verification subagents
independently audit the integrated draft before final synthesis.

The main agent is the only writer for research records. Research and
verification subagents must not create, modify, delete, or move files or
directories. Do not create lane folders, scratch folders, task folders, source
folders, screenshot folders, claim-graph files, or per-subagent record folders.
A subagent may be told the selected record path for context, but it must return
structured output for the main agent to integrate into the single research
record.

Default to subagent-backed research when subagent use is available and
permitted by the active environment. If subagents are unavailable or disallowed,
the main agent must run the same lanes sequentially and record the fallback in
`## Verification Notes`.

Self-audit is a transparency fallback, not independent review. Research that
uses only self-audit cannot be labeled `professional-grade`,
`research-firm-replacement`, or independently verified.

## Research Lanes

Before source discovery, create independent research lanes from the evidence
needs and source families. Use as many lanes as the task requires, typically
three to eight for broad work, but keep each lane focused on a distinct claim
set, source family, jurisdiction, product/version, failure mode, method,
provenance path, or source-family gap that can be searched without waiting on
another lane.

Use these lane floors unless the user set a tighter budget or the environment
cannot support them:

- narrow single topic: at least three lanes or direct passes
- web-only broad topic: at least six lanes/passes
- codebase plus web topic: at least seven lanes/passes
- multi-faceted diligence: at least ten lanes/passes
- full due diligence or high-stakes research: at least twelve lanes/passes plus
  verification lanes

When subagents are available, launch the first wave together instead of
serializing one lane at a time. If subagents are not available, keep the same
lane map and run it sequentially.

Use worker-wave discipline:

- wave 0 establishes framing, query matrix, lane ownership, and stop gates
- wave 1 runs broad scout workers across independent source families
- wave 2 runs target and snowball workers from the best seeds
- wave 3 runs EXPAND, counter-search, currentness, provenance, and gap workers
- wave 4 runs independent verification and synthesis-overreach workers

Do not accept a thin worker output as complete. A thin worker output gives only
a narrative answer, lacks search paths, lacks inspected source locations,
returns no follow-up leads or closure reasons, omits applicable counter-search
or currentness checks, or fails to state what would change its lane conclusion.
Mark thin outputs as coverage debt, then rerun the missing pass directly or
launch a follow-up lane. If the debt cannot be cleared, tie it to a visible
confidence downgrade before synthesis.

Common lanes:

- official, governing, source-of-truth, or primary-record evidence
- currentness, latest-update, supersession, changelog, docket, advisory, or
  status-page evidence
- counterevidence, limitations, failed replications, rebuttals, corrections, or
  negative cases
- source lineage, provenance, duplicated reporting, original-source tracing,
  archives, and citation-chain checks
- domain-specific evidence, such as scholarly, market, product, OSS, legal,
  regulatory, policy, or technical implementation research
- observed behavior, user/community evidence, support traces, or public
  sentiment when those sources are relevant to the claim
- method, dataset, benchmark, survey, or causal-identification audit when
  empirical evidence matters

Dispatch independent research lanes in parallel. When a lane depends on the
candidate pool from another lane, run it as a second-wave lane after
integration unless it can work from known canonical sources independently.

Do not underspecify lanes. Each lane needs an owner boundary, a search matrix
slice, required source families, counter-search terms, expected inspected-source
output, and an explicit request for follow-up leads. A lane that returns only a
summary without search path, source locations, and leads is incomplete.

Each research subagent performs source discovery for its lane using the
essential source metadata in `research-record-template.md` as the output target.
The main agent integrates and spot-checks sources, assigns final source IDs, and
launches follow-up lanes when gaps remain.

## Research Subagent Contract

Give each research subagent only the task framing, its lane assignment, relevant
scope constraints, required source metadata, and expected output. Do not ask
research subagents for final synthesis.

Every research subagent prompt must say:

- this is an explicit exhaustive research assignment
- default stop-when-answered behavior does not apply
- use at least two cycles for the assigned theme: landscape, then targeted gap
- return every lead that could change an important claim
- maintain a frontier queue for the lane: convert every material result,
  opened source, citation, dataset, repository, issue, author, institution,
  local term, counterclaim, correction, archive target, and blocked primary
  source into a lead or close it with a reason
- continue until the latest expansion or gap cycle produces no new high-value
  leads, or remaining material leads are duplicate lineage, blocked, out of
  scope, low quality, or unable to change important claims
- send `WORKING: <lane> - <phase>` before long passes
- send `BLOCKED: <reason>` only when progress truly stops
- inspect source bodies where the lane uses a source as evidence
- include an `## EXPAND` tail listing every lead or `none` with a reason
- include `## CLAIMS` for claim candidates, with risk, support,
  counterevidence, primary-source status, and currentness notes
- return message text only and do not write files or create directories

For enterprise or sensitive research, minimize subagent inputs. Pass only the
source paths, metadata, bounded excerpts, or de-identified facts needed for the
lane. Do not give every subagent confidential, personal, regulated, privileged,
or customer-identifying material by default.

Each research subagent must return:

- lane ID, lane name, and scope
- search-path notes, including lane ID, pass type, query/path, source family,
  result, and follow-up where useful
- source rows or source notes matching the essential `## Sources` table where
  available; use `unknown` rather than guessing
- observation candidates with inspected source locations
- lead list with proposed follow-up searches, priority, and likely confidence
  effect
- closed leads with closure reasons
- frontier queue convergence status for the lane, including the latest
  expansion or gap cycle result and any remaining material open leads
- claims supported, weakened, contradicted, or left unresolved
- high-risk claim candidates that may need the verified-claim gate
- currentness and date/version checks when relevant
- confidence and unresolved gaps for the lane only
- access basis, sensitivity, and minimum-necessary notes for internal or
  connected sources when applicable
- suggested record updates by section, but no direct file edits

After research subagents return, close or stop using them for verification.
Integrate their outputs into a single claim inventory, source table, wave log,
observation manifest, evidence ledger, and provisional synthesis. Resolve
duplicate source IDs and duplicate source lineages before verification.

Before using subagent rows as record inputs, validate that source IDs are not
invented, metadata is marked `unknown` rather than guessed, evidence locations
exist for used sources, confidence does not exceed the source quality, and
internal source sensitivity/access notes are preserved.

Do not treat subagent agreement as evidence. Subagent outputs are leads and
work products; inspected sources and retrieved records are the evidence.

## EXPAND Follow-Up

The main agent must review every lane output before synthesis. Launch a
targeted follow-up lane, or run the same check directly, when a lane reveals:

- weak support for an important claim
- missing inspected source bodies or evidence locations
- conflicting evidence or unclear definitions
- missing currentness, supersession, version, or jurisdiction checks
- same-lineage sources being counted as independent support
- material counterevidence not yet searched
- possible synthesis overreach
- a new citation, dataset, docket, standard, archive, repository, author,
  regulator, method, version, or native-language term that could change a claim

Every follow-up lead must be marked in the single record as followed, duplicate,
dead end, blocked, low quality, out of scope, or used to downgrade affected
claims. If a follow-up lane still leaves a material gap, downgrade the affected
claim, mark it `insufficient`, or record it as unresolved. Do not hide
unresolved gaps inside confident synthesis.

Run expansion as a frontier queue in waves. After integrating a wave, scan the
record for unresolved lead, source-family, currentness, contradiction,
provenance, and lineage gaps. Rank remaining frontier items by decision impact,
error risk, source-family uniqueness, proximity to primary evidence, and
ability to clear coverage debt. Launch the next wave only for leads that can
still change an important claim, close a coverage gate, or correct provenance.
Stop expansion only when a full wave raises no new high-value leads, or when
remaining leads are duplicate lineage, blocked, out of scope, low quality, or
unable to affect the synthesis and the affected confidence labels reflect that.

## Verification Lanes

Run verification with fresh subagents after the research lanes have been
integrated into provisional artifacts. Verification subagents should not inherit
research subagent context or defend a research lane's conclusion.

Give claim, source, currentness, contradiction, and record auditors the research
question, claim inventory, source table, search notes, inspected source bodies
or bounded excerpts with evidence locations, and authorized source paths/URLs
they may reopen. Do not give these auditors the draft synthesis unless their
lane requires it.

For sensitive enterprise sources, prefer bounded excerpts, source metadata, and
redacted claim/source rows over full source bodies unless the verification lane
cannot function without the full material. Record the minimization choice in
the verification lane notes.

Give the draft synthesis only to the synthesis-overreach audit, plus the same
source artifacts needed to test whether the synthesis overstates the evidence.
Verification findings must cite inspected source locations, not just source IDs.
Verification subagents follow the same write boundary as research subagents:
they return audit findings only and do not edit the research record or any
filesystem path.

Use independent verification lanes that attack different failure modes:

- claim verification audit: checks whether each important claim is directly
  supported and correctly classified
- source audit: checks source quality, inspected-body status, evidence
  locations, snippets/AI-only leakage, and source lineage
- currentness audit: checks latest-update, supersession, changelog, docket,
  advisory, status-page, and as-of claims
- contradiction and gap audit: looks for unresolved conflicts, missing source
  families, failed searches, and counterevidence
- source-lineage audit: checks whether apparently independent support depends
  on the same upstream source, dataset, press release, or citation chain
- synthesis-overreach audit: checks whether the draft conclusion says more than
  the sources support
- frontier queue convergence audit: checks whether material leads from research
  lanes, source bodies, citations, datasets, repositories, issues, archives,
  counterclaims, and blocked primary sources were followed, closed, blocked
  with confidence effect, or shown unable to change important claims
- record and coverage audit: checks whether the single research record
  satisfies the `research-record-template.md` contract, including `## Sources`,
  `## Search Matrix`, `## Wave Log`, `## Claim Ledger`,
  `## Verification Notes`, and `## Coverage Gates`
- enterprise governance audit: checks intake, access basis, sensitivity,
  minimum-necessary handling, decision-use status, owner-review triggers, and
  enterprise QA gates when applicable

Baseline verification always requires `claim verification audit`, `source
audit`, `contradiction and gap audit`, `source-lineage audit`, and
`frontier queue convergence audit`. Add `currentness audit` for
current-dependent claims, `synthesis-overreach audit` whenever a draft
conclusion exists, and `record and coverage audit` before claiming the research
record is complete. Record skipped lanes as
`not applicable` with a reason. Add `enterprise governance audit` for
organizational, internal, sensitive, regulated, strategic, procurement,
diligence, risk, executive, or decision-support research.

Add a verified-claim audit for high-risk non-code claims. It checks primary or
governing source backing, independent source lineages, counter-search,
temporal evidence, method/data quality, source lineage, and transferability.

For non-trivial research, cover these lanes through subagents or direct
main-agent passes before final synthesis:

- source discovery
- primary-source or claim verification
- counterevidence
- currentness
- source lineage
- synthesis-overreach audit

Add a method/data audit when the research involves methods, data, statistics,
experiments, surveys, benchmarks, or causal claims.

## Verification Pass Criteria

- claim verification passes only when every important claim has direct inspected
  support, is explicitly downgraded, or is labeled `insufficient`
- source audit passes only when every used source has inspected-body or
  retrieved-record status, lineage, claim provenance label, evidence location,
  and source-quality status
- currentness audit passes only when every current-dependent claim has a
  latest-update or supersession check, or is labeled `insufficient`
- contradiction and gap audit passes only when material conflicts, missing
  source families, and counterevidence searches are resolved or recorded as
  unresolved gaps with affected claims
- source-lineage audit passes only when duplicated source lineages have been
  collapsed and independence claims are justified
- frontier queue convergence audit passes only when the latest EXPAND or gap
  cycle produced no new high-value leads, or every remaining material frontier
  item is closed, blocked, duplicate lineage, out of scope, low quality, unable
  to change the answer, or tied to confidence downgrade
- synthesis-overreach audit passes only when the draft conclusion does not
  exceed the inspected evidence and confidence labels
- record and coverage audit passes only when the single research record has the
  required sections, source table, search matrix, wave log, claim ledger,
  evidence ledger, coverage gates, and stop-rule reasoning, or explicitly
  states why the record could not be written under current constraints
- enterprise governance audit passes only when access basis, sensitivity,
  minimum-necessary handling, decision-use status, and owner-review triggers are
  recorded or explicitly not applicable

If a verification lane fails or finds a material gap, run a targeted gap pass
and then re-run the failed verification lane. If the lane still fails on a
material claim, label the affected claim `low` or `insufficient`. Firm synthesis
is blocked for unresolved high-stakes or current-dependent claims unless the
final answer explicitly frames the issue as unresolved.
