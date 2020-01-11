class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        l, r = 0, len(A) - 1
        while l <= r:
            mid = (l + r) // 2
            if mid == A[mid]:
                return mid
            elif mid > A[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return -1
