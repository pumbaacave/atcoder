class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: 'List[List[int]]') -> 'int':
        # TODO check input
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(n+1):
            if obstacleGrid[1][i-1] == 0:
                dp[1][i] = 1
        for i in range(m+1):
            if obstacleGrid[i-1][0] == 0:
                dp[i][1] = 1
        for i in range(2, m+1):
            for j in range(2, n+1):
                num_left = dp[i-1][j] if obstacleGrid[i-2][j-1] == 0 else 0
                num_right = dp[i][j-1] if obstacleGrid[i-1][j-2] == 0 else 0
                dp[i][j] = num_left + num_right

        return dp[m][n]

s = Solution()
s.uniquePaths(3,2)
