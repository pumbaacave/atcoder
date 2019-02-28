from collections import deque, defaultdict
from typing import *
class Solution1:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        using a stack to build next_greater_num mapping
        the stack is used
        1. to watermark the state, only find next greater num from the stack
        2. ensure sequence, (right)subproblem shold be solved before current problem
        """
        stack = deque(nums2)
        next_greater_map = {}

        def process_stack(stack):
            """
            find next greater num of cur only
            """
            if stack:
                # breakpoint()
                cur = stack.popleft()
                while stack:
                    right = stack[0]
                    if cur < right:
                        next_greater_map[cur] = right
                        return
                    else:
                        process_stack(stack)
                        stack.appendleft(cur)
                        return
                else:
                    next_greater_map[cur] = -1
        while stack:
            process_stack(stack)
        return [ next_greater_map[n] for n in nums1 ]

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        using a monotonic decreasing stack
        """
        stack = deque()
        next_greater_map = defaultdict(lambda :-1)
        for n in nums2:
            while stack and stack[-1] < n:
                cur = stack.pop()
                next_greater_map[cur] = n
            stack.append(n)

        return [ next_greater_map[n] for n in nums1 ]

def test_next():
    s = Solution()
    # nums1 = [4,1,2]
    # nums2 = [1,3,4,2]
    # ans = s.nextGreaterElement(nums1, nums2)
    # print(ans)

    nums1 = [1,3,5,2,4]
    nums2 = [6,5,4,3,2,1,7]
    ans = s.nextGreaterElement(nums1, nums2)
    print(ans)
