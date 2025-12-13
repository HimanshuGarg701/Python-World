class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        forward: dict[str, str] = {}
        reverse: dict[str, str] = {}
        for first, second in zip(s, t):
            if forward.get(first, second) != second or reverse.get(second, first) != first:
                return False
            forward[first] = second
            reverse[second] = first
        return True
