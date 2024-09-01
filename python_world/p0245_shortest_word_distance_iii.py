from __future__ import annotations


class Solution:
    def shortestWordDistance(self, wordsDict: list[str], word1: str, word2: str) -> int:
        first = second = -1
        best = len(wordsDict)
        for index, word in enumerate(wordsDict):
            if word1 == word2 and word == word1:
                first, second = second, index
            elif word == word1:
                first = index
            elif word == word2:
                second = index
            if first >= 0 and second >= 0:
                best = min(best, abs(first - second))
        return best
