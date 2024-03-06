from __future__ import annotations

from .structures import RandomNode


class Solution:
    def copyRandomList(self, head: RandomNode | None) -> RandomNode | None:
        if head is None:
            return None
        current = head
        while current:
            current.next = RandomNode(current.val, current.next)
            current = current.next.next
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next
        copy_head = head.next
        current = head
        while current:
            copy = current.next
            current.next = copy.next
            copy.next = copy.next.next if copy.next else None
            current = current.next
        return copy_head

