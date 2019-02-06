class Solution:
    def numTrees(self, n):
        # dp[i][j] :: num of unique BST using integer in i ... j
        dp = [[0] * n for _ in range(n)]
        # input validation
        if n == 1:
            return 1
        elif n == 2:
            return 2

        # tree width one node
        for i in range(n):
            dp[i][i] = 1
        # tree width two nodes
        for i in range(n-1):
            dp[i][i+1] = 2
        # for width lge to 3 to n
        for w in range(2, n):
            for start in range(n-w):
                end = start + w
                dp[start][end] += dp[start+1][end]
                dp[start][end] += dp[start][end-1]
                for root in range(start+1, end):
                    dp[start][end] += (dp[start][root-1] * dp[root+1][end])
        return dp[0][n-1]

s = Solution()
ans = s.numTrees(3)
print(ans)
