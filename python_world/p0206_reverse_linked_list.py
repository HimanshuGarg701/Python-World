from __future__ import annotations

from python_world.structures import ListNode


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        previous = None
        while head:
            following = head.next
            head.next = previous
            previous = head
            head = following
        return previous
