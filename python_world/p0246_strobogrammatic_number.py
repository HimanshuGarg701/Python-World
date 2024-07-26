from __future__ import annotations


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotations = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        left, right = 0, len(num) - 1
        while left <= right:
            if num[left] not in rotations or rotations[num[left]] != num[right]:
                return False
            left += 1
            right -= 1
        return True
