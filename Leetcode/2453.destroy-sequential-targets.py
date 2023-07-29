#
# @lc app=leetcode id=2453 lang=python3
#
# [2453] Destroy Sequential Targets
#

from collections import Counter

# @lc code=start


class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        if(len(nums) == 1):
            return nums[0]

        # 1st try, wrong, NlogN
        # Sorted Multi set or sorted Map
        # use sorted map

        # 2nd try, can do in N
        rems = [num % space for num in nums]
        cnt: Counter = Counter(rems)
        ret = -1
        global_max = 0
        for num in nums:
            k = num % space
            v = cnt[k]
            if v > global_max:
                global_max = v
                ret = num
            if v == global_max:
                ret = min(ret, num)
        return ret


# @lc code=end
