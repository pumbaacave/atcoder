from math import log2
from functools import reduce
from operator import mul
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        old_nums = nums.copy()
        if nums.count(0) >= 2:
            return [0] * len(nums)
        # at most one 0 element
        zero_idx = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_idx = i
                continue
            nums[i] = log2(abs(nums[i]))
        total = sum(nums)
        sign = reduce(mul, old_nums) > 0

        if zero_idx > 0:
            res = [0] * len(nums)
            res[zero_idx] = round(2 ** total)
            return res
        for i in range(len(nums)):
            nums[i] = round(2 ** (total - nums[i]))
            if sign and old_nums[i] < 0 or (not sign and old_nums[i] > 0):
                nums[i] = -nums[i]
        return nums



