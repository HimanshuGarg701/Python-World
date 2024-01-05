from __future__ import annotations


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        row, column = len(matrix) - 1, 0
        while row >= 0 and column < len(matrix[0]):
            if matrix[row][column] == target:
                return True
            if matrix[row][column] > target:
                row -= 1
            else:
                column += 1
        return False
