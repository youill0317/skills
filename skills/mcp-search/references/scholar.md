# Semantic Scholar Tools

## Covered Tools

- `scholar_paper_search`
- `scholar_paper_search_bulk`
- `scholar_paper_search_match`
- `scholar_paper_details`
- `scholar_paper_batch`
- `scholar_paper_authors`
- `scholar_paper_citations`
- `scholar_paper_references`
- `scholar_author_search`
- `scholar_author_details`
- `scholar_author_papers`
- `scholar_author_batch`
- `scholar_citation_graph`
- `scholar_recommend_single`
- `scholar_recommend_list`

## Common Patterns

- Use `paper_search` for ordinary paper discovery.
- Use `paper_search_match` when you likely know the target paper already.
- Use `paper_details` after you have a stable identifier.
- Use citation, reference, and recommendation tools only after you have a stable seed paper.
- Use author tools for author-centered questions.

## Input Shapes

### `scholar_paper_search`

```json
{
  "query": "model context protocol",
  "limit": 10,
  "offset": 0,
  "year": "2024-2026",
  "fields_of_study": "Computer Science"
}
```

Optional filter fields:

- `publication_types`
- `open_access_pdf`
- `min_citation_count`
- `publication_date_or_year`
- `year`
- `venue`
- `fields_of_study`

### `scholar_paper_search_bulk`

```json
{
  "query": "tool-using language models",
  "token": "opaque-cursor-token",
  "sort": "citationCount:desc"
}
```

### `scholar_paper_search_match`

```json
{
  "query": "Attention Is All You Need"
}
```

### `scholar_paper_details`

```json
{
  "paper_id": "DOI:10.48550/arXiv.1706.03762"
}
```

Accepted `paper_id` formats include Semantic Scholar ID, DOI, arXiv, PubMed, CorpusId, or URL.

### `scholar_paper_citations`

```json
{
  "paper_id": "CorpusId:11903278",
  "limit": 25,
  "publication_date_or_year": "2023:"
}
```

### `scholar_author_search`

```json
{
  "query": "Christopher Manning",
  "limit": 5
}
```

### `scholar_citation_graph`

```json
{
  "paper_id": "DOI:10.48550/arXiv.1706.03762",
  "direction": "citations",
  "limit": 20
}
```

### `scholar_recommend_list`

```json
{
  "positive_paper_ids": [
    "DOI:10.48550/arXiv.1706.03762"
  ],
  "negative_paper_ids": [],
  "limit": 20
}
```

## Output Expectations

- Search endpoints return paged paper lists.
- Detail endpoints return one metadata record.
- Graph and recommendation endpoints return seed-centered expansions.
