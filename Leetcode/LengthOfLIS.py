import bisect
from typing import *
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        can use DP, space, time O(n ** 2)
        but use a triky tree instead
        DP with binary search
        """
        candidates = []
        for num in nums:
            # first num
            if not candidates:
                candidates.append(num)
                continue
            # find new maximum, appendable
            if num > candidates[-1]:
                candidates.append(num)
                continue
            # tyr update lower value in possible sequence
            idx = bisect.bisect_left(candidates, num)
            if num < candidates[idx]:
                candidates[idx] = num
        return len(candidates)

        
