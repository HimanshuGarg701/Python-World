from __future__ import annotations

from .structures import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        def build(left: int, right: int) -> TreeNode | None:
            if left > right:
                return None
            middle = (left + right) // 2
            return TreeNode(nums[middle], build(left, middle - 1), build(middle + 1, right))

        return build(0, len(nums) - 1)

