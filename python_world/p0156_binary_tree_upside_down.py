from __future__ import annotations

from .structures import TreeNode


class Solution:
    def upsideDownBinaryTree(self, root: TreeNode | None) -> TreeNode | None:
        parent = parent_right = None
        current = root
        while current:
            following = current.left
            current.left = parent_right
            parent_right = current.right
            current.right = parent
            parent = current
            current = following
        return parent

