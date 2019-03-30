from typing import *
class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        # print(stones)
        L = len(stones)
        if not L or L == 0:
            return 0
        if L == K:
            return sum(stones)
        if (L - 1) % (K - 1) != 0:
            return -1
        def find_least_pile(stones, K):
            sums = []
            MIN = 1 << 20
            for i in range(len(stones) - K + 1):
                sums.append(sum(stones[i:i + K]))
                MIN  = min(MIN, sums[-1])
            return sums.index(MIN), MIN

        idx, sub_total = find_least_pile(stones, K)
        total = sub_total + self.mergeStones(stones[:idx] + [sub_total] + stones[idx + K:], K)
        return total

def test_stones():
    s = Solution()
    stones = [3,2,4,1]
    K = 2
    assert s.mergeStones(stones, K) == 20
    stones = [3,5,1,2,6]
    K = 3
    assert s.mergeStones(stones, K) == 25
    stones = [3,2,4,1]
    K = 3
    assert s.mergeStones(stones, K) == -1
