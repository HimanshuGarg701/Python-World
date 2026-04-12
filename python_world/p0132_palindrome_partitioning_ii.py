class Solution:
    def minCut(self, text: str) -> int:
        cuts = list(range(-1, len(text)))
        for center in range(len(text)):
            left = right = center
            while left >= 0 and right < len(text) and text[left] == text[right]:
                cuts[right + 1] = min(cuts[right + 1], cuts[left] + 1)
                left -= 1
                right += 1
            left, right = center - 1, center
            while left >= 0 and right < len(text) and text[left] == text[right]:
                cuts[right + 1] = min(cuts[right + 1], cuts[left] + 1)
                left -= 1
                right += 1
        return cuts[-1]

