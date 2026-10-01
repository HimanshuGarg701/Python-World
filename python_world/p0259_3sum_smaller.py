from __future__ import annotations


class Solution:
    def threeSumSmaller(self, nums: list[int], target: int) -> int:
        nums.sort()
        count = 0
        for first in range(len(nums) - 2):
            left, right = first + 1, len(nums) - 1
            while left < right:
                if nums[first] + nums[left] + nums[right] < target:
                    count += right - left
                    left += 1
                else:
                    right -= 1
        return count
