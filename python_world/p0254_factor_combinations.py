from __future__ import annotations


class Solution:
    def getFactors(self, n: int) -> list[list[int]]:
        result: list[list[int]] = []

        def search(remaining: int, smallest: int, factors: list[int]) -> None:
            factor = smallest
            while factor * factor <= remaining:
                if remaining % factor == 0:
                    result.append(factors + [factor, remaining // factor])
                    search(remaining // factor, factor, factors + [factor])
                factor += 1

        search(n, 2, [])
        return result
