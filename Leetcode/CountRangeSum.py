class Solution:
    def countRangeSum(self, nums: 'List[int]', lower: 'int', upper: 'int') -> 'int':
        upper = upper - lower
        for i, _ in enumerate(nums):
            nums[i] -= lower

        #can create Window class
        l, r = 0, 0
        total = 0
        count = 0

        while r < len(nums):

            while total <= upper and 0 <= total and r < len(nums):
                total += nums[r]
                count += r - l + 1
                r += 1
            total -= nums[l]
            l += 1
        return count

def test_positive_allset():
    s = Solution()
    nums = [1, 2, 3]
    ans = s.countRangeSum(nums, 0, 10)
    assert ans == 6

def test_positive_partial_set():
    s = Solution()
    nums = [1, 2, 3]
    ans = s.countRangeSum(nums, 3, 10)
    assert ans == 3

def test_posneg():
    s = Solution()
    nums = [-1, 5, -2]
    ans = s.countRangeSum(nums, -2, 2)
    assert ans == 3
