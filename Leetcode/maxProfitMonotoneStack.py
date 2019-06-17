class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        # for flushing purpose
        prices.append(-float('inf'))
        # monotonic stack
        stack = []
        max_profit = 0
        for p in prices:
            if not stack:
                stack.append(p)

            if p > stack[-1]:
                stack.append(p)
            else:
                # pop smaller elements first
                while stack and p <= stack[-1]:
                    max_profit = max(max_profit, stack[-1] - stack[0])
                    stack.pop()

                stack.append(p)
        return max_profit

