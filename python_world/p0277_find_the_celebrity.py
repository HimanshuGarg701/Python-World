from __future__ import annotations


class Solution:
    def knows(self, first: int, second: int) -> bool:
        raise NotImplementedError("LeetCode supplies the knows API")

    def findCelebrity(self, n: int) -> int:
        candidate = 0
        for person in range(1, n):
            if self.knows(candidate, person):
                candidate = person
        for person in range(n):
            if person == candidate:
                continue
            if self.knows(candidate, person) or not self.knows(person, candidate):
                return -1
        return candidate
