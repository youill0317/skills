# Cleaning and Repair

Load this reference when PDF text contains extraction noise, OCR instability, or line-wrap damage.

## Artifact Removal

Remove repeated non-body text only when it is clearly an extraction artifact:

- page numbers
- running headers and footers
- watermark text
- scanner labels
- system tags such as `<smtcmp_block>` or `<xml>`

Do not remove text that may be part of the document body, even if it looks repetitive, unless repetition is obvious across pages.

## Line and Paragraph Repair

1. Merge hard-wrapped lines into normal sentences when punctuation and syntax indicate continuation.
2. Preserve paragraph boundaries when the source clearly starts a new thought, list item, caption, or section.
3. Restore line-end hyphenation only when it is clearly an artificial split:
   - `pro- cessing` -> `processing`
   - `infor- mation` -> `information`
4. Keep literal hyphenated compounds when they are real words:
   - `state-of-the-art`
   - `long-term`

## OCR Damage Handling

1. Correct obvious OCR spacing and split-token errors only when the intended token is unambiguous.
2. Do not guess missing words, citations, or symbols.
3. Preserve uncertain content rather than replacing it with invented text.

## Repair Priorities

Apply repairs in this order:

1. remove repeated artifacts
2. restore broken words
3. merge broken sentences
4. restore paragraph boundaries
5. classify structure before formatting
