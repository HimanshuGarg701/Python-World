from __future__ import annotations

from .structures import TreeNode


class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def height(node: TreeNode | None) -> int:
            if node is None:
                return 0
            left = height(node.left)
            if left == -1:
                return -1
            right = height(node.right)
            if right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return height(root) != -1

