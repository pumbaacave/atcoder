class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]: return 0

        memo = {}
        M, N = len(matrix), len(matrix[0])
        def valid(pos):
            i, j = pos
            if i < 0 or M <= i or j < 0 or N <= j:
                return False
            return True
        def climb(pos):
            if pos in memo: return memo[pos]
            i, j = pos
            neis = [(i+c, j+r) for c, r in [(-1,0), (1,0), (0,-1),(0,1)]]
            neis = filter(valid, neis)
            dis = -1 for n in neis:
                if matrix[n[0]][n[1]] <= matrix[i][j]:
                    continue
                elif climb(n) > dis:
                    dis = climb(n)
            if dis < 0:
                memo[pos] = 1
            else:
                memo[pos] = dis + 1
            return memo[pos]
        for i in range(M):
            for j in range(N):
                climb( (i,j) )
        return max(memo.values())

