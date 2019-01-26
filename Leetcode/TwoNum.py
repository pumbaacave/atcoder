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

def test_sample():
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    assert [0, 1] == s.twoSum(nums, target)

test_sample()