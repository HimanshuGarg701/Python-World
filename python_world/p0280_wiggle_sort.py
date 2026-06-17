from __future__ import annotations


class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        for index in range(1, len(nums)):
            should_swap = (
                index % 2 == 1 and nums[index] < nums[index - 1]
            ) or (
                index % 2 == 0 and nums[index] > nums[index - 1]
            )
            if should_swap:
                nums[index], nums[index - 1] = nums[index - 1], nums[index]
