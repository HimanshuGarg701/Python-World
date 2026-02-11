class Solution:
    def wordBreak(self, text: str, wordDict: list[str]) -> bool:
        words = set(wordDict)
        possible = [False] * (len(text) + 1)
        possible[0] = True
        longest = max(map(len, words), default=0)
        for end in range(1, len(text) + 1):
            possible[end] = any(
                possible[start] and text[start:end] in words
                for start in range(max(0, end - longest), end)
            )
        return possible[-1]

