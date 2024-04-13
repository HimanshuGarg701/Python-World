from __future__ import annotations

from .structures import NextTreeNode


class Solution:
    def connect(self, root: NextTreeNode | None) -> NextTreeNode | None:
        level = root
        while level:
            dummy = NextTreeNode()
            tail = dummy
            current = level
            while current:
                if current.left:
                    tail.next = current.left
                    tail = tail.next
                if current.right:
                    tail.next = current.right
                    tail = tail.next
                current = current.next
            level = dummy.next
        return root

