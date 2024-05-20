class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window_sum = sum(nums[:k])
        best = window_sum
        for index in range(k, len(nums)):
            window_sum += nums[index] - nums[index - k]
            best = max(best, window_sum)
        return best / k
