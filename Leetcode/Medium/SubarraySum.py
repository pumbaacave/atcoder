from typing import *
import collections
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums: return 0
        # build partial sum array
        cnt = collections.Counter()
        cnt[0] = 1
        total = 0
        cur_sum = 0
        for num in nums:
            cur_sum += num
            total += cnt[cur_sum - k]
            cnt[cur_sum] += 1
        return total
def test_s():
    s = Solution()
    nums = [-1, -1, 1]
    k = 1
    assert s.subarraySum(nums, k) == 1
