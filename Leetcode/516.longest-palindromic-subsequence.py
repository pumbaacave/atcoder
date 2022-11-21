#
# @lc app=leetcode id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#

# @lc code=start


class Solution:
    def longestPalindromeSubseq(self, s) -> int:
        s = list(s)
        N = len(s)
        # dp[i][j] = number of longest at s[i:j]
        dp = [[0 for i in range(N)] for j in range(N)]
        # width 0, and 1 case
        for i in range(N):
            dp[i][i] = 1
            # if i + 1 < N:
            #    # "bb" case
            #    dp[i][i+1] = 2 if s[i] == s[i + 1] else 1

        # width 2...N-1 case
        for w in range(1, N):
            # [i, i+w]
            for i in range(N - w):
                if s[i] == s[i+w]:
                    dp[i][i+w] = dp[i+1][i+w-1] + 2
                else:
                    dp[i][i+w] = max(dp[i][i+w-1], dp[i+1][i+w])
        return dp[0][N-1]


# @lc code=end
