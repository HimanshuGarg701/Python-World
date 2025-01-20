from __future__ import annotations


class Solution:
    def isBadVersion(self, version: int) -> bool:
        raise NotImplementedError("LeetCode supplies the isBadVersion API")

    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            middle = left + (right - left) // 2
            if self.isBadVersion(middle):
                right = middle
            else:
                left = middle + 1
        return left
