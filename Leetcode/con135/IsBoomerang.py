class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        A, B, C = points
        is_ver = A[0] == B[0] and B[0] == C[0]
        is_skew = (B[1] - A[1]) * (C[0] - B[0]) == (B[0] - A[0]) * (C[1] - B[1])
        return not(is_ver or is_skew)
