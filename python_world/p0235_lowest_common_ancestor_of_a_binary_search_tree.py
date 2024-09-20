from __future__ import annotations

from .structures import TreeNode


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        low, high = sorted((p.val, q.val))
        node = root
        while node.val < low or node.val > high:
            node = node.right if node.val < low else node.left
        return node
