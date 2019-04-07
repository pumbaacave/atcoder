from random import choice
from hypothesis import given
from hypothesis import strategies as st
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)
        rev_nums = list(reversed(sorted_nums))
        i = 0
        j = 0
        first, second = -1, -1
        while True:
            temp_sum = sorted_nums[i] + rev_nums[j]
            if  temp_sum == target:
                first, second = sorted_nums[i], rev_nums[j]
                break
            elif temp_sum > target:
                j += 1
                # incr j, i remain the same
                continue
            elif temp_sum < target:
                i += 1
                # incr i, j remain the same
                continue
        print([first, second])
        first_idx = nums.index(first)
        if first == second:
            second_idx = nums.index(second, first_idx + 1)
        else:
            second_idx = nums.index(second)
        return [first_idx, second_idx]

s = Solution()
@given(nums=st.lists(st.integers(min_value=1), min_size=2, unique=True))
def test_sample(nums):
    global s
    target = choice(nums) + choice(nums)
    i,j  = s.twoSum(nums, target)
    res = [nums[i], nums[j]]
    assert res[0] in nums
    assert res[1] in nums
    assert sum(res) == target

