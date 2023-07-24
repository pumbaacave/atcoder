#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        N = len(prices)
        dp_buy = [-float('INF')] * N
        # any initial val <= 0 is ok
        dp_sell = [-float('INF')] * N

        # first day cannot sell
        dp_buy[0] = -prices[0]
        dp_buy[1] = -prices[1]
        # set up no debt to accomodate later buy
        dp_sell[0] = 0
        for i in range(1, N):
            # for k in range(i):
            #     dp_sell[i] = max(dp_buy[k] + (prices[i]), dp_sell[i])
            #     # buy requires cooldown
            #     if k >= i - 1:
            #         continue
            #     dp_buy[i] = max(dp_sell[k] - prices[i], dp_buy[i])

            dp_sell[i] = max(dp_buy[i - 1] + prices[i], dp_sell[i])
            # manage last best state
            dp_sell[i] = max(dp_sell[i - 1], dp_sell[i])
            # buy requires cooldown
            dp_buy[i] = max(dp_buy[i - 1], dp_buy[i])
            if i < 2:
                continue
            dp_buy[i] = max(dp_sell[i - 2] - prices[i], dp_buy[i])
        # print(dp_buy)
        # print(dp_sell)
        return max(max(dp_sell), max(dp_buy))


# @lc code=end
