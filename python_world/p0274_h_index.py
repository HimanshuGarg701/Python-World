from __future__ import annotations


class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse=True)
        h = 0
        for index, citations_count in enumerate(citations, 1):
            if citations_count < index:
                break
            h = index
        return h
