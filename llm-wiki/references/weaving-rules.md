# Weaving Rules

Weaving means integrating new sources into existing wiki knowledge rather than blindly generating isolated pages.

## Existing Page Update

Update an existing page when:

- the page already owns the same concept/entity/decision
- the new source adds examples, constraints, caveats, or evidence
- the target page is draft/reviewed and the new source is compatible

When updating:

- add the raw path to `sources`
- preserve existing headings and stable wording where possible
- append a sourced section instead of rewriting the page wholesale
- add links to related pages
- keep page status unchanged unless the user asks
- grep or search for the same source path, title, URL, and key claim before writing to avoid duplicates

## New Page Creation

Create a new page when:

- no existing page clearly owns the idea
- merging would make an existing page cover two concepts
- the source introduces a durable entity, decision, or output

Use concise filenames:

```text
Research/concepts/context-window-management.md
Research/entities/smart-composer.md
Research/decisions/agent-chat-for-ingest.md
```

## Stable Content

For `status: stable` pages:

- do not rewrite the core claim silently
- add a clearly sourced “New evidence” or “Related note” section when compatible
- if the source contradicts stable content, create a draft conflict note or ask the user

For `status: reviewed` pages:

- prefer append-only sourced sections
- keep the reviewed status unchanged
- do not demote or promote status without user intent

## Conflict Handling

Stop for user choice when:

- two or more wikis are equally plausible
- a source conflicts with a stable page
- a move would overwrite an existing raw
- a requested edit would delete or rewrite substantial existing knowledge

Do not ask when the operation is clear and reversible through normal file history.

## Crystallize or Promote

Use crystallize/promote when several draft pages or repeated query outputs have converged into durable knowledge.

Before promoting:

- read every source listed by the candidate pages
- preserve all source paths
- record superseded pages in the body or log
- keep unresolved contradictions in a “Disputed” section
- update index/log after the promotion
