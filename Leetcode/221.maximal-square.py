#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # DP
        # A B 
        # C D
        # if A, B, C is anchor(right botton) of an N size square
        # D is deemed as a N+1 zide square
        if not matrix:
            return 0
        dp = [[1 if num == "1" else 0 for num in row] for row in matrix]
        n, m = len(dp), len(dp[0])
        # quick return for index under flow case
        edge = 1 if any(sum(row) > 0 for row in dp) else 0
        if n < 2 or m < 2:
            return edge
        ret = edge
        for i in range(1, n):
            for j in range(1, m):
                if dp[i][j] == 0:
                    continue
                A = dp[i-1][j-1]
                B = dp[i-1][j]
                C = dp[i][j-1]
                # B, C can provide extension for direction/edge
                # A provide limitation as well if cannot result in a square
                dp[i][j] = max(min(B, C, A), 0) + 1
                ret = max(ret, dp[i][j])
        return ret ** 2
# @lc code=end

