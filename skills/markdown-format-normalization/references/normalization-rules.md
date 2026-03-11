# Normalization Rules

Load this reference when cleaning inconsistent Markdown without changing document meaning.

## Core Principle

Preserve content first, normalize formatting second.

## Allowed Changes

- fix heading depth when hierarchy is clear
- add blank lines between paragraphs and block elements
- normalize list markers and indentation
- repair malformed table separators
- normalize callout and blockquote formatting
- normalize YAML frontmatter shape and tag list formatting
- standardize code fence formatting

## Disallowed Changes

- summarizing or shortening content
- translating text
- removing URLs or images
- rewriting claims for style alone
- inventing headings, tags, or sections unsupported by the source

## Minimal-Change Rule

Prefer the smallest formatting edit that makes the Markdown readable and internally consistent.
