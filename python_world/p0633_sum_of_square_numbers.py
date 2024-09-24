from math import isqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, isqrt(c)
        while left <= right:
            total = left * left + right * right
            if total == c:
                return True
            if total < c:
                left += 1
            else:
                right -= 1
        return False
