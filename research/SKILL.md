---
name: research
description: Use only when the user explicitly asks for research.
---

# Research

Use evidence-led research when the user explicitly asks for research-grade
source discovery, verification, and synthesis. Research means full investigation. Once triggered, do not simplify it into a quick lookup or proportional light path.

Keep the workflow deep and the record lean: capture the evidence trail, not a
large report scaffold.

## When To Use

Use this skill when the user explicitly says `research`, asks to create a
research record, or asks for diligence, market scan, policy/regulatory review,
literature review, scholarly search, evidence review, competitive landscape,
vendor comparison, investment or security diligence, OSINT/source verification,
or decision-support research.

Do not trigger on investigation, explore, analyze, compare, look into, or
similar wording by itself unless the user asks for research-grade source
discovery or a durable research record.

Do not use this for simple lookup, quick web search, latest-status check, or
direct fact verification unless the user explicitly asks for research. Known-item paper lookup is normal lookup unless the user explicitly asks for
research.

## Record Contract

One explicit research request maps to one research record file. The main agent is the only writer: it chooses or creates
`gigantum-humeris/research/<NNN-topic>.md` and integrates every research or
verification lane into that single file. Subagents return lane notes, source
notes, claim checks, and verification findings only; they must not create,
modify, delete, or move research files or directories.

Do not create multiple sibling research records for one request. Do not create
topic folders, `brief.md`, `sources.md`, or `notes.md`.
Do not use the global Markdown wiki as a substitute for project research
records.

## Required References

Load only what the task needs:

- Always: `references/research-process.md`,
  `references/evidence-needs-core.md`
- Before writing records or lane instructions:
  `references/research-record-template.md`
- When using subagents or sequential lane fallback:
  `references/subagent-orchestration.md`
- For high-stakes, current, conflicting, provenance-sensitive, translated, or
  harmful claims: `references/source-verification.md`
- For specialized search mechanics or domain coverage:
  `references/query-and-source-patterns.md` and the relevant domain reference

## Core Workflow

1. Frame the question, scope, currentness requirement, intended decision, and
   evidence needs.
2. Create or choose the numbered research record file.
3. Use `research-process.md` for scout, target, snowball, and gap-pass work.
4. Inspect source bodies or retrieved connector records. Snippets, AI summaries,
   and generated overviews are leads, not evidence.
5. Integrate sources into a draft answer and source table.
6. Verify important claims for support, source quality, currentness,
   counterevidence, gaps, and synthesis overreach.
7. Launch follow-up lanes or run direct checks when support is weak, sources
   share lineage, currentness is unresolved, or counterevidence is missing.
8. Maintain an evidence ledger for important claims and decide whether each
   claim is used, downgraded, excluded, or unresolved.
9. Synthesize only after important claims are supported, downgraded, or labeled
   `insufficient`.
10. Write the final evidence trail using `research-record-template.md`.

## Output Contract

Before doing research, give the user a concise visible framing and record the
same framing in the single research record:

- research question and intended decision/output
- scope boundaries and assumptions
- evidence needs and preferred source families
- search plan, including scout, target, snowball, and gap-pass paths
- currentness requirement
- privacy, confidentiality, and access boundaries when relevant
- record target under `gigantum-humeris/research/<NNN-topic>.md`

Before the final response, confirm:

- what was checked and what was not checked, with reasons
- strongest evidence and source-family coverage
- counterevidence, uncertainty, and remaining gaps
- verification lanes completed, blocked, or downgraded
- why the stop rule was reached
- confidence by important claim
- research record path, or why no record was written

## Non-Negotiable Checks

- Important claims include every factual claim used in the final answer, every
  claim that can affect the user's decision, every current, high-stakes,
  comparative, quantitative, or causal claim, and every claim attached to a
  citation.
- A used source must have an inspected body or retrieved record.
- Current-dependent claims require a latest-update or supersession check, or
  they must be labeled `insufficient`.
- Important claims require an evidence ledger decision: use, downgrade,
  exclude, or unresolved.
- Non-trivial research requires source discovery, primary-source or claim
  verification, counterevidence, currentness, and synthesis-overreach coverage.
- Research involving methods, data, statistics, experiments, surveys,
  benchmarks, or causal claims requires a method/data audit lane.
- Apply the canonical stop rule in `research-process.md`, plus any loaded
  domain-specific stop gates.
- Do not use subagent conclusions, search snippets, generated summaries, or
  uninspected abstracts as final evidence. Treat them as leads until an
  inspected source body or retrieved record supports the claim.
- Do not describe a result as professional-grade, decision-ready, externally
  reviewable, or research-firm-grade unless the relevant quality gates pass or
  the answer explicitly states which gates failed and why.
