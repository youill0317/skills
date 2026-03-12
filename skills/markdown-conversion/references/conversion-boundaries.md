# Conversion Boundaries

Load this reference when deciding whether the task should stop at first-pass conversion or continue into cleanup or repair.

## Choose Markdown Conversion When

- The input is an accessible non-Markdown source such as PDF, DOCX, PPTX, HTML, or a web page.
- The immediate goal is to generate an initial Markdown draft.
- The user needs a practical Markdown starting point rather than source-perfect reconstruction.

## Do Not Stop Here When

- The converted Markdown is readable but inconsistent in heading depth, lists, spacing, frontmatter, or tables.
- The output clearly omits sections, merges paragraphs incorrectly, damages tables, or collapses list structure.
- The user needs the Markdown to match the original source as closely as possible.

## Hand-off Rules

- Route readable-but-messy Markdown to `markdown-format-normalization`.
- Route source mismatch, omission, OCR damage, paragraph collapse, table damage, or list damage to `pdf-markdown-remediation`.
- Use both in sequence only when the document first needs source-aligned repair and then final normalization.

## Trust Boundary

- Treat MarkItDown output as first-pass conversion only.
- Do not claim that unsupported features, rich layouts, or embedded objects were fully preserved unless directly verified.
