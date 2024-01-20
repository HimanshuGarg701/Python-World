from __future__ import annotations

from .structures import TreeNode


class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []
        result: list[int] = []
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result[::-1]

