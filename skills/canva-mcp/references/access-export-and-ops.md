# Access, Export, And Page Operations

Load this reference when the task involves Canva URLs, export settings, comments, imports, or `merge-designs`.

## URL And ID Handling

- If the user gives a shortlink such as `https://canva.link/abc123`, call `resolve-shortlink` first.
- If the user gives a full design URL such as `https://www.canva.com/design/D...`, extract the `design_id` directly.
- Do not use a design view URL as the source for `import-design-from-url`; imports expect a public downloadable file URL.

## Import Guardrails

- `import-design-from-url` only accepts public HTTPS URLs.
- Reject local paths such as `C:\...`, `/Users/...`, `file://...`, or mentions of Downloads/Desktop/Documents.
- Prefer URLs that point directly to a downloadable file such as a PDF, PPTX, image, or document.

## Export Guardrails

- Do not call `export-design` by default at the end of a successful design task.
- Call `get-export-formats` before `export-design`.
- Keep `pages` 1-based when exporting specific pages.
- Use the export URL returned by Canva only when the user asked for a downloadable file.
- For image exports, specify width or height only when the user actually needs size control.

## Comment Workflows

- Use `list-comments` to inspect existing discussion before adding a new comment when context matters.
- Use `reply-to-comment` when responding inside an existing thread rather than creating a new top-level comment.
- Use `list-replies` only after the relevant `comment_id` is known.

## Structural Operation Rule

Always show the exact `merge-designs` operation summary before running it and ask for confirmation.

For insert or move operations only, a normal confirmation is enough.

For delete operations, explicitly highlight that deletion cannot be undone and wait for a clear approval phrase before continuing.

## Representative Input Shapes

### Resolve A Shortlink

```json
{
  "shortlink_id": "abc123",
  "user_intent": "Resolve a Canva short URL into the underlying design URL"
}
```

### Export A Design

```json
{
  "design_id": "DABCDEFG1234567",
  "format": {
    "type": "pdf",
    "export_quality": "regular",
    "pages": [1, 2, 3]
  },
  "user_intent": "Export the first three slides as PDF"
}
```

### Reorder Pages In An Existing Design

```json
{
  "type": "modify_existing_design",
  "design_id": "DABCDEFG1234567",
  "operations": [
    "move_pages:from=1,to=3"
  ],
  "user_intent": "Move the title slide after the agenda slide"
}
```
