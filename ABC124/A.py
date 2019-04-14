import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def ii(): return int(stdin.readline())
def li(): return map(int, stdin.readline().split())
A, B = tuple(li())
if A == B:
    print(A * 2)
else:
    C = max(A, B)
    print(2*C -1)
