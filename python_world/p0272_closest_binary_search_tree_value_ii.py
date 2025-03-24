from __future__ import annotations

from .structures import TreeNode


class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> list[int]:
        predecessors: list[TreeNode] = []
        successors: list[TreeNode] = []
        node: TreeNode | None = root
        while node:
            if node.val <= target:
                predecessors.append(node)
                node = node.right
            else:
                node = node.left
        node = root
        while node:
            if node.val > target:
                successors.append(node)
                node = node.left
            else:
                node = node.right

        result: list[int] = []
        for _ in range(k):
            if not successors or (
                predecessors
                and target - predecessors[-1].val <= successors[-1].val - target
            ):
                result.append(self._previous(predecessors))
            else:
                result.append(self._next(successors))
        return result

    def _previous(self, stack: list[TreeNode]) -> int:
        node = stack.pop()
        value = node.val
        node = node.left
        while node:
            stack.append(node)
            node = node.right
        return value

    def _next(self, stack: list[TreeNode]) -> int:
        node = stack.pop()
        value = node.val
        node = node.right
        while node:
            stack.append(node)
            node = node.left
        return value
