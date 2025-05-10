class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for character in columnTitle:
            result = result * 26 + ord(character) - ord("A") + 1
        return result

