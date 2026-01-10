class Solution:
    def reverseWords(self, characters: list[str]) -> None:
        self._reverse(characters, 0, len(characters) - 1)
        start = 0
        for end in range(len(characters) + 1):
            if end == len(characters) or characters[end] == " ":
                self._reverse(characters, start, end - 1)
                start = end + 1

    def _reverse(self, characters: list[str], left: int, right: int) -> None:
        while left < right:
            characters[left], characters[right] = characters[right], characters[left]
            left += 1
            right -= 1

