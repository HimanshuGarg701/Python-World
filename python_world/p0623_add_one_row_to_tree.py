from __future__ import annotations

from collections import deque

from python_world.structures import TreeNode


class Solution:
    def addOneRow(
        self,
        root: TreeNode | None,
        val: int,
        depth: int,
    ) -> TreeNode | None:
        if depth == 1:
            return TreeNode(val, root)
        if root is None:
            return None

        queue = deque([root])
        current_depth = 1
        while queue and current_depth < depth - 1:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            current_depth += 1

        for node in queue:
            node.left = TreeNode(val, node.left)
            node.right = TreeNode(val, None, node.right)
        return root
