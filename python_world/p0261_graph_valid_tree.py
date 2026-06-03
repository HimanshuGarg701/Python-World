from __future__ import annotations


class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        parent = list(range(n))
        size = [1] * n

        def find(node: int) -> int:
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        for first, second in edges:
            first_root, second_root = find(first), find(second)
            if first_root == second_root:
                return False
            if size[first_root] < size[second_root]:
                first_root, second_root = second_root, first_root
            parent[second_root] = first_root
            size[first_root] += size[second_root]
        return True
