#
# @lc app=leetcode id=396 lang=python3
#
# [396] Rotate Function
#

# @lc code=start


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # accumulative sum?
        total = sum(nums)
        # holding max to return as well
        F0 = sum(i * n for i, n in enumerate(nums))
        ret = F0
        N = len(nums)
        for r in reversed(nums):
            Fn = F0 + total - r * N
            ret = max(ret, Fn)
            #print(Fn, ret)
            F0 = Fn
        return ret

# @lc code=end
