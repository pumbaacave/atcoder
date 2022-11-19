#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = Counter(p)
        ret = []
        len_p = len(p)
        if len(s) < len_p:
            return []
        cur = Counter(s[:len_p])
        if cur == target:
            ret.append(0)
        for i in range(1, len(s) - len_p + 1):
            # reuse counter is mem efficient
            # sliding window
            cur[s[i + len_p - 1]] += 1
            cur[s[i - 1]] -= 1
            if cur == target:
                ret.append(i)
        return ret

# @lc code=end
