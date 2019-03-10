import itertools
class Solution:
    def clumsy(self, N: int) -> int:
        ops = ["*", "//", "+", "-"]
        ops = itertools.cycle(ops)

        gen = range(N,0,-1)
        # val = itertools.zip_longest(gen, ops)
        val = zip(gen, ops)
        out = []
        for t in val:
            out.extend(list(t))
        out_str = ''.join(map(str, out[:-1]))
        e = eval(out_str)




        return e

def test_clu():
    N = 10
    s = Solution()
    s.clumsy(N)
