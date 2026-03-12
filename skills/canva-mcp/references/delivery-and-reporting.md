# Delivery And Reporting

Load this reference when the Canva work is finished or nearly finished and the next step is delivering the result back to the user.

## Default Delivery Rule

- Do not export and download a file by default after design completion.
- Prefer the Canva web link from `get-design` as the primary delivery artifact.
- Use `export-design` only when the user explicitly asks for a downloadable file such as PDF, PNG, PPTX, GIF, or MP4.

## Link-First Handoff

1. Ensure the work is backed by a real `design_id`.
2. Call `get-design` if the edit or view URL is not already known.
3. Return the Canva web URL to the user.
4. Include the `design_id` in the handoff message.

Prefer the editable Canva design URL when the user is collaborating on the design. If only a view URL is appropriate or available, return that instead. Do not replace the design link with an export URL unless the user asked for a file.

## Local Markdown Report Rule

After delivering the Canva web link, create a short Markdown report in the local workspace.

The report should include:

1. `title`
2. `topic`
3. `used_design`
4. `pages`
5. `canva_link`
6. `design_id`

## Report Content Standard

- `title`: final design title from Canva, or the agreed working title if the Canva title is not yet stable.
- `topic`: one short line describing the design subject or objective.
- `used_design`: the selected Canva design or generated concept that became the final deliverable.
- `pages`: one section per page or slide, each with the page number and its core message.
- `canva_link`: the returned Canva web URL.
- `design_id`: the Canva design ID exactly as used by the tools.

Keep the report concise. It is a design handoff note, not a full narrative transcript.

## Suggested Filename

Use a short, predictable filename such as:

- `canva-design-report.md`
- `canva-design-report-<slug>.md`

Choose a slug from the design title when that improves clarity.

## Suggested Markdown Shape

```md
# Canva Design Report

- Title: Q2 Product Review
- Topic: Executive review of adoption, churn, and roadmap priorities
- Used design: Selected Canva presentation candidate converted to final design
- Canva link: https://www.canva.com/design/DABCDEFG1234567/view
- Design ID: DABCDEFG1234567

## Page 1

- Core content: Quarter summary and top-line KPI snapshot

## Page 2

- Core content: Segment mix and enterprise growth contribution
```

## Minimal Retrieval Flow For The Report

- Use `get-design` for title, URLs, and `design_id`.
- Use `get-design-pages` for page list when the design is paged.
- Use `get-design-content` for page text when page-level summaries are needed.
- Use `get-presenter-notes` only when notes materially improve the page summary.
