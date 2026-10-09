from __future__ import annotations

from .structures import ListNode, TreeNode


class Solution:
    def sortedListToBST(self, head: ListNode | None) -> TreeNode | None:
        def build(start: ListNode | None, end: ListNode | None) -> TreeNode | None:
            if start is end:
                return None
            slow = fast = start
            while fast is not end and fast.next is not end:
                slow = slow.next
                fast = fast.next.next
            assert slow is not None
            return TreeNode(slow.val, build(start, slow), build(slow.next, end))

        return build(head, None)

