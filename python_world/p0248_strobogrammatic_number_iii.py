from __future__ import annotations


class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        pairs = (("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6"))
        count = 0

        def build(characters: list[str], left: int, right: int) -> None:
            nonlocal count
            if left > right:
                candidate = "".join(characters)
                if len(candidate) == len(low) and candidate < low:
                    return
                if len(candidate) == len(high) and candidate > high:
                    return
                count += 1
                return
            for first, second in pairs:
                if left == 0 and len(characters) > 1 and first == "0":
                    continue
                if left == right and first != second:
                    continue
                characters[left], characters[right] = first, second
                build(characters, left + 1, right - 1)

        for length in range(len(low), len(high) + 1):
            build([""] * length, 0, length - 1)
        return count
