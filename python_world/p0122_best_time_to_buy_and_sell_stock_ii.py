class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        return sum(max(0, current - previous) for previous, current in zip(prices, prices[1:]))

