# Query Workflow

Use this when the user asks questions about a wiki, asks what the wiki knows, compares topics, or wants an answer grounded in wiki content.

## Local-First Search

1. Identify the target wiki from the user request, active wiki, or relevant index.
2. Read `Wiki.md`, `index.md`, and recent `log.md` entries first.
3. Search titles, headings, `sources`, and page summaries with `rg`.
4. Read only the likely concept/entity/decision pages.
5. If the vault is large and `qmd` is available, use it as an optional search accelerator; otherwise rely on index and `rg`.

## Answer Rules

- Cite wiki page paths or raw source paths.
- Distinguish sourced claims from inference.
- Say when evidence is missing, stale, or disputed.
- Do not edit files for a normal query.

## File-Back Rule

Offer to save the answer back into the wiki when it is durable:

- comparison table
- synthesis
- decision rationale
- research output
- FAQ entry

If saving, create an `output` or suitable concept/decision page, add source paths, and update index/log.
