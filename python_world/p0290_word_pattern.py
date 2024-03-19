class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        forward: dict[str, str] = {}
        reverse: dict[str, str] = {}
        for letter, word in zip(pattern, words):
            if forward.get(letter, word) != word or reverse.get(word, letter) != letter:
                return False
            forward[letter] = word
            reverse[word] = letter
        return True
