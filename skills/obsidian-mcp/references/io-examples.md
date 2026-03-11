# Representative I/O Patterns

Load this reference when the user needs concrete example calls or output shapes.

These examples show tool input objects only. Do not wrap them in `{"tool": "...", "args": {...}}` unless the client explicitly expects that outer envelope.

## Discovery Then Read

1. Find candidates with `search_markdown`.
2. Inspect structure with `read_markdown_toc`.
3. Read one section with `read_markdown_section`.
4. Escalate to `read_markdown_full` only if required.

## Example Sequence

### Step 1

```json
{
  "query": "semantic scholar",
  "directory": ".",
  "maxResults": 5
}
```

### Step 2

```json
{
  "path": "research/semantic-scholar.md",
  "maxLevel": 2
}
```

### Step 3

```json
{
  "path": "research/semantic-scholar.md",
  "header": "Findings",
  "includeSubsections": true
}
```

## Resource Examples

Use these URIs directly when the client supports resource reads:

- `mcp://markdown-explorer-mcp/vault-context`
- `mcp://markdown-explorer-mcp/info`

## Output Expectations

- Search returns grouped candidate results and structured match metadata.
- Read tools return text blocks with path and line cues when available.
- `read_markdown_full` includes parsed metadata when frontmatter exists.
- Link tools return grouped link or backlink records.
