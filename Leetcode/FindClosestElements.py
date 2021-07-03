from typing import List
from bisect import bisect_right


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # explore left first, thus bisect_right
        if(k >= len(arr)):
            return arr

        idx = bisect_right(arr, x)
        idx = min(idx, len(arr) - 1)

        INF = float('INF')
        # start with [l:r], this constrain is crutrial
        l = r = idx
        # l, r from beginning indicate window length of 2
        while k > 0:
            k -= 1
            val_l = abs(arr[l-1] - x) if l >= 1 else INF
            val_r = abs(arr[r] - x) if r < len(arr) else INF
            if val_l <= val_r:
                l -= 1
            else:
                r += 1
        return arr[l:r]
