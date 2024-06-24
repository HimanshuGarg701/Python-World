from __future__ import annotations

from python_world.structures import TreeNode


class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
