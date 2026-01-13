from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = sum(first == second for first, second in zip(secret, guess))
        shared = sum((Counter(secret) & Counter(guess)).values())
        return f"{bulls}A{shared - bulls}B"
