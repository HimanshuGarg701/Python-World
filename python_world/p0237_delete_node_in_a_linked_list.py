from __future__ import annotations

from .structures import ListNode


class Solution:
    def deleteNode(self, node: ListNode) -> None:
        if node.next is None:
            raise ValueError("the tail node cannot be deleted with this operation")
        node.val = node.next.val
        node.next = node.next.next
