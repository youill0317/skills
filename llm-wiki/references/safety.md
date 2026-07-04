# Safety

The visible approval surface is the safety boundary for file moves, edits, and shell commands. In Smart Composer, Agent Chat tool approvals and internal wiki apply/write controls may be separate surfaces; do not bypass either one.

## Hard Rules

- Stay inside the vault unless the user explicitly provides another path.
- Never delete source material during ingest; move it into `raws/`.
- Never leave duplicate ingested files in `_ingest/`.
- Never overwrite an existing target file. Pick a collision-safe path or ask.
- Never fabricate sources. Every new claim should trace to a raw file or existing wiki page.
- Never add broad frontmatter or model metadata unless the user asks.
- Never auto-resolve disputed or superseded knowledge by deleting the losing claim.

## Before Editing

For small clear ingest batches, proceed through tool calls and let the approval UI handle consent.

For risky operations, first state the plan:

- files to move
- pages to edit
- pages to create
- conflicts
- user choices needed

Risky operations include stable page rewrites, deletion, mass rename, cross-vault writes, or ambiguous wiki selection.

Use dry-run style reporting for:

- mass ingest
- lint fixes across many pages
- graph/export generation
- archive/rebuild
- edits to `status: reviewed` or `status: stable` pages

## After Editing

Verify by reading the changed paths or listing the affected folders. Report a compact ledger:

```text
Moved:
- _ingest/source.md -> Research/raws/source.md

Edited:
- Research/concepts/agent-chat.md

Created:
- Research/decisions/agent-chat-for-ingest.md

Needs review:
- _ingest/ambiguous.md: could fit Research or Product
```
