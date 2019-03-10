import bisect
from collections import deque
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        a = 1 << 31
        MAXINT32 = a - 1
        if n > MAXINT32:
            return -1
        # start processing
        num_list = str(n)
        stack = deque(num_list)
        checked = []
        is_found = False
        while stack:
            if not checked:
                # appendleft
                checked.append(stack.pop())
            else:
                if stack[-1] >= checked[-1]:
                    checked.append(stack.pop())
                else:
                    cur = stack.pop()
                    idx = bisect.bisect_right(checked, cur)
                    cur, checked[idx] = checked[idx], cur
                    res_list = [cur] + checked
                    is_found = True
                    break

        if is_found:
            # find larger
            stack.extend(res_list)
            res = int(''.join(stack))
        else:
            return -1

        if res > MAXINT32:
            return -1

        return res

import pytest

@pytest.mark.parametrize("n, expected",[
    (123, 132),
    (111, -1),
    (9, -1),
    (1222, 2122),
    (1232, 1322),
    (1231, 1312),
    (230241, 230412),
    ])
def test_111(n, expected):
    s = Solution()
    assert s.nextGreaterElement(n) == expected
