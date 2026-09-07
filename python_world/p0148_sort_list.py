from __future__ import annotations

from .structures import ListNode


class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        right = slow.next
        slow.next = None
        return self._merge(self.sortList(head), self.sortList(right))

    def _merge(self, left: ListNode | None, right: ListNode | None) -> ListNode | None:
        dummy = tail = ListNode()
        while left and right:
            if left.val <= right.val:
                tail.next, left = left, left.next
            else:
                tail.next, right = right, right.next
            tail = tail.next
        tail.next = left or right
        return dummy.next

