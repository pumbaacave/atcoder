class Solution:
    def nextPermutation(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        def helper(idx):
            """
            find the minimum from tailing numbers that lgt nums[idx]
            if found:
                swapped and sort tailing numbers
            """
            print(idx)
            swapped = nums[idx]
            candidates = nums[idx+1:]
            # find index of minimun num larger than swapped and swap
            INF = float("INF")
            minimun_upper =  INF
            for c in candidates:
                if c > swapped:
                    minimun_upper = min(minimun_upper, c)
            if minimun_upper <= swapped or minimun_upper == INF:
                return False
            else:
                idx_minimun_upper = candidates.index(minimun_upper)
                nums[idx] = minimun_upper
                nums[idx+1+idx_minimun_upper] = swapped
                sort_buffer = nums[idx+1:]
                nums[idx+1:] = sorted(sort_buffer)
                return True

        length = len(nums)
        is_swapped = False
        for i in range(length):
            is_swapped = helper(length-i-1)
            if is_swapped:
                return nums
        # nums ls a lexicographcal max
        if not is_swapped:
            nums.sort()

def test_nextP():
    s = Solution()
    nums = [1, 2]
    s.nextPermutation(nums)
    print(nums)
