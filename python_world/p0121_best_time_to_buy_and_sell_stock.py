class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minimum = float("inf")
        best = 0
        for price in prices:
            minimum = min(minimum, price)
            best = max(best, price - minimum)
        return best

