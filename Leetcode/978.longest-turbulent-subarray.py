#
# @lc app=leetcode id=978 lang=python3
#
# [978] Longest Turbulent Subarray
#

# @lc code=start


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        max_lenth = 1
        if len(arr) == 1:
            return 1
        if not arr:
            return 0
        l, r = 0, 1
        next_bigger = True
        while r < len(arr):
            if arr[r] == arr[r-1]:
                l = r
                next_bigger = True
            # turbulent maintained
            elif arr[r] > arr[r-1] and next_bigger or arr[r] < arr[r-1] and \
                    (not next_bigger):
                max_lenth = max(max_lenth, r - l + 1)
                next_bigger = not next_bigger
            else:
                # wrong guess but not equal for r and r - 1
                l = r - 1
                max_lenth = max(max_lenth, 2)
                # next_bigger = not next_bigger
            r += 1
        return max_lenth


# @lc code=end
