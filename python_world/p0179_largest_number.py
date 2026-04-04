from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        values = list(map(str, nums))

        def compare(first: str, second: str) -> int:
            return -1 if first + second > second + first else (first + second < second + first)

        result = "".join(sorted(values, key=cmp_to_key(compare)))
        return "0" if result[0] == "0" else result

