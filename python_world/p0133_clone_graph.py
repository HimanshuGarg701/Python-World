from __future__ import annotations

from .structures import GraphNode


class Solution:
    def cloneGraph(self, node: GraphNode | None) -> GraphNode | None:
        copies: dict[GraphNode, GraphNode] = {}

        def clone(original: GraphNode | None) -> GraphNode | None:
            if original is None:
                return None
            if original in copies:
                return copies[original]
            copy = GraphNode(original.val)
            copies[original] = copy
            copy.neighbors = [clone(neighbor) for neighbor in original.neighbors]
            return copy

        return clone(node)

