# Obsidian Web Clipper Intake

Use Web Clipper as a capture surface, not a synthesis layer. Preserve the page before the wiki agent interprets it.

## Import the Template

Import `assets/obsidian-web-clipper-llm-wiki-intake.json` in Web Clipper Settings → Templates → Import.

If browser control cannot claim a `chrome-extension://` page, do not bypass that boundary or claim the settings were applied. Deliver the template and these minimum manual steps instead.

After import:

1. Select the exact destination vault by name. Template exports do not preserve the vault choice.
2. Pre-create `_ingest/` at the vault root.
3. Keep behavior `Create a new note`, location `_ingest`, and save behavior `Add to Obsidian`.
4. Keep Interpreter off. The template intentionally contains no prompt variables.
5. Keep Legacy mode off so long clips use the normal clipboard transport instead of a length-limited URI.
6. Set highlight behavior to `Do nothing`, clear any page selection, and inspect the preview before saving. `{{content}}` may otherwise represent a selection or highlights rather than the article.
7. Keep triggers empty for manual selection. Add only narrow, non-overlapping site triggers when the user asks; a broad trigger can preempt specialized templates.

The template records only `source_url` and `captured_at` properties, a timestamped safe filename, the title, and extracted Markdown content. This keeps the raw note portable and avoids global property-type conflicts.

## Verify Once

Clip a normal article with no selection. Confirm that:

- one Markdown file appears under `_ingest/`;
- its `source_url` matches the page;
- its body contains the intended article rather than navigation, a selection, or an empty extraction;
- no summary or classification was generated;
- the note opens in the intended vault.

Do not enable silent open until this test passes.

## Limits

- Main-content extraction is heuristic. Use a site-specific selector template only for a recurring failure.
- Images normally remain remote URLs. Download material images into the vault or report that visual evidence was not inspected.
- Web Clipper settings and templates may use browser sync storage. Share template-only exports, not full settings exports that may contain provider credentials.
- Interpreter sends context to the configured provider and adds latency, cost, and provider-specific privacy terms. Keep it outside the immutable raw capture path.
- A missing folder and exact filename-collision behavior are not reliable contracts. Pre-create `_ingest/` and use the timestamped filename in the bundled template.
