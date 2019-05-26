class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        if L < M: L, M = M, L
        Len = len(A)
        Ls = [sum(A[i:i+L]) for i in range(Len-L+1)]
        Ms = [sum(A[i:i+M]) for i in range(Len-M+1)]
        total = 0
        for i in range(Len-L+1):
            left = max(Ms[:i-M+1] or [0])
            right = max(Ms[i + L:] or [0])
            cur = Ls[i] + max(left, right)
            total = max(total, cur)
        return total
