class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(m == n for i, m in enumerate(nums) for n in nums[i+1:])
