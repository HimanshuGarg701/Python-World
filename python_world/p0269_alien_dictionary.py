from __future__ import annotations

import heapq


class Solution:
    def alienOrder(self, words: list[str]) -> str:
        graph = {character: set() for word in words for character in word}
        indegree = {character: 0 for character in graph}
        for first, second in zip(words, words[1:]):
            if len(first) > len(second) and first.startswith(second):
                return ""
            for before, after in zip(first, second):
                if before == after:
                    continue
                if after not in graph[before]:
                    graph[before].add(after)
                    indegree[after] += 1
                break
        ready = [character for character, degree in indegree.items() if degree == 0]
        heapq.heapify(ready)
        order: list[str] = []
        while ready:
            character = heapq.heappop(ready)
            order.append(character)
            for following in graph[character]:
                indegree[following] -= 1
                if indegree[following] == 0:
                    heapq.heappush(ready, following)
        return "".join(order) if len(order) == len(graph) else ""
