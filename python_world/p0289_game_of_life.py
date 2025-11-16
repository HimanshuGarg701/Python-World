class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        rows, columns = len(board), len(board[0])
        for row in range(rows):
            for column in range(columns):
                live = 0
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        if dr == dc == 0:
                            continue
                        nr, nc = row + dr, column + dc
                        if 0 <= nr < rows and 0 <= nc < columns and board[nr][nc] & 1:
                            live += 1
                if live == 3 or (live == 2 and board[row][column] & 1):
                    board[row][column] |= 2
        for row in range(rows):
            for column in range(columns):
                board[row][column] >>= 1
