# Resources and Config

Load this reference when the question is about vault scope, startup configuration, or whether a resource is better than a tool call.

## Base Directory Behavior

The server reads from `MARKDOWN_BASE_DIR` when set.

- On Windows, multiple roots are separated by `;`
- If `MARKDOWN_BASE_DIR` is omitted, the server uses its current working directory
- All `path` and `directory` arguments must resolve inside configured base directories

Example:

```json
{
  "env": {
    "MARKDOWN_BASE_DIR": "C:/VaultA;C:/VaultB"
  }
}
```

## When to Use Resources

Prefer a resource read over a filesystem tool call when the user needs a fast snapshot rather than targeted file retrieval.

### `vault-context`

URI: `mcp://markdown-explorer-mcp/vault-context`

Use for:

- configured base directories
- top-level folder and root-file overview
- recently modified markdown files
- popular frontmatter tags
- quick vault-wide orientation before choosing a tool

This resource is a snapshot, not a substitute for targeted reads.

### `server-info`

URI: `mcp://markdown-explorer-mcp/info`

Use for:

- current server version
- available tools and resources
- feature summary
- tool-role confirmation before planning a workflow

## Common Troubleshooting

1. Path not visible:
   - verify `MARKDOWN_BASE_DIR`
   - confirm the path is under one of the configured roots
   - use `vault-context` or `list_directory` to inspect the visible roots

2. Unexpected path resolution:
   - remember that relative paths resolve within configured base directories
   - if `MARKDOWN_BASE_DIR` is unset, the server may be using its startup working directory

3. Tool choice uncertainty:
   - read `server-info` first for capability confirmation
   - read `vault-context` first for environment orientation
