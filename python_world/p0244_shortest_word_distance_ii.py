from __future__ import annotations

from collections import defaultdict


class WordDistance:
    def __init__(self, wordsDict: list[str]):
        self._positions: dict[str, list[int]] = defaultdict(list)
        for index, word in enumerate(wordsDict):
            self._positions[word].append(index)

    def shortest(self, word1: str, word2: str) -> int:
        first = self._positions[word1]
        second = self._positions[word2]
        left = right = 0
        best = float("inf")
        while left < len(first) and right < len(second):
            best = min(best, abs(first[left] - second[right]))
            if first[left] < second[right]:
                left += 1
            else:
                right += 1
        return int(best)
