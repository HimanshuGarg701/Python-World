from collections import deque


class Solution:
    def solve(self, board: list[list[str]]) -> None:
        if not board:
            return
        rows, columns = len(board), len(board[0])
        queue = deque()
        for row in range(rows):
            queue.extend((row, column) for column in (0, columns - 1) if board[row][column] == "O")
        for column in range(columns):
            queue.extend((row, column) for row in (0, rows - 1) if board[row][column] == "O")
        while queue:
            row, column = queue.popleft()
            if not (0 <= row < rows and 0 <= column < columns) or board[row][column] != "O":
                continue
            board[row][column] = "E"
            queue.extend(((row + 1, column), (row - 1, column), (row, column + 1), (row, column - 1)))
        for row in range(rows):
            for column in range(columns):
                board[row][column] = "O" if board[row][column] == "E" else "X"

