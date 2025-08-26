def transpose_file(text: str) -> str:
    """Python equivalent of the AWK transpose requested by LeetCode problem 194."""
    rows = [line.split() for line in text.splitlines() if line.strip()]
    if not rows:
        return ""
    return "\n".join(" ".join(column) for column in zip(*rows))

