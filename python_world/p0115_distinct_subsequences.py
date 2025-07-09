class Solution:
    def numDistinct(self, source: str, target: str) -> int:
        counts = [0] * (len(target) + 1)
        counts[0] = 1
        for source_character in source:
            for index in range(len(target) - 1, -1, -1):
                if source_character == target[index]:
                    counts[index + 1] += counts[index]
        return counts[-1]

