from math import log, floor, sqrt
from functools import lru_cache
class Solution(object):
    def numSquares(self, n):
        large = 1 << 8
        dp = [large] * (n + 1)
        base = floor(sqrt(n))
        # init
        for i in range(1, base+1):
            dp[i ** 2] = 1
        while dp[n] == large:
            for i in range(n + 1):
                for b in range(1, base + 1):
                    op = i + b ** 2
                    if op > n:
                        continue
                    dp[op] = min(dp[op], dp[i] + 1)
        return dp[n]


    def numSquares1(self, n):
        """
        :type n: int
        :rtype: int
        """
        @lru_cache(0)
        def helper(n):
            if n < 0:
                return 1 << 8
            root = sqrt(n)
            if root == floor(root):
                return 1
            else:
                base = floor(log(n, 2))
                return 1 + min([helper(n - i ** 2) for i in range(1, base + 1) ])

        return helper(n)
import pytest

@pytest.mark.parametrize("n, expected",[
    (12, 3),
    (20, 2),
    (1, 1),
    (54, 3),
    (4703, 4),
    ])

def test_num(n, expected):
    s = Solution()
    assert s.numSquares(n) == expected
