from __future__ import annotations


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        missing = len(nums)
        for index, number in enumerate(nums):
            missing ^= index ^ number
        return missing
