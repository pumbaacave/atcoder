#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start


class Solution:
    def rob(self, nums: List[int]) -> int:
        # looks like DP?
        maximum: int = 0
        for i, num in enumerate(nums):
            if i < 2:
                maximum = max(maximum, num)
                # special case update local
                if i == 1:
                    nums[1] = maximum
                continue
            local_max = max(nums[i - 2] + num, nums[i - 1])
            nums[i] = local_max
            maximum = max(maximum, local_max)
        return maximum

# @lc code=end
