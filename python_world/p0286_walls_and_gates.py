from collections import deque


class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        if not rooms:
            return
        rows, columns = len(rooms), len(rooms[0])
        queue = deque((row, column) for row in range(rows) for column in range(columns)
                      if rooms[row][column] == 0)
        while queue:
            row, column = queue.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = row + dr, column + dc
                if 0 <= nr < rows and 0 <= nc < columns and rooms[nr][nc] == 2147483647:
                    rooms[nr][nc] = rooms[row][column] + 1
                    queue.append((nr, nc))
