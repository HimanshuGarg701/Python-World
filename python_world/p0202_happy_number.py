class Solution:
    def isHappy(self, n: int) -> bool:
        def next_value(value: int) -> int:
            total = 0
            while value:
                value, digit = divmod(value, 10)
                total += digit * digit
            return total

        slow = n
        fast = next_value(n)
        while fast != 1 and slow != fast:
            slow = next_value(slow)
            fast = next_value(next_value(fast))
        return fast == 1
