class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return 0
        low, high = min(nums), max(nums)
        if low == high:
            return 0
        bucket_size = max(1, (high - low) // (len(nums) - 1))
        bucket_count = (high - low) // bucket_size + 1
        minima = [float("inf")] * bucket_count
        maxima = [float("-inf")] * bucket_count
        used = [False] * bucket_count
        for number in nums:
            bucket = (number - low) // bucket_size
            minima[bucket] = min(minima[bucket], number)
            maxima[bucket] = max(maxima[bucket], number)
            used[bucket] = True
        best, previous = 0, low
        for bucket in range(bucket_count):
            if used[bucket]:
                best = max(best, int(minima[bucket]) - previous)
                previous = int(maxima[bucket])
        return best

