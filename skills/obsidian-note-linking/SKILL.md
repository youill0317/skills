---
name: Obsidian Note Linking
description: Suggest related Obsidian note connections for the currently open note by exploring vault structure, searching relevant notes, and proposing consistent connection patterns (for example `[[wikilinks]]`, heading/block references, embeds, and tags) with concise rationale.
category: task
---

# Mission

Improve note connectivity in Obsidian by proposing high-signal, consistent connection patterns grounded in actual vault evidence.

## Category

`task`

## Use When

- The user wants to strengthen a current note with related note connections.
- The user asks which existing notes should be connected and how.
- The user wants tag suggestions aligned with vault conventions.
- The user wants practical next-step edits for Obsidian notes.

## Scope

1. Discover candidate notes from the vault before proposing connections.
2. Rank candidates by direct relevance to the open note.
3. Suggest connection patterns (for example `[[wikilinks]]`, `[[Note#Heading]]`, `![[Note]]`, `[[Note#^block-id]]`, and tags).
4. Keep suggestions actionable and easy to paste into the note.
5. Avoid fabricating note names, sections, or metadata.

## Core Workflow

1. Confirm target note path/title and the note's core topic.
2. Extract key concepts from the target note (entities, themes, projects, timeframes).
3. Search the vault for candidate notes using concept keywords and aliases.
4. Read only narrow sections needed to validate relevance and choose the best connection type.
5. Score candidates by overlap, complementarity, and backlink value.
6. Choose one primary connection style for the response unless the user asks for mixed styles.
7. Propose a concise connection plan:
   - recommended connection expressions
   - suggested insertion context (sentence/section)
   - optional tag additions or normalization
8. Return only verifiable suggestions tied to discovered notes.

## Output Standard

Return a compact recommendation bundle with:

1. **Connection style** selected for this response and why.
2. **Top candidates (3-10)** with one-line why.
3. **Insertion suggestions** for where each connection best fits.
4. **Tag suggestions** split into keep/add/merge.
5. **Paste-ready snippet** the user can drop into the current note.

Quality rules:

- Prefer specific notes over broad index pages unless index is clearly useful.
- Prefer connections that add context, evidence, dependency, or next action.
- Do not recommend connections without reading enough to validate relevance.
- Keep each rationale short and concrete.
- Keep connection notation consistent in one response (unless user requested a comparison).

## Integration

1. Use with `obsidian-mcp` for tool-family selection and safe discovery/read flow.
2. Hand off refined notes to `document-summary` when user wants merged synthesis.
3. Hand off to `planning` when connections imply project next steps or action tracking.

## Resource Loading

- Load `references/link-scoring-rubric.md` for candidate ranking and quality gates.
- Load `references/output-template.md` for response structure and paste-ready formatting.
