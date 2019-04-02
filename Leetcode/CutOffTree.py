from typing import *
from collections import namedtuple
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        pos = namedtuple('pos', 'r, c')
        M, N = len(forest), len(forest[0])
        # cutoff update min_cut
        cur = pos(0, 0)
        # if forest[cur.r][cur.c] > 1:
        #     forest[cur.r][cur.c] = 1
        num_walk = 0
        def find_next(cur):
            val = 1 << 20
            p = None
            for r, c in [(cur.r-1, cur.c), (cur.r+1, cur.c), (cur.r, cur.c-1), (cur.r, cur.c+1)]:
                if 0 <= r < M and 0 <= c < N:
                    if forest[cur.r][cur.c] <forest[r][c]< val:
                        val = forest[r][c]
                        p = r, c
                        # print(r, c)

            forest[cur.r][cur.c] = 1
            if not p:
                return p, False
            else:
                return pos(p[0], p[1]), True
        while True:
            # print(cur,forest[cur.r][cur.c])
            cur, found = find_next(cur)
            # print(cur, found)
            if found:
                num_walk += 1
            else:
                break

        # check valid and return
        # print(forest)
        for r in forest:
            for c in r:
                if c > 1:
                    return -1
        return num_walk
def test_find():
    s = Solution()
    i = [[1,2,3],[0,0,4],[7,6,5]]
    assert s.cutOffTree(i) == 6
