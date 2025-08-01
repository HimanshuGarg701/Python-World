class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        seen: set[int] = set()
        duplicate = 0
        for number in nums:
            if number in seen:
                duplicate = number
            seen.add(number)

        expected = len(nums) * (len(nums) + 1) // 2
        missing = expected - sum(seen)
        return [duplicate, missing]
