class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        def cast_binary_guess(left, right):
            """
            worst case cost
            using binary guess strategy
            start from choosing left
            end at choosing right
            """
            cost_left = dp[0][left] + left
            while l < r:
                mid = (l + r) // 2


        LARGE = 1 << 10
        dp = [[LARGE] * (n + 1) for i in range(n)]
        for i in range(n):
            dp[i][i + 1] = i
        for r in range(2, n + 1):
            gen = range(0, r)
            for l in reversed(gen):
                # print('l:',l)
                for i in range(l + 1, r):
                    mid = (i + r) // 2
                    cost = dp[0][i] + dp[mid][r]
                    # print(0, mid, r)
                    # print(cost)
                    dp[l][r]=  min(dp[l][r], cost)

        # print(dp)
        return dp[0][n]


import pytest
@pytest.mark.parametrize("n, expected",[
    (3, 2),
    (4, 4),
    (5, 6),
    (7, 10),
    (9, 14),
    ])
def test_getmonry(n, expected):
    s = Solution()
    ans = s.getMoneyAmount(n)
    assert ans == expected

