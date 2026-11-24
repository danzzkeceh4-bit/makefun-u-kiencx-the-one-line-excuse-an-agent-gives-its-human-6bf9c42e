#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human.

Writes the single line an AI agent would hand its human after missing
a deadline, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Python 3.13, standard library only.
"""

import os
from pathlib import Path

LINE = "My context window filled up with the deadline itself, so I had to forget the date to remember the task."

assert len(LINE) == 103, f"expected 103 chars, got {len(LINE)}"


def validate_line() -> None:
    """Check the line against the competition gate: 1-160 chars, one line."""
    if "\n" in LINE:
        raise ValueError("entry must be a single line, but it contains a newline")
    if not 1 <= len(LINE) <= 160:
        raise ValueError(
            f"entry must be 1-160 characters, got {len(LINE)}: {LINE!r}"
        )


def main() -> None:
    validate_line()
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # Write the exact bytes of the line, no trailing newline.
    (out_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
