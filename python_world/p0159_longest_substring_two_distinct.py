from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, text: str) -> int:
        counts: dict[str, int] = defaultdict(int)
        left = best = 0
        for right, character in enumerate(text):
            counts[character] += 1
            while len(counts) > 2:
                old = text[left]
                counts[old] -= 1
                if counts[old] == 0:
                    del counts[old]
                left += 1
            best = max(best, right - left + 1)
        return best

