class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        M, N = len(A), len(B)
        dp = [[0] * (N + 1) for _ in range(M + 1)]
        for i in range(M):
            for j in range(N):
                match = dp[i][j]
                if A[i] == B[j]: match += 1
                dp[i + 1][j + 1] = max([dp[i][j + 1], dp[i + 1][j], match])
        return dp[-1][-1]
