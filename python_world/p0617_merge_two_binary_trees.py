from __future__ import annotations

from python_world.structures import TreeNode


class Solution:
    def mergeTrees(
        self,
        root1: TreeNode | None,
        root2: TreeNode | None,
    ) -> TreeNode | None:
        if root1 is None:
            return root2
        if root2 is None:
            return root1

        return TreeNode(
            root1.val + root2.val,
            self.mergeTrees(root1.left, root2.left),
            self.mergeTrees(root1.right, root2.right),
        )
