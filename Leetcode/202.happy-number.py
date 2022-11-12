#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start


class Solution:
    def isHappy(self, n: int) -> bool:
        self.seen = set()
        while True:
            ret = self.check(n)
            if ret == 1:
                return True
            if ret in self.seen:
                return False
            self.seen.add(ret)
            n = ret

    def check(self, num):
        ret = 0
        while (num > 9):
            a, b = divmod(num, 10)
            ret += b * b
            num = a
        else:
            ret += num * num
        return ret


# @lc code=end
