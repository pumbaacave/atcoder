from typing import *
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        total_state = []
        # num_l - num_r
        delta = 0
        left, right = "(", ")"
        def helper(remain_l, delta, state):
            if delta < 0: return
            # base case
            if remain_l == 0 and delta == 0:
                total_state.append("".join(state))
                return
            # try insert left
            if remain_l > 0:
                state.append(left)
                helper(remain_l - 1, delta + 1, state)
                state.pop()
            # try insert right
            if delta > 0:
                state.append(right)
                helper(remain_l, delta - 1, state)
                state.pop()
        helper(n, 0, [])
        return total_state

def test_gen():
    s = Solution()
    print(s.generateParenthesis(3))
