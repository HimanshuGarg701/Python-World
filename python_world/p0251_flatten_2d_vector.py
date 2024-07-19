from __future__ import annotations


class Vector2D:
    def __init__(self, vec: list[list[int]]):
        self._vector = vec
        self._row = 0
        self._column = 0

    def next(self) -> int:
        self._advance()
        value = self._vector[self._row][self._column]
        self._column += 1
        return value

    def hasNext(self) -> bool:
        self._advance()
        return self._row < len(self._vector)

    def _advance(self) -> None:
        while self._row < len(self._vector) and self._column == len(self._vector[self._row]):
            self._row += 1
            self._column = 0
