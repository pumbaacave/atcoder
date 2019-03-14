from collections import namedtuple
from itertools import cycle
class Solution(object):
    def __init__(self):
        self.dirs = [
                (0, 1),
                (1, 0),
                (0, -1),
                (-1, 0),
                ]
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        Pos = namedtuple('Pos', ('r', 'c'))
        def out_of_bound(pos):
            N = len(matrix)
            M = len(matrix[0])
            if pos.r < 0 or pos.r >= N:
                return True
            if pos.c < 0 or pos.c >= M:
                return True
            return False
        def get_next(cur, d):
            p = Pos(cur.r + d[0], cur.c + d[1])
            if out_of_bound(p) or matrix[p.r][p.c] == "#":
                next_d = next(gen_dir)
                next_p = Pos(cur.r + next_d[0], cur.c + next_d[1])
                print(next_p)
                if out_of_bound(next_p):
                    return cur, d
                else:
                    return next_p, next_d
            else:
                return p, d
        gen_dir = cycle(self.dirs)
        output = []
        # destructive update
        d = next(gen_dir)
        cur = Pos(0, 0)
        while matrix[cur.r][cur.c] != "#":
            r, c = cur
            output.append(matrix[r][c])
            matrix[r][c] = "#"

            cur, d = get_next(cur, d)

        return output
