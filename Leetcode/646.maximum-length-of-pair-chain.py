#
# @lc app=leetcode id=646 lang=python3
#
# [646] Maximum Length of Pair Chain
#

# @lc code=start


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # smallest tail pair fisrt
        pairs = sorted(pairs, key=lambda x: x[1])
        # print(pairs)
        cnt = 1
        pre = pairs[0]
        for p in pairs[1:]:
            # can chain
            if pre[1] < p[0]:
                cnt += 1
                pre = p
        return cnt

# @lc code=end
