import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def ii(): return int(stdin.readline())
def li(): return map(int, stdin.readline().split())
A, P = tuple(li())
ps = A * 3 + P
print(ps // 2)
