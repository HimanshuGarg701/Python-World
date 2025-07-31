from __future__ import annotations


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        two = three = five = 0
        while len(ugly) < n:
            candidate = min(ugly[two] * 2, ugly[three] * 3, ugly[five] * 5)
            ugly.append(candidate)
            while ugly[two] * 2 <= candidate:
                two += 1
            while ugly[three] * 3 <= candidate:
                three += 1
            while ugly[five] * 5 <= candidate:
                five += 1
        return ugly[-1]
