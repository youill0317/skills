# Agent Prompts

## Full Ingest Prompt

```text
Use $llm-wiki.

Process the vault-root _ingest/ folder into the appropriate llm-wiki folders.

Requirements:
- Treat the current Obsidian vault as the wiki workspace.
- Discover all existing llm-wiki folders and definition notes.
- Read existing wiki pages before deciding whether to create or update pages.
- Check existing sources/log/manifest so already-processed sources are not duplicated.
- Move each ingested source into the selected wiki's raws/ folder. Do not copy and leave duplicates.
- Weave new information into existing pages when appropriate.
- Create new pages only when the idea is not already owned by an existing page.
- Create a new wiki only when no existing wiki fits.
- Preserve provenance. New claims must cite raw source paths or be marked inferred/ambiguous.
- Preserve stable pages; if a source conflicts with stable content, stop and report the conflict.
- Update index.md and log.md.
- Summarize moved raws, edited pages, created pages, and unresolved choices.
```

## Classification-Only Prompt

```text
Use $llm-wiki.

Inspect _ingest/ and all llm-wiki folders. Classify each ingest source into:
- update-existing-page
- create-new-page
- create-new-wiki
- needs-user-choice

Do not move or edit files. Return a concise table with source, target wiki, target page/action, and reason.
```

## Query Prompt

```text
Use $llm-wiki.

Answer this question from the llm-wiki. Read index.md and recent log.md first, then only the relevant pages and raw sources. Cite wiki page paths or raw source paths. If the wiki does not contain enough evidence, say what is missing. Do not edit files unless I ask you to save the answer.
```

## Repair Prompt

```text
Use $llm-wiki.

Audit the llm-wiki structure in this vault. Find stale definition paths, missing raws referenced by pages, broken wikilinks, orphan pages, duplicate concept/entity pages, stale index/log entries, weak provenance, disputed claims, and _ingest files that were not processed. Do not edit files until you report proposed fixes grouped by severity.
```
