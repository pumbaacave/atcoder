#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx/description/
#
# algorithms
# Easy (37.06%)
# Likes:    5221
# Dislikes: 3671
# Total Accepted:    1.3M
# Total Submissions: 3.4M
# Testcase Example:  '4'
#
# Given a non-negative integer x, return the square root of x rounded down to
# the nearest integer. The returned integer should be non-negative as well.
#
# You must not use any built-in exponent function or operator.
#
#
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
#
#
#
# Example 1:
#
#
# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.
#
#
# Example 2:
#
#
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down
# to the nearest integer, 2 is returned.
#
#
#
# Constraints:
#
#
# 0 <= x <= 2^31 - 1
#
#
#

# @lc code=start


class Solution:
    def mySqrt(self, x: int) -> int:
        self.target = x
        # binary search
        l, r = 0, x
        while True:
            mid = (l + r) // 2
            next = self.test(mid)
            if next == 0:
                return mid
            if next > 0:
                l = mid + 1
            else:
                r = mid - 1

    """
    return status code

    0: found match
    1: found right next
    -1: found left next
    """

    def test(self, num) -> int:
        lt = num * num <= self.target
        gt = self.target < (num + 1) * (num + 1)
        return 0 if (lt and gt) else 1 if lt else -1

# @lc code=end
