from typing import *
from collections import Counter, defaultdict, namedtuple
import heapq

class Coor:
    def __init__(self, v, r, c):
        self.v = v
        self.r = r
        self.c = c
    def __lt__(self, rhs):
        return self.v < rhs.v
    def __repr__(self):
        return f"v:{self.v} r:{self.r} c:{self.c}"

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        books = {}
        # preset parent as self
        for s in stones:
            books[tuple(s)] = tuple(s)
        def find(key):
            if books[key] == key:
                return key
            else:
                return find(books[key])
        def update(key, p):
            if books[key] == p:
                return
            o_p = books[key]
            books[key] = p
            update(o_p, p)
        for s in stones:
            for r in stones:
                if s[0] == r[0] or s[1] == r[1]:
                    #merge
                    p_s, p_r = find(books[tuple(s)]), find(books[tuple(r)])
                    p = min(p_s, p_r)
                    update(tuple(s), p)
                    update(tuple(r), p)
        cnt = Counter(find(key) for key in books.keys())
        # print(books)
        # print(cnt)
        total = 0
        for v in cnt.values():
            total += v - 1
        return total

        
            
def test_remove():
    s = Solution()
    st = [[4,4],[5,5],[3,1],[1,4],[1,1],[2,3],[0,3],[2,4],[3,5]]
    assert s.removeStones(st) == 10

