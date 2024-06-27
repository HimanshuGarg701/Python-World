from collections import deque


class Solution:
    def __init__(self) -> None:
        self.pending: deque[str] = deque()

    def read4(self, buffer: list[str]) -> int:
        """Provided by LeetCode; subclasses can supply it for local tests."""
        raise NotImplementedError

    def read(self, buffer: list[str], n: int) -> int:
        written = 0
        while written < n:
            if not self.pending:
                temporary = [""] * 4
                count = self.read4(temporary)
                self.pending.extend(temporary[:count])
                if count == 0:
                    break
            buffer[written] = self.pending.popleft()
            written += 1
        return written

