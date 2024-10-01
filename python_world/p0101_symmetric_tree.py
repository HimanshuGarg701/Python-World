from __future__ import annotations

from .structures import TreeNode


class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def mirror(left: TreeNode | None, right: TreeNode | None) -> bool:
            if left is None or right is None:
                return left is right
            return (
                left.val == right.val
                and mirror(left.left, right.right)
                and mirror(left.right, right.left)
            )

        return root is None or mirror(root.left, root.right)

