from __future__ import annotations

from collections import defaultdict


class Solution:
    def groupStrings(self, strings: list[str]) -> list[list[str]]:
        groups: dict[tuple[int, ...], list[str]] = defaultdict(list)
        for string in strings:
            key = tuple(
                (ord(string[index]) - ord(string[index - 1])) % 26
                for index in range(1, len(string))
            )
            groups[key].append(string)
        return list(groups.values())
