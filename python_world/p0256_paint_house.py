from __future__ import annotations


class Solution:
    def minCost(self, costs: list[list[int]]) -> int:
        if not costs:
            return 0
        red, blue, green = costs[0]
        for red_cost, blue_cost, green_cost in costs[1:]:
            red, blue, green = (
                red_cost + min(blue, green),
                blue_cost + min(red, green),
                green_cost + min(red, blue),
            )
        return min(red, blue, green)
