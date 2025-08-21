from __future__ import annotations


class Solution:
    def hIndex(self, citations: list[int]) -> int:
        left, right = 0, len(citations)
        while left < right:
            middle = (left + right) // 2
            if citations[middle] >= len(citations) - middle:
                right = middle
            else:
                left = middle + 1
        return len(citations) - left
