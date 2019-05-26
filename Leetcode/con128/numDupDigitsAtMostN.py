from functools import reduce
from itertools import islice
from math import log10, floor
"""
algo right but,,,,
"""
class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        # cal num_digit without repeatition
        l = floor(log10(N)) + 1
        full = [0] * l
        N_str = str(N)
        ops = range(9, 0, -1)
        def cal_num(L):
            total = 0
            # cal num of non repeat when start idx not 0
            for i in range(L):
                g = gen()
                total += 1
                

