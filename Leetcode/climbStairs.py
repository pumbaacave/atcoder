class Solution:
    def climbStairs(self, n: int) -> int:
        # possible choise 1 step or 2 step
        n1 = 1
        n2 = 2
        n3 = 3
        if n <= 3:
            # base cases
            return n
        while n > 3:
            # perform n - 3 iteration
            n -= 1
            temp = n2 + n3
            n1, n2, n3 = n2, n3, temp
        return n3
