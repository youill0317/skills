"""Small CLI I/O helpers for research skill scripts."""

from __future__ import annotations

import sys


def force_utf8_stdio() -> None:
    """Prefer UTF-8 for CLI output, including Windows legacy code pages."""

    for stream_name in ("stdout", "stderr"):
        stream = getattr(sys, stream_name)
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure:
            reconfigure(encoding="utf-8", errors="replace")
