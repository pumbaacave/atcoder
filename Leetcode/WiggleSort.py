class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L = len(nums)
        def helper(start, end):
            if end >= L:
                if L - start == 1:
                    return
                elif L - start == 2:
                    # out of order
                    if nums[start] > nums[-1]:
                        nums[start], nums[-1] = nums[-1], nums[start]
            else:
                # wiggle sort 3 numbers
                swap_idx = start
                for idx in range(start+1, start+3):
                    if nums[idx] > nums[swap_idx]:
                        swap_idx = idx
                nums[start+1], nums[swap_idx] = nums[swap_idx], nums[start+1]
        for i in range(0, L, 2):
            start, end = i, i + 2
            helper(start, end)
