import sys
import bisect
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def li(): return map(int, stdin.readline().split())

N, M = tuple(li())

categories = [ tuple(li()) for _ in range(N) ]
categories.sort()

total_cost = [(0, 0)]
for A, B in categories:
    total_cost.append((B + total_cost[-1][0], A * B + total_cost[-1][1]))
    idx = bisect.bisect_right( total_cost, (M, 0) )
total = total_cost[idx][1] + (M - total_cost[idx][0]) * categories[idx - 1][0]
print(total)
