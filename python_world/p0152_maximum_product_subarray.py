class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        largest = smallest = answer = nums[0]
        for number in nums[1:]:
            if number < 0:
                largest, smallest = smallest, largest
            largest = max(number, largest * number)
            smallest = min(number, smallest * number)
            answer = max(answer, largest)
        return answer

