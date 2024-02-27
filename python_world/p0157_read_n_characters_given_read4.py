class Solution:
    def read4(self, buffer: list[str]) -> int:
        """Provided by LeetCode; subclasses can supply it for local tests."""
        raise NotImplementedError

    def read(self, buffer: list[str], n: int) -> int:
        written = 0
        temporary = [""] * 4
        while written < n:
            count = self.read4(temporary)
            if count == 0:
                break
            copied = min(count, n - written)
            buffer[written : written + copied] = temporary[:copied]
            written += copied
        return written

