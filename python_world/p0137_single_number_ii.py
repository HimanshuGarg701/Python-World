class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ones = twos = 0
        mask = 0xFFFFFFFF
        for number in nums:
            number &= mask
            ones = (ones ^ number) & ~twos & mask
            twos = (twos ^ number) & ~ones & mask
        return ones if ones < 1 << 31 else ones - (1 << 32)

