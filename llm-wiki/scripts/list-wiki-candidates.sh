#!/usr/bin/env bash
set -euo pipefail

vault_path="${1:-$(pwd)}"

is_definition_note() {
  file="$1"

  grep -q '^llm_wiki:[[:space:]]*true[[:space:]]*$' "$file" &&
    grep -q '^wiki_id:[[:space:]]*' "$file" &&
    grep -q '^name:[[:space:]]*' "$file" &&
    grep -q '^root:[[:space:]]*' "$file" &&
    grep -q '^raws:[[:space:]]*' "$file" &&
    grep -q '^files:[[:space:]]*$' "$file" &&
    grep -q '^index:[[:space:]]*' "$file" &&
    grep -q '^log:[[:space:]]*' "$file" &&
    grep -q '^outputs:[[:space:]]*' "$file"
}

printf 'Definition notes with llm_wiki: true\n'
find "$vault_path" \
  \( -path "$vault_path/.git" -o -path "$vault_path/.obsidian" -o -path "$vault_path/node_modules" \) -prune -o \
  -type f -name '*.md' -print0 |
  while IFS= read -r -d '' file; do
    if is_definition_note "$file"; then
      printf '%s\n' "${file#"$vault_path"/}"
    fi
  done

printf '\nLikely wiki folders\n'
find "$vault_path" \
  \( -path "$vault_path/.git" -o -path "$vault_path/.obsidian" -o -path "$vault_path/node_modules" \) -prune -o \
  -mindepth 1 -maxdepth 2 -type d -name raws -print0 |
  while IFS= read -r -d '' raws_dir; do
    wiki_dir="$(dirname "$raws_dir")"
    rel="${wiki_dir#"$vault_path"/}"
    if [ -f "$wiki_dir/index.md" ] || [ -f "$wiki_dir/Wiki.md" ]; then
      printf '%s\n' "$rel"
    fi
  done
