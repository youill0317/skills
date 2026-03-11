# Discovery And Navigation Tools

Load this reference when choosing search or directory-navigation tools in `mcp_obsidian`.

## Covered Tools

- `search_markdown`
- `list_directory`
- `get_directory_tree`

## `search_markdown`

Use when the path is unknown and the task starts from topic, tag, body text, or filename pattern.

### Input Shape

```json
{
  "query": "model context protocol",
  "directory": ".",
  "maxResults": 10,
  "respectGitignore": true,
  "useRegex": false,
  "fuzzy": false
}
```

Optional filters:

- `tag`
- `filenamePattern`
- `frontmatterFilter`
- `modifiedAfter`
- `modifiedBefore`

Constraints:

- `query` must be non-empty.
- `useRegex` and `fuzzy` cannot both be true.
- `modifiedAfter` and `modifiedBefore` must be ISO-like date strings.
- Keep one search intent per call.

Output notes:

- Results are grouped by filename, tag, and content matches.
- Structured match metadata is available in addition to the text summary.

## `list_directory`

Use for one directory level.

```json
{
  "path": ".",
  "markdownOnly": true,
  "showHidden": false,
  "respectGitignore": true
}
```

Use when you need one folder level only.

## `get_directory_tree`

Use for recursive structure overviews.

```json
{
  "path": ".",
  "depth": 3,
  "markdownOnly": true,
  "showHidden": false,
  "respectGitignore": true
}
```

Constraints:

- `depth` must be an integer and must respect the server max depth.
- Use only with directory paths, not file paths.
