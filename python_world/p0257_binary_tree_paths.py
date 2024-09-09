from __future__ import annotations

from .structures import TreeNode


class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        paths: list[str] = []

        def visit(node: TreeNode | None, path: str) -> None:
            if node is None:
                return
            current = f"{path}->{node.val}" if path else str(node.val)
            if node.left is None and node.right is None:
                paths.append(current)
                return
            visit(node.left, current)
            visit(node.right, current)

        visit(root, "")
        return paths
