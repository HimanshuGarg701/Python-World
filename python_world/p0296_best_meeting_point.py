class Solution:
    def minTotalDistance(self, grid: list[list[int]]) -> int:
        rows = [row for row in range(len(grid)) for value in grid[row] if value == 1]
        columns = sorted(
            column for row in grid for column, value in enumerate(row) if value == 1
        )
        row_median = rows[len(rows) // 2]
        column_median = columns[len(columns) // 2]
        return sum(abs(row - row_median) for row in rows) + sum(
            abs(column - column_median) for column in columns
        )
