class Solution:
    def isPalindrome(self, text: str) -> bool:
        left, right = 0, len(text) - 1
        while left < right:
            while left < right and not text[left].isalnum():
                left += 1
            while left < right and not text[right].isalnum():
                right -= 1
            if text[left].casefold() != text[right].casefold():
                return False
            left += 1
            right -= 1
        return True

