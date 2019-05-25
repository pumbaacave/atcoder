import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def ii(): return int(stdin.readline())
def li(): return map(int, stdin.readline().split())
N, M = tuple(li())
interval = [1, N]
def intersect(ia, ib):
    if not ia or not ib:
        return []
    l = max(ia[0], ib[0])
    r = min(ia[1], ib[1])
    if l > r:
        return []
    else:
        return [l, r]

for i in range(M):
    l, r = tuple(li())
    interval = intersect(interval, [l, r])
if not interval:
    print(0)
else:
    print(interval[1] - interval[0] + 1)
