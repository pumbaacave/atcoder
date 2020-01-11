import heapq
import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def ii(): return int(stdin.readline())
def li(): return map(int, stdin.readline().split())
N, M = tuple(li())
intervals = []
for i in range(N):
    a, b, c = tuple(li())
    if b - c < 0:
        continue
    intervals.append([a - c, b - c, c])
intervals.sort(key=lambda x: x[2])
idx = 0
for i in range(M):
    d = ii()
    for a, b, c in intervals:
        if a< d < b:
            print(c)
            break
    else:
        print(-1)


