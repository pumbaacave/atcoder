class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums)==1:
            return [nums]
        head = nums[0]
        tail = nums[1:]
        tail_permutation = self.permute(tail)
        head_pmt = []
        for pmt in tail_permutation:
            for idx in range(len(pmt)+1):

                copy = pmt.copy()
                copy.insert(idx, head)
                head_pmt.append(copy)
        return head_pmt


nums = [1, 2, 3]
s = Solution()
print(s.permute(nums))
        