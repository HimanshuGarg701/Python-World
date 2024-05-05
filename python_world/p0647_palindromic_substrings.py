class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0

        def expand(left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        for center in range(len(s)):
            total += expand(center, center)
            total += expand(center, center + 1)
        return total
