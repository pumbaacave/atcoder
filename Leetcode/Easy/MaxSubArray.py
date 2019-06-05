class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -float('inf')
        running_sum = 0
        for num in nums:
            running_sum = max(num, running_sum + num)
            max_sum = max(max_sum, running_sum)
        return max_sum
