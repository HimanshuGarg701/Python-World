from __future__ import annotations

from python_world.structures import TreeNode


class Solution:
    def inorderSuccessor(self, root: TreeNode | None, p: TreeNode) -> TreeNode | None:
        successor = None
        while root:
            if p.val < root.val:
                successor = root
                root = root.left
            else:
                root = root.right
        return successor
