from __future__ import annotations

from .structures import ListNode


class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        if not head or not head.next:
            return True
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second = self._reverse(slow.next)
        slow.next = second
        first, cursor = head, second
        palindrome = True
        while cursor:
            if first.val != cursor.val:
                palindrome = False
                break
            first = first.next
            cursor = cursor.next
        slow.next = self._reverse(second)
        return palindrome

    def _reverse(self, node: ListNode | None) -> ListNode | None:
        previous = None
        while node:
            following = node.next
            node.next = previous
            previous = node
            node = following
        return previous
