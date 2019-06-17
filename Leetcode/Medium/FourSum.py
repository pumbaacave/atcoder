# from loguru import logger
from hypothesis import given
from hypothesis.strategies import lists, integers
from random import sample
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = {}
        state = []
        L = len(nums) - 1
        # @lru_cache(None)
        def search(start, target):
            if start >= L: return
            # print(target, state)
            if len(state) == 2:
                # twoSum problem
                l, r = start, L
                while l < r:
                    total = nums[l] + nums[r]
                    if total == target:
                        ans = state[:] + [nums[l], nums[r]]
                        ans.sort()
                        ret[str(ans)] = ans
                        # maybe remaining combination
                        l += 1
                        r -= 1
                    elif total > target:
                        r -= 1
                    else:
                        l += 1

            elif len(state) < 2:
                for i in range(start, L):
                    state.append(nums[i])
                    search(i + 1, target - nums[i])
                    state.pop()
        nums.sort()
        search(0, target)
        return list(ret.values())

s = Solution()
@given(nums=lists(integers(), min_size=4))
def test_hypo(nums):
    pick = sample(nums, 4)
    target = sum(pick)
    ret = s.fourSum(nums, target)
    for r in ret:
        assert len(r) == 4
        assert sum(r) == target
def test_foursum():
    nums = [1,0,-1,0,-2,2]
    target = 0
    assert len(s.fourSum(nums, target)) == 3
def test_foursum1():
    nums = [1,-2,-5,-4,-3,3,3,5]
    target = -11
    assert len(s.fourSum(nums, target)) == 1
def test_foursum2():
    nums = [-3,-2,-1,0,0,1,2,3]
    target = 0
    assert len(s.fourSum(nums, target)) == 8
