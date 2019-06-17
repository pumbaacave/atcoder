import bisect
from collections import Counter
from typing import *
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [0] * len(nums)
        ways = [1] * len(nums)
        total = 0
        for i, num in enumerate(nums):
            candidates = [dp[j]for j in range(0,i) if nums[i] > nums[j]]
            dp[i] = max(candidates) + 1 if candidates else 1
            if dp[i] > 1:
                ways[i] = sum( [ways[j] for j in range(0, i) if nums[i] > nums[j] and dp[i] == dp[j] + 1] )
        c = Counter(dp)
        return sum( [ways[i] for i in range(len(nums)) if dp[i] == max(dp)] )

def test_find():
    s = Solution()
    nums = [1,3,5,4,7]
    assert s.findNumberOfLIS(nums) == 2
    nums = [2,2,2,2,2]
    assert s.findNumberOfLIS(nums) == 5
    nums = [1,2,4,3,5,4,7,2]
    assert s.findNumberOfLIS(nums) == 3
