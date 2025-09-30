from functools import lru_cache


class Solution:
    def wordBreak(self, text: str, wordDict: list[str]) -> list[str]:
        words = set(wordDict)

        @lru_cache(None)
        def sentences(start: int) -> tuple[str, ...]:
            if start == len(text):
                return ("",)
            result: list[str] = []
            for end in range(start + 1, len(text) + 1):
                word = text[start:end]
                if word in words:
                    result.extend(word if not suffix else f"{word} {suffix}" for suffix in sentences(end))
            return tuple(result)

        return list(sentences(0))
