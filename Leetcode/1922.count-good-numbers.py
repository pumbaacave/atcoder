#
# @lc app=leetcode id=1922 lang=python3
#
# [1922] Count Good Numbers
#

# @lc code=start

MOD = 10**9 + 7


class Solution:
    # python is too slow ...
    def countGoodNumbers(self, n: int) -> int:
        # cardinality
        card_even = 5
        card_odd = 4
        total = 1
        #for num in range(n):
        #    if num % 2 == 0:
        #        total *= card_even
        #    else:
        #        total *= card_odd
        #    total %= MOD
        d, m = divmod(n, 2)
        even_factor = 5 ** d % MOD
        odd_factor = 4 ** d % MOD
        # 素因素分解
        total = even_factor * odd_factor % MOD
        if m == 1:
            total = total * 5 % MOD
        return total


# @lc code=end
