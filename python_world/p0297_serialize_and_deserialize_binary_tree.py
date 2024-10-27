from __future__ import annotations

from collections import deque

from python_world.structures import TreeNode


class Codec:
    def serialize(self, root: TreeNode | None) -> str:
        values: list[str] = []

        def visit(node: TreeNode | None) -> None:
            if node is None:
                values.append("#")
                return
            values.append(str(node.val))
            visit(node.left)
            visit(node.right)

        visit(root)
        return ",".join(values)

    def deserialize(self, data: str) -> TreeNode | None:
        values = deque(data.split(","))

        def build() -> TreeNode | None:
            value = values.popleft()
            if value == "#":
                return None
            node = TreeNode(int(value))
            node.left = build()
            node.right = build()
            return node

        return build()
