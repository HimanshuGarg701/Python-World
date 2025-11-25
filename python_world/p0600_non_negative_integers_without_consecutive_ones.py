class Solution:
    def findIntegers(self, n: int) -> int:
        ways = [0] * 32
        ways[0], ways[1] = 1, 2
        for bit in range(2, len(ways)):
            ways[bit] = ways[bit - 1] + ways[bit - 2]

        answer = 0
        previous_bit = 0
        for bit in range(30, -1, -1):
            if n & (1 << bit):
                answer += ways[bit]
                if previous_bit:
                    return answer
                previous_bit = 1
            else:
                previous_bit = 0
        return answer + 1
