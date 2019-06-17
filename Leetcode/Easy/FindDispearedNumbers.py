class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # bucket sort
        if not nums:
            return nums
        ln = len(nums)
        bucs = [0] * (ln + 1)
        for n in nums:
            bucs[n] += 1
        ret = []
        for n, c in enumerate(bucs[1:], 1):
            if c == 0:
                ret.append(n)
        return ret
