from __future__ import annotations


class Solution:
    def findStrobogrammatic(self, n: int) -> list[str]:
        pairs = (("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6"))

        def build(length: int, outer_length: int) -> list[str]:
            if length == 0:
                return [""]
            if length == 1:
                return ["0", "1", "8"]
            result: list[str] = []
            for middle in build(length - 2, outer_length):
                for left, right in pairs:
                    if length == outer_length and left == "0":
                        continue
                    result.append(left + middle + right)
            return result

        return build(n, n)
