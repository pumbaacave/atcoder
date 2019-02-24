from collections import deque
class Solution:
    def integerReplacement(self, n: int) -> int:
        """
        use -1, >> 1 cost 2 ops per "1" digit
        use +1> >> 1 cost 1 ops per "1" digit but add "1" digit to left
        """
        binary = format(n, 'b')
        stack = deque(binary)
        num_op = 0
        l, r = 0, 0
        length = len(binary)
        while stack:
            if stack[-1]  == '0':
                stack.pop()
                num_op += 1
                r += 1
                l += 1
                continue
            #else
            while stack and stack[-1] == '1':
                stack.pop()
                r += 1
            # stack[-1] is zero, or stack empty
            one_length = r - l
            # update l position
            l = r
            if stack:
                if one_length == 1:
                    num_op += 2
                else:
                    num_op += 1 + one_length
                    stack[-1] = '1'
            # stack empty
            else:
                if one_length <= 2:
                    num_op += 2 *(one_length - 1)
                else:
                    num_op += 1 + one_length

        return num_op


import pytest

@pytest.mark.parametrize("n, expected",[
    (3, 2),
    (7, 4),
    (8, 3),
    (27, 7)
    ])
def test_replace(n, expected):
    s = Solution()
    ans = s.integerReplacement(n)
    assert ans == expected

