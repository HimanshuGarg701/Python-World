class Solution:
    def partition(self, text: str) -> list[list[str]]:
        result: list[list[str]] = []

        def search(start: int, parts: list[str]) -> None:
            if start == len(text):
                result.append(parts.copy())
                return
            for end in range(start + 1, len(text) + 1):
                piece = text[start:end]
                if piece == piece[::-1]:
                    parts.append(piece)
                    search(end, parts)
                    parts.pop()

        search(0, [])
        return result

