from itertools import zip_longest


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        first = map(int, version1.split("."))
        second = map(int, version2.split("."))
        for left, right in zip_longest(first, second, fillvalue=0):
            if left != right:
                return 1 if left > right else -1
        return 0

