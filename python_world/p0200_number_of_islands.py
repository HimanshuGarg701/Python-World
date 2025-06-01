class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        rows, columns = len(grid), len(grid[0])

        def sink(start_row: int, start_column: int) -> None:
            stack = [(start_row, start_column)]
            grid[start_row][start_column] = "0"
            while stack:
                row, column = stack.pop()
                for neighbor_row, neighbor_column in (
                    (row + 1, column),
                    (row - 1, column),
                    (row, column + 1),
                    (row, column - 1),
                ):
                    if (
                        0 <= neighbor_row < rows
                        and 0 <= neighbor_column < columns
                        and grid[neighbor_row][neighbor_column] == "1"
                    ):
                        grid[neighbor_row][neighbor_column] = "0"
                        stack.append((neighbor_row, neighbor_column))

        islands = 0
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == "1":
                    islands += 1
                    sink(row, column)
        return islands
