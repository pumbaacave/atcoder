from math import log2, floor
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        num =floor(log2(N))
        mask = 2 ** (num + 1)- 1
        return N ^ mask
