from functools import lru_cache


class Solution:
    def canWin(self, currentState: str) -> bool:
        @lru_cache(maxsize=None)
        def winning(state: str) -> bool:
            for index in range(len(state) - 1):
                if state[index:index + 2] == "++":
                    next_state = state[:index] + "--" + state[index + 2:]
                    if not winning(next_state):
                        return True
            return False

        return winning(currentState)
