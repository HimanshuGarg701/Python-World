from __future__ import annotations

from python_world.structures import TreeNode


class Solution:
    def tree2str(self, root: TreeNode | None) -> str:
        if root is None:
            return ""

        result = str(root.val)
        if root.left is not None or root.right is not None:
            result += f"({self.tree2str(root.left)})"
        if root.right is not None:
            result += f"({self.tree2str(root.right)})"
        return result
