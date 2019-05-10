from functools import lru_cache
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        large = 1 << 100
        memo = {}
        @lru_cache(None)
        def cal(target):
            # if target in memo:
            #     return memo[target]
            if target == 0:
                return 0
            if target < 0:
                return large
            num = min([cal(target - c) for c in coins])
            if num == large:
                # memo[target] = large
                return large
            else:
                # memo[target] = num + 1
                return num + 1

        res =  cal(amount)
        if res == large:
            return -1
        else:
            return res
def test():
    coins = [1,2,5]
    a = 100
    s = Solution()
    assert s.coinChange(coins, a) == 20
