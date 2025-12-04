class Solution:
    def findMissingRanges(self, nums: list[int], lower: int, upper: int) -> list[str]:
        result: list[str] = []
        previous = lower - 1
        for current in nums + [upper + 1]:
            if current - previous >= 2:
                start, end = previous + 1, current - 1
                result.append(str(start) if start == end else f"{start}->{end}")
            previous = current
        return result

