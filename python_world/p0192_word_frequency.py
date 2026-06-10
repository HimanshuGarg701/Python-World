from collections import Counter


def word_frequency(text: str) -> list[tuple[str, int]]:
    """Python equivalent of the word-frequency shell pipeline in problem 192."""
    counts = Counter(text.split())
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))

