from loguru import logger
from functools import logger
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # @lru_cache(0)
        # choises is mutable so lru_cache not work
        # or add deserial and serial function
        def can1PWin(choises, desired_total):
            # logger.debug(memo)
            # desired_total will be positive
            if not choises: return False
            h = tuple(choises)
            if h in memo:
                # logger.debug("memo works")
                return memo[h]

            if max(choises) >= desired_total:
                memo[h] = True
                return True

            # if 2P fail one case, use it and 1P can win
            for i in range(len(choises)):
                # all logic choises[0], choises[i] = choises[i], choises[0]
                # judge can2PWin on remainging choises
                if not can1PWin(choises[1:], desired_total - choises[0]):
                    memo[h] = True
                    return True
                choises[0], choises[i] = choises[i], choises[0]

            # all case 2P can win
            memo[h] = False
            return False
        memo = {}
        choices = list(reversed(range(1, maxChoosableInteger + 1)))
        if sum(choices) < desiredTotal: return False
        return can1PWin(choices, desiredTotal)

def test_win():
    s = Solution()
    # assert s.canIWin(10, 25) == False
    assert s.canIWin(20, 210) == False
