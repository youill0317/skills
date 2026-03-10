# Output Template

Use this structure when returning recommendations.

## 0) Connection Style

- Primary style: `[[wikilink]]` | `[[Note#Heading]]` | `[[Note#^block-id]]` | `![[Note]]` | `tags`
- Why this style fits the current note.
- Consistency rule: keep one primary style in this response unless user asked for mixed styles.

## 1) Top Connection Candidates

- `[[Note A]]` — why this note matters to the current note.
- `[[Note B#Key Heading]]` — why this section-level connection is better than whole-note link.

## 2) Suggested Placement

- Intro/context section: `[[Note A]]`
- Evidence/background section: `[[Note B#Key Heading]]`
- Quote/excerpt section: `![[Note C]]`
- Next steps/tasks section: `[[Note D#^block-id]]`

## 3) Tag Suggestions

- Keep: `#tag1`, `#tag2`
- Add: `#tag3`, `#tag4`
- Normalize: `#old-tag -> #new-tag`

## 4) Paste-ready Snippet

```markdown
## Related Connections
- [[Note A]] — one-line rationale
- [[Note B#Key Heading]] — one-line rationale
- ![[Note C]] — one-line rationale

## Tags
#tag1 #tag2 #tag3
```
