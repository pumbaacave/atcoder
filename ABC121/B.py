
import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def li(): return map(int, stdin.readline().split())

N, M, C = tuple(li())
Bs = tuple(li())
cnt = 0

for i in range(N):
    total = 0
    Ai = tuple(li())
    for j, b in enumerate(Bs):
        total += b * Ai[j]
    if total + C > 0:
        cnt += 1

print(cnt)
