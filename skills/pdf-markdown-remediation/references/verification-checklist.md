# Verification Checklist

Load this reference before finalizing the conversion.

## Completeness Checks

1. The output starts with YAML frontmatter.
2. The document body is present from beginning to end.
3. No section was summarized, omitted, or replaced with placeholder text.
4. URLs, image syntax, formulas, and footnote markers were preserved.
5. No system tags such as `<smtcmp_block>` remain.
6. Frontmatter fields beyond the empty block are limited to safe metadata supported by the source or requested convention.

## Fidelity Checks

1. Meaning was preserved during line repair and paragraph merging.
2. Heading depth matches the document structure.
3. Lists and tables are readable and do not distort source relationships.
4. Ambiguous OCR content was not over-corrected into new facts.

## Failure Handling

If a repair is uncertain:

- keep the more literal version
- avoid introducing missing content
- prefer incomplete formatting over fabricated reconstruction
