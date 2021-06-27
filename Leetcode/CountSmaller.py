from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ret = [0] * len(nums)
        seen = SortedList()
        for idx, num in enumerate(reversed(nums)):
            cnt = seen.bisect_left(num)
            seen.add(num)
            ret[len(nums) - 1 - idx] = cnt
        return ret
            
