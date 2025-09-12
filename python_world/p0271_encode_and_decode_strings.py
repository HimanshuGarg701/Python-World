from __future__ import annotations


class Codec:
    def encode(self, strs: list[str]) -> str:
        return "".join(f"{len(string)}#{string}" for string in strs)

    def decode(self, s: str) -> list[str]:
        result: list[str] = []
        index = 0
        while index < len(s):
            separator = s.index("#", index)
            length = int(s[index:separator])
            start = separator + 1
            result.append(s[start : start + length])
            index = start + length
        return result
