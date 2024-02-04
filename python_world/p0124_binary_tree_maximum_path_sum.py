from __future__ import annotations

from .structures import TreeNode


class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        best = float("-inf")

        def gain(node: TreeNode | None) -> int:
            nonlocal best
            if node is None:
                return 0
            left = max(0, gain(node.left))
            right = max(0, gain(node.right))
            best = max(best, node.val + left + right)
            return node.val + max(left, right)

        gain(root)
        return int(best)

