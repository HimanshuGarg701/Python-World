from collections import deque


class MyStack:
    def __init__(self) -> None:
        self.values: deque[int] = deque()

    def push(self, x: int) -> None:
        self.values.append(x)
        self.values.rotate(1)

    def pop(self) -> int:
        return self.values.popleft()

    def top(self) -> int:
        return self.values[0]

    def empty(self) -> bool:
        return not self.values
