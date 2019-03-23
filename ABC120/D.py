"""
union find & reverse bridge op order
the last bridge cost decreasing connectivity ===
the first bridge to increasing connectivity
"""
from collections import deque
import sys

stdin = sys.stdin
def li(): return map(int, stdin.readline().split())

N, M = tuple(li())
stack = []
for i in range(M):
    stack.append( tuple(li()) )

p_map = {}
for i in range(1, N + 1):
    # key: val
    # node_id: parent_id, union_size
    p_map[i] = [i, 1]

combs = deque()
def parent(i):
    if p_map[i][0] == i:
        return i
    else:
        return parent(p_map[i][0])
while stack:
    print(p_map)
    l, r = stack.pop()
    p_l = parent(l)
    p_r = parent(r)
    # parent should be greater
    if p_l == p_r:
        if combs:
            combs.appendleft(combs[0])
    else:
        if p_l < p_r:
            p_l, p_r = p_r, p_l
        p_map[p_r][0] = p_l
        incr = p_map[p_l][1] * p_map[p_r][1]
        p_map[p_l][1] += p_map[p_r][1]
        if combs:
            combs.appendleft(combs[0] + incr)
        else:
            combs.appendleft(incr)
cnt = 0
combs.append(0)
while combs:
    cur = combs.popleft()
    if combs:
        cnt += cur - combs[0]
        print(cnt)
