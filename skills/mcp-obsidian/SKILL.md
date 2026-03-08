---
name: mcp-obsidian
description: Guide for the `mcp_obsidian` server and its tools. Use when users ask how to search markdown notes, read files or sections, inspect links, navigate directories, or choose parameters and examples for Obsidian markdown tools.
---

# Mission

Use `mcp_obsidian` tools with a strict discovery-first and narrow-read approach.

## Scope

1. Cover tool selection, parameter usage, path handling, and example calls for `mcp_obsidian`.
2. Focus on local markdown discovery, reading, directory navigation, and link analysis.
3. Keep reads as narrow as possible.
4. Preserve path, header, and line-level evidence when available.

## Operating Rules

1. Use discovery tools when the path is unknown.
2. Use read tools only after the path is known.
3. Use link tools only when note relationships matter.
4. Use directory tools for structure, not for content retrieval.
5. Keep `path` values inside `BASE_DIRS`.

## Tool Families

- Discovery: `search_markdown`
- Directory structure: `list_directory`, `get_directory_tree`
- Reading: `read_markdown_toc`, `read_markdown_section`, `read_markdown_full`
- Link analysis: `get_linked_files`, `get_backlinks`

## Resource Loading

- Load `references/discovery-and-navigation.md` for search and directory tools.
- Load `references/read-and-link-tools.md` for read and link tools.
- Load `references/io-examples.md` for representative argument shapes and output patterns.
