class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        if not customers: return 0
        total = 0
        running_sum = 0
        idx = 0
        stable = 0
        delta = X
        for c, g in zip(customers, grumpy):

            if g == 0:
                stable += c

            if X == 0:
                X += 1
                running_sum -= customers[idx-delta] * grumpy[idx-delta]

            running_sum += c * g
            total = max(total, running_sum)
            print(idx, total)

            X -= 1
            idx += 1
        return total + stable
