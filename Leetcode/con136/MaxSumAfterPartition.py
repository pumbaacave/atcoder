from collections import deque
from itertools import chain
class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        if not A: return 0
        la = len(A)
        # TODO: when la <= K
        if la < K:
            return max(A) * la
        # DP
        dp = [0] * la
        for i in range(K):
            dp[~i] = (i + 1) * max(A[~i:])
        for i in reversed(range(la-K)):
            for j in range(K):
                left = max(A[i:i+j+1]) * (j+1)
                # off by one check
                cur = left + dp[i+j+1]
                dp[i] = max(dp[i], cur)
        return dp[0]
