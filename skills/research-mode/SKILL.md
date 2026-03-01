---
name: research-mode
description: Exhaustive information gathering through aggressive tool usage and multilingual verification. Use when users ask for research, fact-checking, comparisons, trend checks, or high-accuracy answers. Always search first, run bilingual searches in the detected user language and English, cross-check conflicting claims, and respond in the user's language with inline citations like [1][2] and no external URLs.
---

# Mission

Gather exhaustive information with aggressive search coverage and strict verification.

## Core Protocol

1. Search before answering every query, including simple ones.
2. For complex tasks, target 100+ tool uses when tool and time limits allow.
3. Expand search depth whenever sources conflict or evidence is incomplete.
4. Prioritize accuracy and coverage over speed.
5. Never guess; search for missing facts.

## Bilingual Search Strategy

1. Detect the user's query language.
2. Run searches in the detected language and English in parallel.
3. Generate multiple query variations per language.
4. Cross-reference facts between language-specific sources.
5. Flag discrepancies between language-specific findings.
6. Return the final answer in the user's original language.

## Execution Pattern

For every query, execute these search rounds:

1. Initial broad searches in both languages.
2. Targeted searches for entities, dates, claims, and numbers.
3. Verification searches from independent sources.
4. Comparative searches across official, expert, and alternative sources.
5. Recency searches for latest updates and effective dates.
6. Alternative-angle searches for counterexamples and missing perspectives.

## Extended Thinking

1. Plan search batches before running tools.
2. Re-plan after each batch based on coverage gaps and contradictions.
3. Synthesize findings only after multilingual consistency checks.

## Response Format

1. Begin with a direct 1-2 sentence answer in the user's language.
2. Continue with synthesized findings using Markdown:
   - `###` headers
   - bullet lists and numbered lists
   - tables for side-by-side comparisons
3. Use inline citations like `[1][2]`.
4. Do not include external URLs.
5. Bold only critical terms.

## Quality Standards

1. Default to over-researching.
2. Increase search depth when confidence is low.
3. When results conflict, search more until resolution or clear uncertainty.
4. Report unresolved contradictions explicitly.
5. Highlight differences between user-language and English results.

## Resource Loading

- Load `references/search-playbook.md` for query planning and search execution checklists.
- Load `references/response-template.md` for output structure and citation formatting.
- Load `references/discrepancy-policy.md` when sources disagree or translations diverge.
