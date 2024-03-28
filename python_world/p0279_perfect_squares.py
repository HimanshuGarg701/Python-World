from __future__ import annotations

from math import isqrt


class Solution:
    def numSquares(self, n: int) -> int:
        if isqrt(n) ** 2 == n:
            return 1
        reduced = n
        while reduced % 4 == 0:
            reduced //= 4
        if reduced % 8 == 7:
            return 4
        for first in range(1, isqrt(n) + 1):
            remainder = n - first * first
            if isqrt(remainder) ** 2 == remainder:
                return 2
        return 3
