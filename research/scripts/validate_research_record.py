#!/usr/bin/env python3
"""Run the full compact research-record validation gate."""

from __future__ import annotations

from pathlib import Path
import argparse
import subprocess
import sys

from script_io import force_utf8_stdio


force_utf8_stdio()


SCRIPT_DIR = Path(__file__).resolve().parent


def run_check(script_name: str, record: str, allow_placeholders: bool) -> subprocess.CompletedProcess:
    command = [sys.executable, "-B", str(SCRIPT_DIR / script_name), record]
    if allow_placeholders:
        command.append("--allow-placeholders")
    return subprocess.run(command, capture_output=True, text=True, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("record")
    parser.add_argument(
        "--allow-placeholders",
        action="store_true",
        help="Allow draft scaffold placeholders and planned/open rows",
    )
    args = parser.parse_args()

    checks = [
        ("validate_record.py", "shape"),
        ("audit_record_consistency.py", "consistency"),
    ]
    failures: list[str] = []
    for script_name, label in checks:
        result = run_check(script_name, args.record, args.allow_placeholders)
        if result.returncode != 0:
            output = (result.stdout + result.stderr).strip()
            failures.append(f"{label} check failed via {script_name}:\n{output}")

    if failures:
        print("Research record full validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Research record full validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
