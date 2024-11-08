class Solution:
    def findRepeatedDnaSequences(self, text: str) -> list[str]:
        seen: set[str] = set()
        repeated: set[str] = set()
        for start in range(len(text) - 9):
            sequence = text[start : start + 10]
            if sequence in seen:
                repeated.add(sequence)
            else:
                seen.add(sequence)
        return list(repeated)

