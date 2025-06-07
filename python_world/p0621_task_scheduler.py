from collections import Counter


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        frequencies = Counter(tasks).values()
        highest = max(frequencies)
        highest_count = sum(count == highest for count in frequencies)
        frame = (highest - 1) * (n + 1) + highest_count
        return max(len(tasks), frame)
