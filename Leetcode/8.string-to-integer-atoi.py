#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start


class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        s = s.strip()
        if not s:
            return 0
        idx = 0
        sign = 1
        if s[0] in ('+', '-'):
            sign = 1 if s[0] == '+' else -1
            idx += 1
        od_0 = ord('0')
        ret = 0
        while idx < len(s):
            if od_0 <= ord(s[idx]) < od_0 + 10:
                ret *= 10
                ret += (ord(s[idx]) - od_0)
                idx += 1
            else:
                break
        # handle overflow, to reduce memory consumption
        # better cutout whole needed string and parse from tail to stop erlear.
        MASK = 1 << 31
        if sign < 0 and ret >= MASK:
            return sign * MASK
        if sign > 0 and ret >= MASK - 1:
            return MASK - 1
        return sign * ret


# @lc code=end
