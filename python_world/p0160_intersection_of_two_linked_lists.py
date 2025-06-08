from __future__ import annotations

from .structures import ListNode


class Solution:
    def getIntersectionNode(
        self, headA: ListNode | None, headB: ListNode | None
    ) -> ListNode | None:
        first, second = headA, headB
        while first is not second:
            first = headB if first is None else first.next
            second = headA if second is None else second.next
        return first
