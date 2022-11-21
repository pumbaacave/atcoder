#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#

# @lc code=start


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # sortedset?
        # many great edge cases :)
        if len(nums) < 3:
            return max(nums)
        m1, m2, m3 = list(reversed(sorted(nums[:3])))
        for n in nums:
            # dedup
            if n in (m1, m2, m3):
                continue
            if m1 == m2:
                m2 = n
                m1, m2, m3 = reversed(sorted((m1, m2, m3)))
                continue
            if m2 == m3:
                m2 = n
                m1, m2, m3 = reversed(sorted((m1, m2, m3)))
                continue
            if n > m1:
                m1, m2, m3 = n, m1, m2
            elif n > m2:
                m1, m2, m3 = m1, n, m2
            elif n > m3:
                m1, m2, m3 = m1, m2, n
        if len(set((m1, m2, m3))) < 3:
            return max(m1, m2, m3)
        else:
            return list(reversed(sorted((m1, m2, m3))))[2]


# @lc code=end
