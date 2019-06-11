import bisect
class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        for i in reversed(range(len(A))):
            if i == len(A) - 1:
                continue
            elif A[i] > A[i + 1]:
                swp_v = bisect.bisect_left(A, A[i], i + 1) - 1
                swp_i = A.index(A[swp_v], i+1)
                A[i], A[swp_i] = A[swp_i], A[i]
                break
        return A

