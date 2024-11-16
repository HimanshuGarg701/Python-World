from collections import defaultdict
from math import gcd


class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        best = 0
        for first in range(len(points)):
            slopes: dict[tuple[int, int], int] = defaultdict(int)
            duplicates = 1
            for second in range(first + 1, len(points)):
                dx = points[second][0] - points[first][0]
                dy = points[second][1] - points[first][1]
                if dx == 0 and dy == 0:
                    duplicates += 1
                    continue
                divisor = gcd(dx, dy)
                dx, dy = dx // divisor, dy // divisor
                if dx < 0 or (dx == 0 and dy < 0):
                    dx, dy = -dx, -dy
                slopes[(dy, dx)] += 1
            best = max(best, duplicates + max(slopes.values(), default=0))
        return best
