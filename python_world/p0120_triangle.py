class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        costs = triangle[-1].copy()
        for row in range(len(triangle) - 2, -1, -1):
            for column, value in enumerate(triangle[row]):
                costs[column] = value + min(costs[column], costs[column + 1])
        return costs[0]
