from __future__ import annotations

from python_world.structures import TreeNode


class Solution:
    def longestConsecutive(self, root: TreeNode | None) -> int:
        answer = 0

        def visit(node: TreeNode | None, parent_value: int, length: int) -> None:
            nonlocal answer
            if node is None:
                return
            current = length + 1 if node.val == parent_value + 1 else 1
            answer = max(answer, current)
            visit(node.left, node.val, current)
            visit(node.right, node.val, current)

        if root:
            visit(root, root.val - 1, 0)
        return answer
