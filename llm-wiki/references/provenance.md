# Provenance

Provenance is the difference between a useful llm-wiki and plausible generated notes.

## Source Rules

- Every compiled page lists raw source paths in `sources`.
- Every new durable claim should be near a source reference in the body.
- If a claim combines multiple sources, list each source.
- If a statement is inferred, mark it as inferred in prose.
- If sources disagree, keep both claims and mark the section disputed or ambiguous.

## Suggested Body Sections

```text
## Source-Grounded Claims

- Claim. Source: [[Research/raws/source.md]]

## Inferred

- Inference. Basis: [[Research/raws/source-a.md]], [[Research/raws/source-b.md]]

## Disputed

- [[Research/raws/a.md]] says X.
- [[Research/raws/b.md]] says Y.
- Status: needs review.
```

## Stable Source Identity

When a source has a URL, DOI, title, or stable ID, preserve it in the raw note body. Do not rely only on filenames, because filenames can change.

If a wiki already uses stable source IDs, follow that convention instead of inventing a new one.
