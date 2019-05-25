import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def ii(): return int(stdin.readline())
def li(): return map(int, stdin.readline().split())

r, d, x = tuple(li())

def grow(x):
    return r * x - d
for i in range(10):
    x = grow(x)
    print(x)
