from __future__ import annotations

from .structures import TreeNode


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        positions = {value: index for index, value in enumerate(inorder)}
        postorder_index = len(postorder) - 1

        def build(left: int, right: int) -> TreeNode | None:
            nonlocal postorder_index
            if left > right:
                return None
            value = postorder[postorder_index]
            postorder_index -= 1
            middle = positions[value]
            right_node = build(middle + 1, right)
            left_node = build(left, middle - 1)
            return TreeNode(value, left_node, right_node)

        return build(0, len(inorder) - 1)

