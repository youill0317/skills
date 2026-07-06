# Query And Source Patterns

Use this when building search lanes or query seeds.

## Query Portfolio

Build diversified query families instead of repeating near-duplicates:

- official or governing source
- latest/current/supersession
- counterevidence, criticism, limitation, failure
- scholarly or methods
- dataset, statistics, appendix, codebook
- provenance, original source, archive, author, funding
- local-language and jurisdiction-specific terms
- repository, issue, release, standard, advisory
- comparison, pricing, benchmark, procurement, review

Use `scripts/query_matrix.py` as a seed generator when helpful:

```bash
python <skill-dir>/scripts/query_matrix.py --topic "<topic>"
python <skill-dir>/scripts/query_matrix.py --topic "<topic>" --format batches --batch-size <tool-limit>
```

The output is not a required template. Copy only useful rows into the record.

## Search Moves

- Combine exact names with aliases, acronyms, translations, versions, and false
  positive exclusions.
- Use source-family operators such as `site:`, `filetype:pdf`, `intitle:`,
  official domains, repositories, archives, and date filters when available.
- Search beyond the first phrasing that works.
- After opening a strong source, search for its references, title, author,
  organization, dataset, standard number, docket, release, or named claims.
- For absence claims, record the boundary searched rather than claiming global
  non-existence.
