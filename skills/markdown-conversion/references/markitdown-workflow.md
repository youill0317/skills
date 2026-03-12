# MarkItDown Workflow

Load this reference when performing initial source-to-Markdown conversion through MarkItDown MCP.

## Source Preference

1. Prefer the original source file or URL over pasted extracted text.
2. Use pasted extracted text only when the original source cannot be accessed in a form the converter can read.
3. Keep the source target as narrow as possible: one file or one URL per conversion pass unless the connected release explicitly supports batching.

## Execution Rules

1. Check the connected MCP tool list before assuming an exact tool name.
2. Confirm whether the server expects a plain path, a `file://` URI, or another URI form.
3. Use the simplest supported target shape that identifies the original source unambiguously.
4. Run the conversion once before deciding whether downstream repair is necessary.

## Expected Losses

- Complex layout may flatten.
- Tables may simplify.
- Rich media, comments, tracked changes, or unsupported embedded objects may be omitted or reduced.
- Heading depth and list structure may need downstream cleanup even when content is mostly present.

## Stop Conditions

- Stop here when the output is complete enough to be readable and only needs formatting cleanup.
- Escalate to `pdf-markdown-remediation` when content fidelity or structural completeness is in doubt.
