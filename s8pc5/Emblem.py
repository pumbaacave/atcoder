from math import sqrt
import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
def li(): return map(int, stdin.readline().split())

N, M = tuple(li())
for i in range(N):
    dummy = li()

Ms = []
for i in range(M):
    Ms.append(tuple(li()))
Ms.sort()
L = len(Ms)
ret = float('inf')
for i in range(L):
    for j in range(i + 1, L):
        if Ms[j][0] - Ms[i][0] >= ret:
            break
        else:
            ret = min(ret, sqrt((Ms[j][0] - Ms[i][0])**2 +(Ms[j][1] - Ms[i][1])**2))
print(ret/2)
