class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx = len(nums1) - 1
        i1, i2 = m - 1, n - 1
        while idx >= 0 and i1 >= 0 and i2 >= 0:
            if nums1[i1] <= nums2[i2]:
                nums1[idx], nums2[i2] = nums2[i2], nums1[idx]
                i2 -= 1
                idx -= 1
            else:
                nums1[idx], nums1[i1] = nums1[i1], nums1[idx]
                i1 -= 1
                idx -= 1
        while idx >= 0 and i1 >= 0:
            nums1[idx], nums1[i1] = nums1[i1], nums1[idx]
            i1 -= 1
            idx -= 1
        while idx >= 0 and i2 >= 0:
            nums1[idx], nums2[i2] = nums2[i2], nums1[idx]
            i2 -= 1
            idx -= 1

