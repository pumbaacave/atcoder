import bisect
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # monotonic stack
        if not nums:
            return nums
        len_n = len(nums)
        inc_idxs = sorted(range(len_n), key=lambda i:nums[i])
        downs = [0] * len_n
        ret = []
        for idx in inc_idxs:
            bisect.insort_left(ret,idx)
            num_lesser = len(ret) - bisect.bisect_left(ret, idx) - 1
            downs[idx] = num_lesser
        return downs
