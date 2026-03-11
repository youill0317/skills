# Output Template

Use this structure when returning recommendations.

## 0) Vault Connection Policy

- Primary form: `[[Note]]`
- Escalation forms: `[[Note#Heading]]`, `[[Note#^block-id]]`, `![[Note]]`
- Tag style: lowercase kebab-case
- Note: apply the same policy to all notes unless user requested a change.

## 1) Top Connection Candidates

- `[[Note A]]` — why this note matters to the current note.
- `[[Note B#Key Heading]]` — why this section-level connection is better than whole-note link.

## 2) Suggested Placement

- Intro/context section: `[[Note A]]`
- Evidence/background section: `[[Note B#Key Heading]]`
- Quote/excerpt section: `[[Note D#^block-id]]`
- Optional embed area: `![[Note C]]`

## 3) Tag Suggestions

- Keep: `#tag1`, `#tag2`
- Add: `#tag3`, `#tag4`
- Normalize: `#old-tag -> #new-tag`

## 4) Paste-ready Snippet

```markdown
## Related Connections
- [[Note A]] — one-line rationale
- [[Note B#Key Heading]] — one-line rationale

## Tags
#tag1 #tag2 #tag3
```
