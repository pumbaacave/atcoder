from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ret = float("INF")
        for i: int, num in enumerate(nums[:-2]):
            t_sum = self.twoSumClosest(nums[(i+1):], target - num)
            s_sum = t_sum + num
            ret = self.swap(s_sum, ret, target)
        return int(ret)

    def twoSumClosest(self, nums: List[int], target: int) -> int:
        # nums are sorted and len(nums) >= 2.
        assert len(nums) > 1
        ret = float("INF")
        l, r = 0, len(nums) - 1
        while l < r:
            cur = nums[l] + nums[r]
            if cur > target:
                r -= 1
                ret = self.swap(cur, ret, target)
            elif cur < target:
                l += 1
                ret = self.swap(cur, ret, target)
            else:
                return target
        return int(ret)

    def swap(self, num, ret, target):
        if abs(num - target) < abs(ret - target):
            return num
        else:
            return ret