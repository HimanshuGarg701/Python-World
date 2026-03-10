from __future__ import annotations

from python_world.structures import TreeNode


class Solution:
    def findTarget(self, root: TreeNode | None, k: int) -> bool:
        seen: set[int] = set()
        stack = [root] if root else []
        while stack:
            node = stack.pop()
            if k - node.val in seen:
                return True
            seen.add(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False
