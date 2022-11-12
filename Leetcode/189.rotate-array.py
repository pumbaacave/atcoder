#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # O(1) method
        # use xor property to hold 2 number in one slot
        # and cancel old number later
        n = len(nums)
        k = k % n
        buffer = list(nums[n-k:])
        for i in reversed(range(n - k)):
            nums[i + k] = nums[i]
        for i in range(k):
            nums[i] = buffer[i]

# @lc code=end
