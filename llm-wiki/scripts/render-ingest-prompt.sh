#!/usr/bin/env bash
set -euo pipefail

vault_path="${1:-$(pwd)}"
ingest_dir="${2:-_ingest}"

cat <<PROMPT
Use \$llm-wiki.

Process the Obsidian vault ingest folder into the appropriate llm-wiki folders.

Vault path: ${vault_path}
Ingest folder: ${ingest_dir}

Requirements:
- Treat the vault itself as the wiki workspace.
- Discover all existing llm-wiki folders and definition notes.
- Read existing wiki pages before deciding whether to create or update pages.
- Check existing sources, log entries, and manifests so already-processed sources are not duplicated.
- Move each ingested source into the selected wiki's raws/ folder. Do not copy and leave duplicates.
- Weave new information into existing pages when appropriate.
- Create new pages only when the idea is not already owned by an existing page.
- Create a new wiki only when no existing wiki fits.
- Preserve provenance. Every durable claim should cite a raw source path or be marked inferred/ambiguous.
- Preserve stable pages; if a source conflicts with stable content, stop and report the conflict.
- Update index.md and log.md.
- Verify moved and edited paths before final response.
- Summarize moved raws, edited pages, created pages, skipped files, and unresolved choices.
PROMPT
