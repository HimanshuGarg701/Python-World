class Solution:
    def reverseWords(self, text: str) -> str:
        return " ".join(reversed(text.split()))

