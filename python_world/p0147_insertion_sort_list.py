from __future__ import annotations

from .structures import ListNode


class Solution:
    def insertionSortList(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        while head:
            following = head.next
            position = dummy
            while position.next and position.next.val <= head.val:
                position = position.next
            head.next = position.next
            position.next = head
            head = following
        return dummy.next

