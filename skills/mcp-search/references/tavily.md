# Tavily Tools

## Covered Tools

- `tavily_search`
- `tavily_extract`
- `tavily_crawl`
- `tavily_map`
- `tavily_image_search`

## When To Use

- Use `tavily_search` for web discovery with domain and recency filters.
- Use `tavily_extract` when you already know which URLs deserve close reading.
- Use `tavily_crawl` when one starting page is not enough and you need multi-page extraction.
- Use `tavily_map` when you need site structure without extracting page bodies.
- Use `tavily_image_search` for image search with the same domain and recency controls.

## Input Shapes

### `tavily_search`

```json
{
  "query": "openai api batching guide",
  "search_depth": "advanced",
  "max_results": 8,
  "include_domains": ["platform.openai.com"],
  "topic": "general",
  "time_range": "month"
}
```

Key parameters:

- `query`: required string
- `search_depth`: optional enum `basic | advanced`
- `include_raw_content`: optional boolean
- `max_results`: optional integer, `1-20`
- `include_domains`, `exclude_domains`: optional string arrays
- `topic`: optional enum `general | news`
- `days`: optional integer, `1-365`
- `time_range`: optional enum `day | week | month | year`

### `tavily_extract`

```json
{
  "urls": [
    "https://platform.openai.com/docs/overview",
    "https://modelcontextprotocol.io"
  ]
}
```

### `tavily_crawl`

```json
{
  "url": "https://modelcontextprotocol.io",
  "max_depth": 2,
  "max_breadth": 20,
  "limit": 25,
  "select_paths": ["/docs"],
  "allow_external": false
}
```

### `tavily_map`

```json
{
  "url": "https://modelcontextprotocol.io",
  "max_depth": 2,
  "max_results": 40,
  "select_paths": ["/docs"]
}
```

### `tavily_image_search`

```json
{
  "query": "mcp diagram",
  "search_depth": "basic",
  "max_results": 10
}
```

## Output Expectations

- `tavily_search`: ranked search results, optionally with raw content.
- `tavily_extract`: extracted text for known URLs.
- `tavily_crawl`: discovered pages plus extracted text.
- `tavily_map`: discovered URLs without page extraction.

## Selection Notes

- Choose `map` before `crawl` when structure is uncertain.
- Keep `crawl` limits narrow to avoid oversized outputs.
