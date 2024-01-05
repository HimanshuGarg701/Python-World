from __future__ import annotations


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None) -> None:
        self.val = val
        self.next = next


class NextTreeNode:
    def __init__(
        self,
        val: int = 0,
        left: NextTreeNode | None = None,
        right: NextTreeNode | None = None,
        next: NextTreeNode | None = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class GraphNode:
    def __init__(self, val: int = 0, neighbors: list[GraphNode] | None = None) -> None:
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class RandomNode:
    def __init__(
        self,
        val: int = 0,
        next: RandomNode | None = None,
        random: RandomNode | None = None,
    ) -> None:
        self.val = val
        self.next = next
        self.random = random
