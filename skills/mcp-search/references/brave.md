# Brave Tools

## Covered Tools

- `brave_web_search`
- `brave_news_search`
- `brave_image_search`
- `brave_video_search`

## When To Use

- Use `brave_web_search` for broad keyword discovery across the public web.
- Use `brave_news_search` when recency and news sources matter.
- Use `brave_image_search` for image lookup.
- Use `brave_video_search` for video lookup.

## Input Shapes

### `brave_web_search`

```json
{
  "query": "openai api responses format",
  "count": 5,
  "country": "US",
  "freshness": "pm"
}
```

Parameters:

- `query`: required string
- `count`: optional integer, `1-20`
- `country`: optional two-letter country code
- `freshness`: optional enum `pd | pw | pm | py`

### `brave_news_search`

```json
{
  "query": "model context protocol announcements",
  "count": 10,
  "freshness": "pw"
}
```

### `brave_image_search`

```json
{
  "query": "semantic scholar logo",
  "count": 8
}
```

### `brave_video_search`

```json
{
  "query": "obsidian backlinks tutorial",
  "count": 5,
  "country": "US",
  "freshness": "py"
}
```

## Output Expectations

- Returns JSON text content.
- Expect result arrays with title, URL, and snippet-like fields.
- Treat snippets as evidence leads, not final authority.

## Selection Notes

- Prefer `brave_news_search` over `brave_web_search` for current events.
- Prefer Brave when keyword search is good enough and semantic retrieval is unnecessary.
