# Union Find
# find the number of connected componnent
import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def ii(): return int(stdin.readline())
def li(): return map(int, stdin.readline().split())
N, M = tuple(li())
prn = {i:i for i in range(1, N+1)}
def parent(node):
    if prn[node] == node:
        return node
    else:
        return parent(prn[node])
for _ in range(M):
    a, b, c = tuple(li())
    pa, pb = parent(a), parent(b)
    root = min(pa, pb)
    prn[a], prn[b] = root, root


print(len(set(prn.values())))
