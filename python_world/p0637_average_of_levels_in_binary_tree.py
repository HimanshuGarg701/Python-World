from __future__ import annotations

from collections import deque

from python_world.structures import TreeNode


class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        if root is None:
            return []

        averages: list[float] = []
        queue = deque([root])
        while queue:
            level_sum = 0
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            averages.append(level_sum / level_size)
        return averages
