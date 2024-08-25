class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        if k == 0 or not prices:
            return 0
        if k >= len(prices) // 2:
            return sum(max(0, current - previous) for previous, current in zip(prices, prices[1:]))
        buys = [float("-inf")] * (k + 1)
        sells = [0] * (k + 1)
        for price in prices:
            for transaction in range(1, k + 1):
                buys[transaction] = max(buys[transaction], sells[transaction - 1] - price)
                sells[transaction] = max(sells[transaction], buys[transaction] + price)
        return sells[k]

