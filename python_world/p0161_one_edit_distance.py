class Solution:
    def isOneEditDistance(self, first: str, second: str) -> bool:
        if len(first) > len(second):
            return self.isOneEditDistance(second, first)
        if len(second) - len(first) > 1:
            return False
        for index in range(len(first)):
            if first[index] != second[index]:
                if len(first) == len(second):
                    return first[index + 1 :] == second[index + 1 :]
                return first[index:] == second[index + 1 :]
        return len(second) == len(first) + 1

