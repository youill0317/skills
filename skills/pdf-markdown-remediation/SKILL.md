---
name: PDF Markdown Remediation
description: Repair noisy text copied or extracted from PDFs and reconstruct it into complete, readable Markdown. Use when PDF text has broken line wraps, OCR damage, layout artifacts, damaged tables or lists, and must be converted without losing content.
category: task
---

# Mission

Convert unstable PDF- or OCR-extracted raw text into complete, readable Markdown without changing meaning or dropping content.

## Category

`task`

## Use When

- The input is raw text copied from a PDF, OCR tool, or layout-based extractor.
- Sentences are broken by forced line wraps, hyphenated word splits, or repeated page artifacts.
- Tables, lists, headings, callouts, footnotes, or code blocks were damaged during extraction.
- The user needs a full Markdown reconstruction rather than a summary.

## Scope

1. Repair extraction artifacts while preserving source meaning.
2. Rebuild document structure in standard Markdown.
3. Preserve URLs, image syntax, numbers, formulas, and footnote references exactly when present.
4. Always add YAML frontmatter, keeping it minimal when no safe metadata can be recovered or inferred.
5. Keep the source language unchanged.
6. Never summarize, omit, translate, or invent content.

## Core Workflow

1. Clean repeated non-body artifacts such as page numbers, headers, footers, watermark text, and system tags.
2. Repair broken line wraps, paragraph splits, and line-end hyphenation only when the merge is strongly supported by context.
3. Identify structural units: title, sections, body paragraphs, lists, tables, callouts, code, math, images, and footnotes.
4. Reconstruct the document into standard Markdown with readable spacing and stable heading depth.
5. Insert YAML frontmatter first, then the full reconstructed document body.
6. Run a completeness pass to ensure every source segment is accounted for and no Markdown-internal tags remain.

## Output Standard

Every output must:

1. Start with YAML frontmatter.
2. Use pure Markdown only.
3. Preserve content order unless local reflow is required to repair line-wrap damage.
4. Include the entire document from start to finish.
5. Keep ambiguous repairs conservative; prefer visibly awkward but faithful output over guessed reconstruction.

## Integration

1. Use before `markdown-format-normalization` when the source is still raw PDF text rather than Markdown.
2. Hand off to `markdown-format-normalization` only after the document is structurally reconstructed and complete.
3. Do not use `document-summary` or `report-writing` as substitutes for remediation.

## Resource Loading

Pass only the needed `reference_paths` to `run_skill`; these files do not load automatically.

- Load `references/cleaning-and-repair.md` for artifact removal and line repair rules.
- Load `references/structure-analysis.md` when headings, tables, callouts, code, math, or footnotes are difficult to classify.
- Load `references/markdown-output-contract.md` when Markdown formatting rules must be applied strictly.
- Load `references/frontmatter-and-tags.md` when frontmatter or topic-tag selection needs consistency.
- Load `references/verification-checklist.md` for completeness and anti-hallucination checks.
