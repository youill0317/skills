# Setup And Examples

Use official MarkItDown documentation as the source of truth:

- Microsoft MarkItDown GitHub: `github.com/microsoft/markitdown`
- `markitdown-mcp` PyPI package: `pypi.org/project/markitdown-mcp/`

## Setup Guidance

- `markitdown-mcp` exposes an MCP server around MarkItDown conversion.
- The official package documentation describes transport support for `stdio`, Streamable HTTP, and SSE.
- Exact installation and launch commands may vary by environment, so follow the current official package instructions instead of hard-coding client-specific launch text into the skill body.

## Tool Discovery Rule

- Check the connected MCP tool list before assuming an exact tool name or parameter schema.
- In the current official package documentation, the primary tool is described as `convert_to_markdown(uri)`.
- Treat this as a likely default, not a guaranteed invariant across releases.

## Input Pattern Guidance

- Prefer one concrete input target at a time.
- Use the URI or file-addressing pattern accepted by the connected server.
- Prefer explicit local paths or explicit URLs over vague human descriptions of files.
- Confirm whether the connected server expects file paths, `file://` URIs, HTTPS URLs, or another URI form before calling it.

## Example Guidance Shapes

- Local file conversion:
  - Choose MarkItDown MCP when you need to verify transport or input shape first.
  - Confirm whether the tool accepts a plain path or a `file://` URI.
  - Hand the confirmed call shape to `markdown-conversion` for the task-facing conversion step.
- Remote page conversion:
  - Choose MarkItDown MCP when the goal is page-to-Markdown conversion and the question is how to call the MCP tool rather than whether to convert.
  - Pass one explicit HTTPS URL.
  - Review the result for simplified structure or omitted rich elements.
- Post-conversion cleanup:
  - If the Markdown is readable but messy, route to `markdown-format-normalization`.
  - If the Markdown is structurally broken, misaligned with the source, or derived from noisy OCR/PDF extraction, route to `pdf-markdown-remediation`.
