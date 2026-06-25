from __future__ import annotations

from .structures import NextTreeNode


class Solution:
    def connect(self, root: NextTreeNode | None) -> NextTreeNode | None:
        level = root
        while level and level.left:
            current = level
            while current:
                current.left.next = current.right
                if current.next:
                    current.right.next = current.next.left
                current = current.next
            level = level.left
        return root

