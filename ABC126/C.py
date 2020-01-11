import sys
from math import ceil, log2
stdin = sys.stdin

def li(): return map(int, stdin.readline().split())
N, K = tuple(li())
total = 0
for i in range(1, N + 1):
    if i < K:
        total += 2 ** -ceil(log2(K/i))
    else:
        total += 1
print(total/N)
