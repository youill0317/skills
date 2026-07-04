#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -ne 2 ]; then
  printf 'Usage: %s <source_file> <wiki_dir>\n' "$0" >&2
  exit 2
fi

source_file="$1"
wiki_dir="$2"
raws_dir="$wiki_dir/raws"
definition_note="$wiki_dir/Wiki.md"

if [ ! -f "$source_file" ]; then
  printf 'Source file does not exist: %s\n' "$source_file" >&2
  exit 1
fi

if [ ! -f "$definition_note" ]; then
  printf 'Target wiki is missing definition note: %s\n' "$definition_note" >&2
  exit 1
fi

if ! grep -q '^llm_wiki:[[:space:]]*true[[:space:]]*$' "$definition_note"; then
  printf 'Target wiki definition is missing llm_wiki: true: %s\n' "$definition_note" >&2
  exit 1
fi

mkdir -p "$raws_dir"

base_name="$(basename "$source_file")"
name="${base_name%.*}"
ext=""
if [ "$name" != "$base_name" ]; then
  ext=".${base_name##*.}"
fi

dest="$raws_dir/$base_name"
counter=2
while [ -e "$dest" ]; do
  dest="$raws_dir/${name}-${counter}${ext}"
  counter=$((counter + 1))
done

mv -- "$source_file" "$dest"
printf '%s\n' "$dest"
