from collections import Counter
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        c = Counter()
        L = len(nums)
        if L < 2:
            return 0

        for i, num in enumerate(nums):
            cur = num
            for testee in nums[i + 1:]:
                c[cur ^ testee] += 1
        total = 0
        for k, v in c.items():
            total += format(k, 'b').count('1') * v
        return total
    def totalHammingDistance(self, nums):
        return sum(x*(len(nums)-x) for x in [b.count('0') for b in zip(*map('{:032b}'.format, nums))])
