class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        swap_idx = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            nums[i], nums[swap_idx] = nums[swap_idx], nums[i]
            swap_idx += 1
