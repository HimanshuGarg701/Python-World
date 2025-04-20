class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_value = 0
        for _ in range(32):
            reversed_value = (reversed_value << 1) | (n & 1)
            n >>= 1
        return reversed_value

