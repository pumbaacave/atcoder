#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start

from collections import Set


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        if n == 3:
            return 1
        non_prime = set()
        # pre-allocate bool array of is_prime can reduce memory foot print.
        for i in range(2, int(n ** 0.5) + 1):
            if i not in non_prime:
                for k in range(i * i, n, i):
                    non_prime.add(k)
        return n - 2 - len(non_prime)


# @lc code=end
