class Solution:
    def judgeCircle(self, moves: str) -> bool:
        horizontal = moves.count("R") - moves.count("L")
        vertical = moves.count("U") - moves.count("D")
        return horizontal == 0 and vertical == 0
