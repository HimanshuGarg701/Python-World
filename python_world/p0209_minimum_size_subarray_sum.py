class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        total = 0
        answer = len(nums) + 1
        for right, value in enumerate(nums):
            total += value
            while total >= target:
                answer = min(answer, right - left + 1)
                total -= nums[left]
                left += 1
        return 0 if answer > len(nums) else answer
