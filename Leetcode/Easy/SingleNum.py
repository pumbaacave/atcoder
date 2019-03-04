class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #  nums is non-empty
        res = 0
        for num in nums:
            res ^= num
        return res
