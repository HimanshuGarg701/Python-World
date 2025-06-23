from __future__ import annotations


class Solution:
    def minCostII(self, costs: list[list[int]]) -> int:
        if not costs:
            return 0
        if len(costs[0]) == 1:
            return costs[0][0] if len(costs) == 1 else -1
        previous = costs[0][:]
        for row in costs[1:]:
            smallest = min(range(len(previous)), key=previous.__getitem__)
            second = min(
                (index for index in range(len(previous)) if index != smallest),
                key=previous.__getitem__,
            )
            previous = [
                cost + (previous[second] if color == smallest else previous[smallest])
                for color, cost in enumerate(row)
            ]
        return min(previous)
