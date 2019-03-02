"""
use binary search
num_mid numbers of both array can form a set
if idx = i in nums1 in set, than idx = j = num_mid - i in nums2
"""
from typing import *
import bisect
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        find least mid - 1 numbers
        than return median
        """
        L1 = len(nums1)
        L2 = len(nums2)
        mid = (L1 + L2) // 2
        # either one can be []
        if not L1 and not L2:
            return 0

        if not nums1:
            return self.kth(nums1, nums2, mid)
        elif not nums2:
            return self.kth(nums2, nums1, mid)

        if not nums1 or nums1[-1] <= nums2[0]:
            return self.kth(nums1, nums2, mid)
        elif not nums2 or nums2[-1] <= nums1[0]:
            return self.kth(nums2, nums1, mid)
        l1, l2 = 0, 0

        num_tar = mid if (L1 + L2) & 1 == 1 else mid - 1
        while l1 + l2 != num_tar:
            num_can = l1 + l2
            if num_can < num_tar:
                delta = num_tar - num_can
                # if traverse to nums1 last number, find in nums2 pls
                # but dont want to change find logic
                # so replace with large value to short cut
                # but L1 == 1 will bug
                # so escape
                if l1 == L1 - 1 and L1 > 1:
                    nums1[l1] = 1 << 20
                    l2 = num_tar - L1
                    break
                elif l2 == L2 - 1 and L2 > 1:
                    nums2[l2] = 1 << 20
                    l1 = num_tar - L2
                    break
                # extend TODO: what if l1 > L1
                elif nums1[l1] <= nums2[l2] or l2 == L2 - 1:
                    # extend from nums1
                    temp_l1 = l1 +min(delta, (L1 - l1) // 2)
                    l1 = min(temp_l1, L1 - 1)
                else:
                    # extend from nums2
                    temp_l2 = l2 + min(delta, (L2 - l2) // 2)
                    l2 = min(temp_l2, L2 -1)
            else:
                # shrink
                if nums1[l1] <= num2[l2]:
                    l2 = l2 // 2
                else:
                    l1 = l1 // 2
        LARGE = 1 << 20
        nums1.extend([LARGE, LARGE])
        nums2.extend([LARGE, LARGE])
        print("l1:", l1)
        print("l2", l2)
        if (L1 + L2) & 1 == 1:
            return min( nums1[l1], nums2[l2] )
        else:
            a = nums1[l1] + nums2[l2]
            b = nums1[l1] + nums1[l1 + 1]
            c = nums2[l2] + nums2[l2 + 1]
            return min(a, b, c) / 2

    def kth(self, nums1, nums2, kth):
        L1 = len(nums1)
        L2 = len(nums2)
        mid = kth
        is_odd = (L1 + L2) & 1 == 1
        total = nums1 + nums2
        if is_odd:
            return total[mid]
        elif not is_odd:
            return (total[mid - 1] + total[mid]) / 2


def test_neg():
    s = Solution()
    nums1 = [1, 2]
    nums2 = [1, 2, 3]
    assert s.findMedianSortedArrays(nums1, nums2) == 2.0
def test_empty2():
    s = Solution()
    nums1 = [1, 2, 3, 4, 5]
    nums2 = []
    assert s.findMedianSortedArrays(nums1, nums2) == 3
def test_1_lt_2():
    s = Solution()
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [6]
    assert s.findMedianSortedArrays(nums1, nums2) == 3.5
    s = Solution()
    nums1 = [1, 2, 3, 4]
    nums2 = [6]
    assert s.findMedianSortedArrays(nums1, nums2) == 3

def test_2_lt_1():
    s = Solution()
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [6]
    assert s.findMedianSortedArrays(nums2, nums1) == 3.5
    s = Solution()
    nums1 = [1, 2, 3, 4]
    nums2 = [6]
    assert s.findMedianSortedArrays(nums2, nums1) == 3

def test_odd():
    s = Solution()
    nums1 = [1, 3]
    nums2 = [2]
    assert s.findMedianSortedArrays(nums1, nums2) == 2.0

def test_even():
    s = Solution()
    nums1 = [1, 3]
    nums2 = [2, 4]
    assert s.findMedianSortedArrays(nums1, nums2) == 2.5

def test_skew():
    s = Solution()
    nums1 = [1, 3]
    nums2 = [2, 4, 6, 8, 10, 12, 14, 16]
    assert s.findMedianSortedArrays(nums1, nums2) == 7
