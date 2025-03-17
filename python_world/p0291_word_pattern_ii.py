class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        mapping: dict[str, str] = {}
        used: set[str] = set()

        def search(pattern_index: int, text_index: int) -> bool:
            if pattern_index == len(pattern):
                return text_index == len(s)
            letter = pattern[pattern_index]
            if letter in mapping:
                value = mapping[letter]
                return s.startswith(value, text_index) and search(
                    pattern_index + 1, text_index + len(value)
                )
            remaining_letters = len(pattern) - pattern_index - 1
            for end in range(text_index + 1, len(s) - remaining_letters + 1):
                value = s[text_index:end]
                if value in used:
                    continue
                mapping[letter] = value
                used.add(value)
                if search(pattern_index + 1, end):
                    return True
                used.remove(value)
                del mapping[letter]
            return False

        return search(0, 0)
