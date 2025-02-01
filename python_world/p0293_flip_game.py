class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> list[str]:
        return [
            currentState[:index] + "--" + currentState[index + 2:]
            for index in range(len(currentState) - 1)
            if currentState[index:index + 2] == "++"
        ]
