class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        if not matrix:
            return 0
        dp = [0] * (len(matrix[0]) + 1)
        largest = 0
        for row in matrix:
            diagonal = 0
            for column, value in enumerate(row, 1):
                above = dp[column]
                if value == "1":
                    dp[column] = 1 + min(dp[column], dp[column - 1], diagonal)
                    largest = max(largest, dp[column])
                else:
                    dp[column] = 0
                diagonal = above
        return largest * largest
