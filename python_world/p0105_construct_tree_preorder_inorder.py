from __future__ import annotations

from .structures import TreeNode


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        positions = {value: index for index, value in enumerate(inorder)}
        preorder_index = 0

        def build(left: int, right: int) -> TreeNode | None:
            nonlocal preorder_index
            if left > right:
                return None
            value = preorder[preorder_index]
            preorder_index += 1
            middle = positions[value]
            return TreeNode(value, build(left, middle - 1), build(middle + 1, right))

        return build(0, len(inorder) - 1)

