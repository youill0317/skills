"""Markdown helpers for compact research record scripts."""

from __future__ import annotations

import re


def read_markdown(path) -> str:
    return path.read_text(encoding="utf-8-sig")


def strip_fenced_code_blocks(text: str) -> str:
    return re.sub(
        r"^[ \t]{0,3}```[^\n]*\n.*?^[ \t]{0,3}```[ \t]*$",
        "",
        text,
        flags=re.MULTILINE | re.DOTALL,
    )


def section_body(text: str, heading: str) -> str:
    pattern = (
        rf"^##\s+{re.escape(heading)}\s*$"
        rf"(?P<body>.*?)(?=^##\s+|\Z)"
    )
    match = re.search(pattern, text, re.MULTILINE | re.DOTALL)
    return match.group("body").strip() if match else ""


def split_markdown_table_row(line: str) -> list[str]:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return []

    cells: list[str] = []
    current: list[str] = []
    escaped = False
    in_code = False
    for char in stripped[1:-1]:
        if escaped:
            current.append(char)
            escaped = False
            continue
        if char == "\\":
            escaped = True
            continue
        if char == "`":
            in_code = not in_code
            current.append(char)
            continue
        if char == "|" and not in_code:
            cells.append("".join(current).strip())
            current = []
            continue
        current.append(char)

    if escaped:
        current.append("\\")
    cells.append("".join(current).strip())
    return cells


def parse_markdown_rows(body: str) -> list[list[str]]:
    rows: list[list[str]] = []
    for raw_line in body.splitlines():
        cells = split_markdown_table_row(raw_line)
        if not cells:
            continue
        if all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
            continue
        rows.append(cells)
    return rows
