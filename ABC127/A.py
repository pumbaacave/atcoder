import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def ii(): return int(stdin.readline())
def li(): return map(int, stdin.readline().split())
A, B = tuple(li())
if A >= 13:
    print(B)
elif A >= 6:
    print(B//2)
else:
    print(0)
