class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        summary = []
        if not nums: return summary
        l = r = nums[0]

        def output(l, r):
            if l == r:
                summary.append(str(l))
            else:
                summary.append('->'.join([str(l), str(r)]))
        for n in nums:
            if n == r + 1:
                r += 1
            elif n > r + 1:
                output(l, r)
                l = r = n
        else:
            output(l, r)
        return summary
