from __future__ import annotations

from .structures import ListNode


class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        if head is None or head.next is None:
            return
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        previous = None
        while second:
            following = second.next
            second.next = previous
            previous = second
            second = following
        first, second = head, previous
        while second:
            next_first, next_second = first.next, second.next
            first.next = second
            second.next = next_first
            first, second = next_first, next_second

