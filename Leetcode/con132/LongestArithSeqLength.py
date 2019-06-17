from collections import defaultdict
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        # key: index, delta
        memo = defaultdict(int)
        L = len(A)
        if L < 1: return 0
        for i in range(L):
            for j in range(i + 1, L):
                l, r = A[i], A[j]
                d = l - r
                memo[j, d] = max(memo[j, d], memo[i, d] + 1)

        # plus 1 because of not count init seq_len
        return max(memo.values()) + 1
