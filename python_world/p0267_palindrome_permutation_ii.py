from __future__ import annotations

from collections import Counter


class Solution:
    def generatePalindromes(self, s: str) -> list[str]:
        counts = Counter(s)
        odd = [character for character, count in counts.items() if count % 2]
        if len(odd) > 1:
            return []
        middle = odd[0] if odd else ""
        half_counts = {character: count // 2 for character, count in counts.items()}
        half_length = len(s) // 2
        result: list[str] = []

        def build(path: list[str]) -> None:
            if len(path) == half_length:
                half = "".join(path)
                result.append(half + middle + half[::-1])
                return
            for character in sorted(half_counts):
                if half_counts[character] == 0:
                    continue
                half_counts[character] -= 1
                path.append(character)
                build(path)
                path.pop()
                half_counts[character] += 1

        build([])
        return result
