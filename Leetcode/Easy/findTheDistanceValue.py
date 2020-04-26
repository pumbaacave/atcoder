import bisect


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        if not arr1 or not arr2:
            return 0
        arr1.sort()
        arr2.sort()
        cnt = 0
        l = arr2[0]
        idx = 0
        def dis(elem, l, r):
            return min(abs(elem - l), abs(elem - r))

        # compute all min distance of elem from arr1 to arr2
        for elem in arr1:
            while idx < len(arr2) and arr2[idx] < elem:
                l = arr2[idx]
                idx += 1
            cnt += d < dis(elem, l, arr2[idx % len(arr2)])
        return cnt
