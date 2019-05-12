class Solution:
    def baseNeg2(self, N: int) -> str:
        if N == 0:
            return "0"
        res = []
        while N not in (0, 1):
            div, mod = divmod(N, -2)
            if mod == -1:
                res.extend([1, 1])
            else:
                res.append(mod)
            N = div
            if N == 1:
                res.append(N)
        res = reversed(res)
        return "".join(map(str, res))
