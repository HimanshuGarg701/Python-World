from __future__ import annotations

from .structures import TreeNode


class Solution:
    def countUnivalSubtrees(self, root: TreeNode | None) -> int:
        count = 0

        def is_univalue(node: TreeNode | None) -> bool:
            nonlocal count
            if node is None:
                return True
            left = is_univalue(node.left)
            right = is_univalue(node.right)
            if not left or not right:
                return False
            if node.left and node.left.val != node.val:
                return False
            if node.right and node.right.val != node.val:
                return False
            count += 1
            return True

        is_univalue(root)
        return count
