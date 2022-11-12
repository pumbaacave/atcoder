#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#

# @lc code=start


class Solution:
    def grayCode(self, n: int) -> List[int]:
        ret = [0]
        for i in range(n):
            front = ret
            offset = 2 ** i
            back = [num + offset for num in reversed(ret)]
            ret = front + back
        return ret


# @lc code=end
