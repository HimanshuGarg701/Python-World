from __future__ import annotations


def tenth_line(text: str) -> str | None:
    """Python equivalent of the line-selection shell command in problem 195."""
    lines = text.splitlines()
    return lines[9] if len(lines) >= 10 else None
