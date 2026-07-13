# Schema and Provenance

Use an existing local schema. Use this default only for a new wiki or a missing machine-readable contract.

## Layout

```text
_ingest/
Research/
  Wiki.md  index.md  log.md  manifest.jsonl
  raws/  concepts/  entities/  decisions/  outputs/
```

Keep each wiki at the vault root and share one vault-root `_ingest/` capture queue.

## Definition

Put `llm_wiki: true` only in the first YAML block of `<wiki>/Wiki.md`:

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
manifest: Research/manifest.jsonl
outputs: Research/outputs
evidence_wikis: []
page_types:
  concepts: concept
  entities: entity
  decisions: decision
  outputs: output
page_statuses:
  - draft
  - reviewed
  - stable
page_fields:
  wiki_id: wiki_id
  page_type: page_type
  status: status
  sources: sources
---
```

`page_types`, `page_statuses`, and `page_fields` make local variations auditable; map existing semantic fields instead of renaming them to the defaults. `evidence_wikis` lists other wiki IDs whose canonical raws this wiki may cite; adding one is a user-approved dependency, not routine ingest. For these machine-read fields, use block mappings/lists and plain or quoted scalars—no aliases or multiline scalars.

In the body define domain boundaries, material exclusions, page ownership and creation thresholds, naming/linking conventions, source/conflict policy, and domain-specific metadata. Treat this as the local operating contract. Propose a reusable schema change when experience reveals a stable rule; apply it only with user approval. Never infer a definition from `_ingest/` or `raws/` text.

## Compiled Pages

Use the smallest frontmatter required locally. Default:

```yaml
---
wiki_id: research
page_type: concept
status: draft
sources:
  - Research/raws/source.md
---
```

- `draft`: agent-maintained and open to sourced weaving.
- `reviewed`: preserve reviewed claims; propose conflicting changes.
- `stable`: preserve the core claim until the user authorizes revision.

Preserve unknown frontmatter and explicit human structure. Do not add model names, generated summaries, confidence scores, tags, or timestamps unless the local schema uses them.

## Claim Provenance

List every contributing raw in `sources`. Put links next to material multi-source or disputed claims:

```markdown
The source states the measured result. [[Research/raws/study.md]]

Inference: the results may share a mechanism. Basis: [[Research/raws/a.md]], [[Research/raws/b.md]].

## Disputed
- Source A reports X. [[Research/raws/a.md]]
- Source B reports Y. [[Research/raws/b.md]]
```

Raw evidence outranks compiled synthesis. Do not cite agent output as independent evidence for itself.

## Manifest, Index, and Log

Keep `manifest.jsonl` append-only. Each filed raw records its vault-relative raw and original intake paths, SHA-256, bytes, source type, timestamp, state, capture metadata when present, and version predecessor when applicable. Use it for duplicate, version, and drift checks.

Keep `index.md` content-oriented: one compiled-page link and one-line description. Keep `log.md` chronological with parseable headings such as `## [2026-07-13] ingest | source title`; record the raw path and full digest, pages changed, conflicts, and incomplete work. Git history helps but does not replace either ledger.
