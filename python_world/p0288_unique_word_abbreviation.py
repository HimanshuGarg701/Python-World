class ValidWordAbbr:
    def __init__(self, dictionary: list[str]) -> None:
        self.words: dict[str, set[str]] = {}
        for word in dictionary:
            self.words.setdefault(self._abbreviation(word), set()).add(word)

    def isUnique(self, word: str) -> bool:
        matches = self.words.get(self._abbreviation(word))
        return matches is None or matches == {word}

    def _abbreviation(self, word: str) -> str:
        if len(word) <= 2:
            return word
        return f"{word[0]}{len(word) - 2}{word[-1]}"
