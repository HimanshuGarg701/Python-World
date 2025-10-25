from __future__ import annotations


class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        difference = 0
        for number in nums:
            difference ^= number
        distinguishing_bit = difference & -difference
        first = second = 0
        for number in nums:
            if number & distinguishing_bit:
                first ^= number
            else:
                second ^= number
        return [first, second]
