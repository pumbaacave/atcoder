from typing import *
from collections import deque, defaultdict
class Solution:
    def nextGreaterElement(self, nums: List[int]) -> List[int]:
        """
        nums2 now is consider a cycle list
        """
        stack = deque()
        next_greater_map = defaultdict(deque)
        for n in nums * 2:
            while stack and stack[-1] < n:
                cur = stack.pop()
                next_greater_map[cur].append(n)
            stack.append(n)

        res = []
        for n in nums:
            if next_greater_map[n]:
                res.append( next_greater_map[n].popleft() )
            else:
                res.append(-1)
        return res

def test_next():
    s = Solution()
    nums = [1,2,1]
    ans = s.nextGreaterElement(nums)
    assert ans == [2, -1, 2]

def test_failLC_sample():
    s = Solution()
    nums = [100,1,11,1,120,111,123,1,-1,-100]
    ans = s.nextGreaterElement(nums)
    assert ans == [120,11,120,120,123,123,-1,100,100,100]
