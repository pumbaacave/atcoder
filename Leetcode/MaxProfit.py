class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        length = len(prices)
        low = 1 << 100
        high = 0
        high_first_down = True
        gain = 0
        length = len(prices)
        for i in range(length-1):
            if prices[i] < low:
                low = prices[i]
            if high <= prices[i+1]:
                high = prices[i+1]
            else:

                gain += max(0, high-low)
                high = prices[i+1]
                low = prices[i+1]

        gain += max(0, high-low)
        return gain

