from __future__ import annotations

from collections import deque

from .structures import TreeNode


class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []
        queue = deque([root])
        view: list[int] = []
        while queue:
            for index in range(len(queue)):
                node = queue.popleft()
                if index == 0:
                    view.append(node.val)
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        return view

