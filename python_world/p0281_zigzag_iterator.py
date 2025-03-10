from __future__ import annotations

from collections import deque
from collections.abc import Iterator


class ZigzagIterator:
    def __init__(self, v1: list[int], v2: list[int]) -> None:
        self.queue: deque[Iterator[int]] = deque(iter(values) for values in (v1, v2) if values)

    def next(self) -> int:
        iterator = self.queue.popleft()
        value = next(iterator)
        try:
            following = next(iterator)
        except StopIteration:
            return value
        self.queue.append(_PrefetchedIterator(following, iterator))
        return value

    def hasNext(self) -> bool:
        return bool(self.queue)


class _PrefetchedIterator:
    def __init__(self, first: int, remaining: Iterator[int]) -> None:
        self.first = first
        self.remaining = remaining
        self.pending = True

    def __iter__(self) -> _PrefetchedIterator:
        return self

    def __next__(self) -> int:
        if self.pending:
            self.pending = False
            return self.first
        return next(self.remaining)
