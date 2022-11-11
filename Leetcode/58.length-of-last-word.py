#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        s = s.rstrip()
        words = s.rsplit(" ")
        return len(words[-1])
        
# @lc code=end

