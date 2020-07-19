class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        cnt = numBottles
        while numExchange <= numBottles:
            div, numBottles= divmod(numBottles, numExchange)
            numBottles += div
            cnt += div
        return cnt
