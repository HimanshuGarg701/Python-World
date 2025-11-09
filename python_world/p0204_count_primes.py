class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        prime = bytearray(b"\x01") * n
        prime[0:2] = b"\x00\x00"
        limit = int(n**0.5) + 1
        for value in range(2, limit):
            if prime[value]:
                start = value * value
                prime[start:n:value] = b"\x00" * (((n - 1 - start) // value) + 1)
        return sum(prime)
