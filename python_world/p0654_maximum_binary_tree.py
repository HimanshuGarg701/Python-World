from __future__ import annotations

from python_world.structures import TreeNode


class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> TreeNode | None:
        stack: list[TreeNode] = []
        for number in nums:
            node = TreeNode(number)
            while stack and stack[-1].val < number:
                node.left = stack.pop()
            if stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0] if stack else None
