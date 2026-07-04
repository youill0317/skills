---
name: llm-wiki
description: Maintain an Obsidian llm-wiki inside a vault. Use when the user asks to process _ingest/, classify sources into multiple wiki folders, create or update wiki notes, move raw sources into raws/, answer questions from the wiki, run wiki lint/audit/repair, promote or crystallize draft knowledge, update index/log, or run llm-wiki work through Smart Composer Wiki Chat or Agent Chat.
---

# LLM Wiki

Use this skill to maintain a persistent, compounding Obsidian wiki from raw sources. The workflow can run through Agent Chat, Smart Composer Wiki Chat, or explicit wiki commands. Do not bypass the visible approval surface for file moves or edits.

## Core Contract

- Treat the Obsidian vault itself as the wiki workspace.
- Support multiple independent wiki folders under the vault root.
- Use a single vault-root `_ingest/` folder as the intake queue.
- Move ingested source files into the selected wiki's `raws/`; do not copy and leave duplicates in `_ingest/`.
- Read the wiki definition, index, log, and likely related pages before deciding where a source belongs.
- Weave new source material into the existing wiki: update relevant pages when appropriate, create new pages when needed, and create a new wiki only when no existing wiki fits.
- Keep frontmatter limited to the repo's operational wiki fields.
- Preserve provenance. Every durable claim should trace to a raw source, an existing wiki page, or be marked as inferred/ambiguous in the body.
- Never silently overwrite stable knowledge. If a source conflicts with reviewed/stable content, preserve the conflict and make the edit explicit.

## Operations

- `setup/discover`: find definition notes and wiki folders; create a new wiki only when no existing wiki fits.
- `ingest`: classify `_ingest/` files, move raws, update/create pages, and update index/log.
- `query`: answer from the wiki using index-first, local-first search; offer to file valuable answers back into the wiki.
- `lint/audit`: check structure, provenance, broken links, orphan pages, missing raws, duplicates, stale index/log, and unprocessed `_ingest/`.
- `repair`: propose fixes first; apply only clear, low-risk structural repairs.
- `crystallize/promote`: consolidate draft or repeated knowledge into a reviewed/stable page while preserving sources and conflicts.
- `status`: summarize active wikis, pending ingest files, recent log entries, and lint findings.

## Success Criteria

For ingest, finish only when:

- every processed source was moved from `_ingest/` into exactly one wiki `raws/` path
- every created or edited page lists the raw source path in `sources`
- index and log reflect the change
- ambiguous wiki choices, conflicts, and skipped files are reported
- changed paths were verified by reading or listing them

For query, finish only when:

- the answer cites wiki pages or raw source paths
- the answer says when evidence is missing or ambiguous
- any new output page is created only after the user asks or the value is clearly durable

For lint/audit, finish only when findings are grouped by severity and include exact paths.

## Page Rules

Use this minimal frontmatter shape for compiled wiki pages in this repo:

```yaml
---
wiki_id: research
page_type: concept
status: draft
sources:
  - research/raws/source.md
---
```

Allowed `page_type` values: `concept`, `entity`, `decision`, `output`, `index`, `log`.

Allowed `status` values: `draft`, `reviewed`, `stable`.

Use `llm_wiki: true` on wiki definition notes, not on compiled concept/entity/decision pages for this repo's strict schema.

When updating an existing page, preserve its frontmatter unless it is missing required wiki fields. Add new raw source paths to `sources`. Put inferred, ambiguous, disputed, or superseded state in the body unless the user's schema explicitly supports more fields.

## Resource Loading

Load only the reference needed for the current task:

- For structure and frontmatter rules, read `references/wiki-structure.md`.
- For `_ingest/` processing, read `references/ingest-workflow.md`.
- For wiki questions and file-back answers, read `references/query-workflow.md`.
- For lint, audit, repair, and health checks, read `references/lint-workflow.md`.
- For existing-page updates and conflict handling, read `references/weaving-rules.md`.
- For provenance and source-grounding rules, read `references/provenance.md`.
- For write safety and approval expectations, read `references/safety.md`.
- For reusable Agent Chat prompts, read `references/agent-prompts.md`.

Useful scripts:

- `scripts/render-ingest-prompt.sh [vault_path] [ingest_dir]` prints a ready-to-paste Agent Chat prompt.
- `scripts/list-wiki-candidates.sh [vault_path]` lists likely llm-wiki definition notes and folders.
- `scripts/move-raw.sh <source_file> <wiki_dir>` moves one source into `<wiki_dir>/raws/` with a collision-safe filename.
- `scripts/scaffold-wiki.sh <vault_path> <wiki_folder> <wiki_id> [display_name]` creates a standard root-level wiki folder.

## Default Agent Behavior

For a request like “`_ingest 처리해서 위키에 반영해줘`”, run ingest end-to-end. Do not turn it into a general explanation.

For a request like “이 위키에 대해 물어봐”, answer from the vault/wiki context without changing files unless the user asks to save the answer.

For a request like “위키 점검해줘”, run lint/audit first and report proposed fixes before editing.
