from collections import deque
class Solution:
    def maxProfit(self, prices, fee):
        if not prices or len(prices) == 1:
            return 0
        # dp_buy = [0]*length
        # dp_sale = [0]*length
        # init
        # dp_buy[0] = - prices[0]
        gain_one_in_hand = - (1<<100)
        gain_zero_in_hand = 0
        for i, price in enumerate(prices):
            old_one = gain_one_in_hand
            old_zero = gain_zero_in_hand
            gain_one_in_hand = max(old_one, old_zero - price) # stay or buy 1
            gain_zero_in_hand = max(old_zero, old_one + price - fee) # stay or sale 1
            print(old_one, old_zero)
            # dp_buy[i] = max(dp_buy[i-1], dp_sale[i-1] - prices[i])
            # dp_sale[i] = max(dp_sale[i-1], dp_buy[i-1] + prices[i] - fee)
        return gain_zero_in_hand

s = Solution()
Input = [1,3,2,5]
ans = s.maxProfit(Input, 1)
print(ans)
