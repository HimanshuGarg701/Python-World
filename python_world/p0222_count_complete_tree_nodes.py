from __future__ import annotations

from python_world.structures import TreeNode


class Solution:
    def countNodes(self, root: TreeNode | None) -> int:
        def left_depth(node: TreeNode | None) -> int:
            depth = 0
            while node:
                depth += 1
                node = node.left
            return depth

        if root is None:
            return 0
        left = left_depth(root.left)
        right = left_depth(root.right)
        if left == right:
            return (1 << left) + self.countNodes(root.right)
        return (1 << right) + self.countNodes(root.left)
