from __future__ import annotations

from .structures import TreeNode


class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        stack: list[TreeNode] = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            node = node.right
        raise ValueError("k exceeds the number of nodes")
