#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -lt 3 ] || [ "$#" -gt 4 ]; then
  printf 'Usage: %s <vault_path> <wiki_folder> <wiki_id> [display_name]\n' "$0" >&2
  exit 2
fi

vault_path="${1%/}"
wiki_folder="$2"
wiki_id="$3"
display_name="${4:-$wiki_folder}"

case "$wiki_folder" in
  "" | "." | ".." | /* | *"/"* | *".."*)
    printf 'wiki_folder must be a single root-level folder name: %s\n' "$wiki_folder" >&2
    exit 1
    ;;
esac

case "$wiki_id" in
  "" | *[!a-z0-9_-]*)
    printf 'wiki_id must contain only lowercase letters, numbers, underscores, and hyphens: %s\n' "$wiki_id" >&2
    exit 1
    ;;
esac

wiki_root="$vault_path/$wiki_folder"
if [ -e "$wiki_root" ]; then
  printf 'Target wiki folder already exists: %s\n' "$wiki_root" >&2
  exit 1
fi

quoted_display="$(printf '%s' "$display_name" | sed "s/'/''/g")"
today="$(date +%Y-%m-%d)"

mkdir -p \
  "$wiki_root/raws" \
  "$wiki_root/concepts" \
  "$wiki_root/entities" \
  "$wiki_root/decisions" \
  "$wiki_root/outputs"

cat > "$wiki_root/Wiki.md" <<EOF
---
llm_wiki: true
wiki_id: $wiki_id
name: '$quoted_display'
root: $wiki_folder
raws: $wiki_folder/raws
files:
  concepts: $wiki_folder/concepts
  entities: $wiki_folder/entities
  decisions: $wiki_folder/decisions
index: $wiki_folder/index.md
log: $wiki_folder/log.md
outputs: $wiki_folder/outputs
---
# $display_name

## Scope

- Add the wiki's topic boundary here.

## Ingest Rules

- Move processed sources into \`raws/\`.
- Update existing pages before creating new pages.
- Create new pages only for durable concepts, entities, decisions, or outputs.
EOF

cat > "$wiki_root/index.md" <<EOF
# $display_name Index

## Concepts

## Entities

## Decisions

## Outputs
EOF

cat > "$wiki_root/log.md" <<EOF
# $display_name Log

## $today

- Created wiki scaffold.
EOF

printf '%s\n' "$wiki_root"
