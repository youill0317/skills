# arXiv And Usage Tools

## Covered Tools

- `arxiv_search`
- `check_usage`

## `arxiv_search`

Use for arXiv-native preprint search when you want raw arXiv coverage rather than citation graph features.

### Input Shape

```json
{
  "query": "model context protocol",
  "category": "cs.AI",
  "start": 0,
  "max_results": 10,
  "sort_by": "submittedDate",
  "sort_order": "descending"
}
```

Accepted query forms:

- `query`
- `raw_query`
- `id_list`

At least one of those must be provided.

## `check_usage`

Use when the blocker is provider availability or quota rather than retrieval itself.

### Input Shape

```json
{
  "service": "all"
}
```

Allowed `service` values:

- `brave`
- `tavily`
- `exa`
- `semantic_scholar`
- `arxiv`
- `all`

## Output Expectations

- `arxiv_search` returns arXiv entry records.
- `check_usage` returns availability or usage information by provider.
