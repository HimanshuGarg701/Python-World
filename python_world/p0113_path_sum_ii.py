from __future__ import annotations

from .structures import TreeNode


class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        paths: list[list[int]] = []

        def visit(node: TreeNode | None, remaining: int, path: list[int]) -> None:
            if node is None:
                return
            path.append(node.val)
            if node.left is None and node.right is None and node.val == remaining:
                paths.append(path.copy())
            else:
                visit(node.left, remaining - node.val, path)
                visit(node.right, remaining - node.val, path)
            path.pop()

        visit(root, targetSum, [])
        return paths

