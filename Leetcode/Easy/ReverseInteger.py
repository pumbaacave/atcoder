class Solution:
    def reverse(self, x: int) -> int:
        limit = (1 << 31)
        is_minus = False
        if x < 0:
            is_minus = True
            x = abs(x)
        ret = 0
        while x != 0:
            x, mod = divmod(x, 10)
            ret = ret * 10 + mod
        ret = -ret if is_minus else ret
        if ret > limit-1: return 0
        if ret < -limit: return 0
        return ret
