class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        # n by n 2d array
        # dp[i][j]: left =i, right = j(inclusive) range, if start with A, its max gain
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0
        for i in range(n - 1):
            dp[i][i+1] = max(stones[i], stones[i + 1])
        for i in range(n - 2):
            left = min(stones[i+2], stones[i + 1])
            right = min(stones[i], stones[i + 1])
            dp[i][i+2] = max(left, right)
        # iterate through width, w == 0 -> 1 element
        for w in range(3, n):
            # iterate through left point
            for l in range(n - w):
                # choose left
                score_l = min(stones[l+1], stones[l+w]) + dp[l+2][l+w-1]
                # choose right
                score_r = min(stones[l], stones[l+w-1]) + dp[l+1][l+w-2]

                dp[l][l + w] = max(score_l, score_r)
        return dp[0][n-1]

