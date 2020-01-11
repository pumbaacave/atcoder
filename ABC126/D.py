import sys
from collections import defaultdict, deque
from math import ceil, log2
stdin = sys.stdin
def ii(): return int(stdin.readline())
def li(): return map(int, stdin.readline().split())
N = ii()
seen = dict()
lr = defaultdict(list)
for i in range(N - 1):
    l, r, d= tuple(li())
    lr[l].append([r, d])
    lr[r].append([l, r])

# start from 1, color it black
queue = deque([[1, 0]])
seen[1] = 0
while queue:
    cur, d = queue.popleft()
    for nei, delta in lr[cur]:
        if nei in seen: continue
        else:
            new_color = 0 if (d & 1) == 0 else 1
            seen[nei] = new_color
            queue.append([nei, d + delta])
for i in range(1, N + 1):
    print(seen[i])
