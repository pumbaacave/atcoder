class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for num in num_set:
            # this works as a explored_num_set
            if num - 1 not in num_set:
                cur_l = 1
                while num + 1 in num_set:
                    num += 1
                    cur_l += 1
                longest = max(longest, cur_l)
        return longest
