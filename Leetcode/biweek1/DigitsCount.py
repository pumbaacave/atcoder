class Solution:
    def digitsCount(self, d: int, low: int, high: int) -> int:
        def count(d, bound):
            total = 0
            res = 1
            mul = 1
            while True:
                div, mod = divmod(bound, 10)
                if mod == d:
                    total += res
                elif mod < d:
                    total += mod * mul
                else:
                    total += (res + (mod - 1) * mul)
                mul *= 10
                res += mod * mul

                if div == 0:
                    break
            return total
        return count(d, high) - count(d, low)

