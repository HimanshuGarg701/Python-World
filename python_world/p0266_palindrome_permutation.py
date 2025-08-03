from __future__ import annotations

from collections import Counter


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        return sum(count % 2 for count in Counter(s).values()) <= 1
