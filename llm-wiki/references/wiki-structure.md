# Wiki Structure

## Vault Layout

The vault may contain several wiki folders at the root:

```text
_ingest/
Research/
  Wiki.md
  index.md
  log.md
  raws/
  concepts/
  entities/
  decisions/
  outputs/
Product/
  Wiki.md
  index.md
  log.md
  raws/
  concepts/
  entities/
  decisions/
  outputs/
```

Do not create a global parent folder for all wikis unless the user explicitly asks. A wiki is a folder under the vault root.

## Definition Note

Prefer a `Wiki.md` definition note with:

```yaml
---
llm_wiki: true
wiki_id: research
name: Research
root: Research
raws: Research/raws
files:
  concepts: Research/concepts
  entities: Research/entities
  decisions: Research/decisions
index: Research/index.md
log: Research/log.md
outputs: Research/outputs
---
```

In Smart Composer, configured definition note paths are authoritative. If you infer a wiki from folder shape, treat it as a candidate and say that a definition note should be created or configured.

## Page Frontmatter

Compiled concept/entity/decision pages in this repo use only required operational fields:

```yaml
---
wiki_id: research
page_type: concept
status: draft
sources:
  - Research/raws/source.md
---
```

Avoid noisy frontmatter such as arbitrary tags, confidence, timestamps, model names, embeddings metadata, or long summaries.

Put uncertainty in the body, not frontmatter, unless the user's wiki schema explicitly supports more fields:

```text
## Source-Grounded Claims

- Claim text. Source: [[Research/raws/source.md]]

## Inferred

- Inference text. Marked inferred because no source states it directly.

## Ambiguous or Disputed

- Source A says X; source B says Y. Needs review.
```

## Page Types

- `concept`: reusable idea, mechanism, pattern, principle.
- `entity`: person, organization, project, product, system, library.
- `decision`: durable choice, tradeoff, policy, ADR-like note.
- `output`: generated deliverable or report.
- `index`: navigational page.
- `log`: chronological update record.

## Manifest and Delta

If a wiki has `.manifest.json`, `manifest.md`, or a log section that tracks ingested raw paths, use it to avoid duplicate ingest. If no manifest exists, use `log.md`, `sources` frontmatter, and `raws/` filenames as the delta source.

Do not re-ingest a raw source when its path is already present in compiled page `sources` unless the user asks to reprocess it.
