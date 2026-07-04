# Ingest Workflow

Use this when the user asks to process `_ingest/`, import sources, add files to the wiki, or run llm-wiki ingest.

## Steps

1. Locate the vault root and `_ingest/`.
2. List ingest files. Process Markdown and plain text first.
3. Inventory configured wiki definitions and candidate wiki folders.
4. For each source:
   - read the full source
   - read candidate wiki definition/index/log
   - read existing pages likely related by title, aliases, headings, backlinks, or keyword overlap
   - check whether the source is already referenced in page `sources`, `log.md`, or a manifest
   - classify the source
5. Choose the action:
   - update existing page when the source adds detail to a known concept/entity/decision
   - create new page when it introduces a distinct concept/entity/decision
   - create new wiki when it clearly does not belong in existing wikis
   - stop for user choice when several wikis fit and no active wiki is clearly intended
6. Move the original source into `<wiki>/raws/`.
7. Apply wiki page edits or creates.
8. Update `index.md` and `log.md`.
9. Run a small verification pass on moved and edited paths.
10. Report results.

## Classification Signals

Use all of these, not only filename similarity:

- wiki definition name and `wiki_id`
- index links and section headings
- existing concepts/entities/decisions
- raw source topics
- recurring vocabulary
- user’s active file or explicit target wiki
- prior log entries
- existing page `sources`
- source IDs, URLs, or quoted titles already present in the wiki

## Raw Move Rules

- Move, do not copy.
- Preserve original filename where possible.
- If the target exists, use a collision-safe suffix such as `source-2.md`.
- After moving, no duplicate should remain in `_ingest/`.
- Never move unsupported binary files unless the user asks.
- Never move into a folder that is not a wiki root. Confirm `Wiki.md` or the user's configured wiki definition first.

## Page Update Rules

- Add the moved raw path to `sources`.
- Add source-grounded claims with direct source references.
- Mark synthesis as inferred when the raw source does not state it directly.
- Mark conflicts as ambiguous/disputed instead of flattening them into one conclusion.
- Prefer append or targeted merge over wholesale rewrite.

## Index and Log Rules

- `index.md` is content-oriented: links to pages with one-line summaries.
- `log.md` is chronological: ingests, queries saved as pages, lint passes, repairs, and promotions.
- Use consistent headings such as `## [2026-06-19] ingest | source.md` when editing manually.

## Output Summary

Report:

- source path before and after
- target wiki
- pages edited
- pages created
- pages skipped
- conflicts or user choices needed
