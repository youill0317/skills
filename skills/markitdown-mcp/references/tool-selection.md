# Tool Selection

Use `MarkItDown MCP` when the main job is choosing or operating the MCP-side conversion tool, not when the task-facing skill should execute the conversion workflow.

## Choose MarkItDown MCP When

- The user has the original file, path, or URL.
- The task is blocked on tool choice, transport, setup, or accepted input shape.
- The task is source-to-Markdown conversion rather than repair of already-extracted text.
- The source is a supported input type for the connected MarkItDown release.
- You need to establish the correct conversion call before handing off to task execution.

## Do Not Choose MarkItDown MCP When

- The user only has broken OCR text, pasted PDF text, or layout-damaged Markdown.
- The user already needs actual first-pass conversion instructions; route to `markdown-conversion`.
- The task is to preserve high-fidelity layout, spreadsheet styling, or exact rendering details.
- The needed work is mostly cleanup, section repair, or normalization after conversion.
- The source is inaccessible or cannot be addressed in a form accepted by the connected MCP tool.

## Hand-off Rules

- Use `markdown-conversion` for task-facing first-pass conversion once tool choice is settled.
- Use `pdf-markdown-remediation` after conversion when the Markdown is incomplete, badly wrapped, structurally damaged, or misaligned with the source.
- Use `markdown-format-normalization` after conversion when the Markdown is readable but inconsistent.
- Use both in sequence only when the converted output first needs recovery and then normalization.

## Output Trust Boundary

- Treat converted Markdown as a best-effort representation.
- Verify headings, lists, tables, links, code blocks, and truncation-sensitive sections.
- Assume unsupported or complex source features may be simplified, omitted, or flattened.

## Official Guidance Boundary

Microsoft's MarkItDown documentation explicitly positions the project as a Markdown conversion utility and notes that it is not the best choice for high-fidelity document reproduction. Keep that boundary visible in user guidance.
