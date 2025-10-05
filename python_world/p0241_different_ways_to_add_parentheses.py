from __future__ import annotations

from functools import cache


class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        @cache
        def solve(part: str) -> tuple[int, ...]:
            results: list[int] = []
            for index, character in enumerate(part):
                if character not in "+-*":
                    continue
                for left in solve(part[:index]):
                    for right in solve(part[index + 1 :]):
                        if character == "+":
                            results.append(left + right)
                        elif character == "-":
                            results.append(left - right)
                        else:
                            results.append(left * right)
            return tuple(results or [int(part)])

        return list(solve(expression))
