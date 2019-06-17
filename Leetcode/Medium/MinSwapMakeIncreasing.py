class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        L = len(A)
        if L <= 1:
            return 0
        cnt = 0
        # total num_swap when do not swap at i while maintain monotonicity
        not_swap = [L] * L
        not_swap[0] = 0
        # total num_swap when swap at i while...
        swap = [L] * L
        # swap can still keep sorted
        swap[0] = 1
        for i in range(1, L):
            if A[i - 1] < A[i] and B[i - 1] < B[i]:
                # update not_swap[i] first in this case
                not_swap[i] = not_swap[i - 1]
                swap[i] = swap[i - 1] + 1
            if A[i - 1] < B[i] and B[i - 1] < A[i]:
                not_swap[i] = min(not_swap[i], swap[i - 1])
                swap[i] = not_swap[i - 1] + 1
        return min(swap[L-1], not_swap[L-1])
