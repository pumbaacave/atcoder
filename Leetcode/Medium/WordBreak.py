from typing import *
from collections import deque
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # BST
        L = len(s)
        dp = [False] * (L + 1)
        dp[0] = True
        for i in range(L):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        if dp[L]: return True
        else: return False

def test_process():
    s = Solution()
    print(s.process_dict(["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba"]))

