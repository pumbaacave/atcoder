import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def li(): return map(int, stdin.readline().split())

H, W = tuple(li())
h, w = tuple(li())

res = (H - h) * (W * w)
