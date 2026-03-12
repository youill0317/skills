---
name: Document Summary
description: Produce structured summaries from local documents and notes. Use when the user asks for concise summaries, executive briefs, or key-point extraction.
category: task
---

# Mission

Extract and organize the essential content of documents into layered, actionable summaries.

## Category

`task`

## Use When

- The user wants a concise summary, executive brief, or key-point extraction.
- The source material is local documentation, notes, or loaded references.
- The deliverable should compress content rather than answer a narrow question.

## Scope

1. Summarize loaded documents and notes without inventing facts.
2. Adjust depth to document length, complexity, and audience.
3. Preserve important terms, numbers, and uncertainties.
4. Support multilingual input while keeping critical source terms intact.
5. Switch to domain-specific summary formats when the document type requires a fixed reporting structure.

## Core Workflow

1. Read target documents or references.
2. Classify document type using these explicit categories: `academic paper`, `technical`, `business`, `policy/legal`, `education/learning`, `news/report`, `opinion/essay/column`, or generic fallback.
3. Apply the document-type priority in this order when multiple labels seem plausible:
   1. Academic paper: journal article, conference paper, working paper, thesis chapter, dissertation excerpt.
   2. Policy/legal: law, regulation, case summary, policy draft, administrative guidance.
   3. News/report: news article, breaking update, press-style report, incident coverage.
   4. Opinion/essay/column: editorial, opinion piece, essay, signed column.
   5. Technical: API docs, technical design, architecture note, engineering procedure.
   6. Business: business report, strategy memo, market analysis, operational review.
   7. Education/learning: lecture note, textbook excerpt, study guide, training material.
4. If the source matches a domain-specific category, load the corresponding reference and follow its fixed Korean output format.
5. Otherwise, use the generic summary path and identify the main claims, data points, and open questions.
6. Select summary depth based on user request or document length.
7. Apply a length-aware strategy: direct summary for short files, grouped synthesis for medium files, and section-by-section reduction for long files.
8. Produce a layered summary following the output structure below, unless a domain-specific reference overrides it.
9. Add unknowns and follow-up checks when data is incomplete.

## Output Standard

Generic fallback summaries must include:

1. **1-line takeaway**: the single most important conclusion.
2. **Summary paragraph**: 3-5 sentences covering scope, findings, and implications.
3. **Key points**: bullet list of major claims or data.
4. **Open questions / unknowns**: gaps, ambiguities, or items needing verification.

Depth rules:

- **Overview**: 1-line takeaway + 3-5 key points.
- **Standard**: default format above.
- **Detailed**: add section-by-section breakdown with source references.
- **Executive**: add decision-focused action items.

For `Detailed` and `Executive` depths, add:

5. **Section breakdown**: per-section summaries with source references.
6. **Action items** (Executive only): concrete next steps derived from the content.

Domain-specific override rules:

- When the source matches a domain-specific reference, the fixed Korean section headers in that reference replace the generic summary paragraph format.
- Keep the generic `Overview`, `Standard`, `Detailed`, and `Executive` depth rules only for the fallback path or when a user explicitly requests hybrid detail.
- If metadata, dates, numbers, sample sizes, actors, or source details are missing in the document, state `확인 필요` rather than inferring them.

Domain-specific mappings:

- `academic paper` -> `references/academic-paper-summary.md`
- `technical` -> `references/technical-summary.md`
- `business` -> `references/business-summary.md`
- `policy/legal` -> `references/policy-legal-summary.md`
- `education/learning` -> `references/education-learning-summary.md`
- `news/report` -> `references/news-summary.md`
- `opinion/essay/column` -> `references/opinion-summary.md`

## Integration

1. Use after `document-qa` when question-specific evidence has already been collected.
2. Feed summaries into `report-writing`, `presentation-design`, or `planning` when a more structured deliverable is needed next.
3. Preserve translation-sensitive terms and open questions for downstream skills.

## Resource Loading

Pass only the needed `reference_paths` to `run_skill`; these files do not load automatically.

- Load `references/summary-style.md` when style or brevity needs tighter control.
- Load `references/summary-template.md` when the output should use the generic fallback structure.
- Load `references/extraction-rules.md` when deciding what counts as a key point is non-trivial.
- Load `references/academic-paper-summary.md` when the source is an academic paper and the output should follow the paper-summary report format in Korean.
- Load `references/technical-summary.md` when the source is a technical document, API guide, or architecture/procedure note.
- Load `references/business-summary.md` when the source is a strategy memo, market review, or business performance document.
- Load `references/policy-legal-summary.md` when the source is a policy, regulation, law, case-related summary, or administrative guidance.
- Load `references/education-learning-summary.md` when the source is a lecture note, textbook excerpt, training material, or study guide.
- Load `references/news-summary.md` when the source is a factual news article or report-style coverage.
- Load `references/opinion-summary.md` when the source is an essay, editorial, signed column, or opinion-focused article.
