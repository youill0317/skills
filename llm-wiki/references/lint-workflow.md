# Lint Workflow

Use this when the user asks to audit, repair, health-check, lint, clean, or validate a wiki.

## Checks

Run the checks that fit the request and current wiki structure:

- definition note exists and has valid operational fields
- `raws/`, `concepts/`, `entities/`, `decisions/`, `outputs/`, `index.md`, and `log.md` exist
- compiled pages have valid frontmatter for this repo: `wiki_id`, `page_type`, `status`, `sources`
- every `sources` path exists
- `_ingest/` does not contain already-processed duplicates
- `index.md` links to created pages
- `log.md` has recent ingest/query/lint entries
- wikilinks resolve to existing notes where practical
- obvious duplicate concept/entity pages are reported
- stable/reviewed pages are not silently contradicted by newer pages
- quoted or strongly factual claims are grounded in sources

## Severity

- `error`: broken source path, invalid definition, destructive conflict, or missing required page.
- `warning`: stale index/log, likely duplicate, orphan page, unprocessed ingest file, or disputed claim.
- `info`: optional improvement, candidate link, missing summary, or suggested source to collect.

## Repair

Report proposed fixes before editing when more than one file is affected.

Safe auto-fixes:

- add missing index links
- append log entries
- add missing source paths when the source is obvious
- create missing standard folders

Ask before:

- merging duplicate pages
- rewriting stable/reviewed pages
- deleting or archiving pages
- resolving disputed claims
