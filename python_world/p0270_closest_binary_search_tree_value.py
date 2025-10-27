from __future__ import annotations

from .structures import TreeNode


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = root.val
        node: TreeNode | None = root
        while node:
            if abs(node.val - target) < abs(closest - target):
                closest = node.val
            node = node.left if target < node.val else node.right
        return closest
