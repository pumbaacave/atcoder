#
# @lc app=leetcode id=1685 lang=python3
#
# [1685] Sum of Absolute Differences in a Sorted Array
#

# @lc code=start


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        # calculate total diff with lhs and total diff with rhs
        total_diff_lhs = 0
        total_diff_rhs = 0
        left = [0] * len(nums)
        right = [0] * len(nums)
        n = len(nums) - 1
        for i in range(len(nums)):
            if i == 0:
                continue
            left[i] = (nums[i] - nums[i-1]) * i + left[i-1]
            right[n-i] = abs(nums[n-i] - nums[n-i+1]) * i + right[n-i+1]
        return list(left[i] + right[i] for i in range(len(nums)))

# @lc code=end
