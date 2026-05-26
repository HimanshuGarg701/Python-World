from __future__ import annotations


class MyQueue:
    def __init__(self) -> None:
        self._incoming: list[int] = []
        self._outgoing: list[int] = []

    def push(self, x: int) -> None:
        self._incoming.append(x)

    def pop(self) -> int:
        self._prepare_outgoing()
        return self._outgoing.pop()

    def peek(self) -> int:
        self._prepare_outgoing()
        return self._outgoing[-1]

    def empty(self) -> bool:
        return not self._incoming and not self._outgoing

    def _prepare_outgoing(self) -> None:
        if not self._outgoing:
            while self._incoming:
                self._outgoing.append(self._incoming.pop())
