class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: 'List[List[int]]') -> 'int':
        # TODO check input
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if m == 1 and n == 1 and obstacleGrid[m-1][n-1] == 1:
            return 0
        memo = {(m - 1, n - 1): 1 - obstacleGrid[m-1][n-1]}
        def helper(c, r):
            if (c, r) in memo: return memo[(c, r)]
            if obstacleGrid[c][r] != 1:
                num_r = helper(c, r+1) if r+1 < n else 0
                num_d = helper(c+1, r) if c+1 < m else 0
                total = num_r + num_d
            else:
                total = 0
            memo[(c, r)] = total
            return total

        helper(0, 0)
        return memo[(0, 0)] if memo[(0,0)] > 0 else 0


s = Solution()
s.uniquePaths(3,2)
