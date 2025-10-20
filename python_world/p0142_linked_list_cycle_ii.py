from __future__ import annotations

from .structures import ListNode


class Solution:
    def detectCycle(self, head: ListNode | None) -> ListNode | None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                seeker = head
                while seeker is not slow:
                    seeker = seeker.next
                    slow = slow.next
                return seeker
        return None

