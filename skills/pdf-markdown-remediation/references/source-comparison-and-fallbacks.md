# Source Comparison and Fallbacks

Load this reference when deciding which source view should control a repair.

## Truth Priority

1. Original source file or page
2. Direct readable extract from the source
3. MarkItDown conversion output
4. Other auxiliary extracts or OCR views

When these disagree, prefer the highest-priority source that can actually support the disputed segment.

## Comparison Workflow

1. Identify whether the current Markdown is missing content, mistranscribed, or structurally collapsed.
2. Compare the damaged segment against the original source first.
3. If direct source reading is limited, compare at least one auxiliary extract such as MarkItDown output.
4. Recover only the content that is supported by the best available evidence.
5. Leave unresolved uncertainty conservative and visible in the wording rather than fabricating certainty.

## Typical Repair Cases

- Missing section headings in converted Markdown
- Paragraphs merged across page or slide boundaries
- List markers dropped during extraction
- Tables flattened into prose
- OCR token splits or substitutions
- Partial omission of captions, notes, or footnotes
