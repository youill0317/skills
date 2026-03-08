# Exa Tools

## Covered Tools

- `exa_search`
- `exa_contents`
- `exa_find_similar`
- `exa_search_advanced`
- `exa_crawl`
- `exa_people_search`

## When To Use

- Use `exa_search` for semantic discovery when exact keywords are weak.
- Use `exa_contents` for known URLs.
- Use `exa_find_similar` from one seed URL.
- Use `exa_search_advanced` when domain, date, text, or crawl controls matter.
- Use `exa_crawl` for one live URL extraction.
- Use `exa_people_search` for people profiles.

## Input Shapes

### `exa_search`

```json
{
  "query": "companies building model context protocol tooling",
  "num_results": 10,
  "type": "neural",
  "include_text": false
}
```

### `exa_contents`

```json
{
  "urls": [
    "https://modelcontextprotocol.io/introduction"
  ],
  "include_text": true
}
```

### `exa_find_similar`

```json
{
  "url": "https://modelcontextprotocol.io",
  "num_results": 10,
  "type": "auto"
}
```

### `exa_search_advanced`

```json
{
  "query": "agent frameworks with mcp support",
  "num_results": 20,
  "include_domains": ["github.com", "docs.anthropic.com"],
  "start_published_date": "2025-01-01",
  "text_max_characters": 4000,
  "livecrawl": "fallback"
}
```

Important advanced parameters:

- `include_domains`, `exclude_domains`
- `start_published_date`, `end_published_date`
- `start_crawl_date`, `end_crawl_date`
- `include_text`, `exclude_text`
- `text_max_characters`
- `livecrawl`: `never | fallback | always | preferred`
- `subpages`, `subpage_target`

### `exa_crawl`

```json
{
  "url": "https://modelcontextprotocol.io/docs",
  "max_characters": 5000
}
```

### `exa_people_search`

```json
{
  "query": "founders of exa ai",
  "num_results": 5,
  "text_max_characters": 2000
}
```

## Output Expectations

- Search tools return ranked result items.
- Content and crawl tools return fetched text payloads.
- People search returns profile-like records rather than general web pages.
