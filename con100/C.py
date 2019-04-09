
import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def li(): return map(int, stdin.readline().split())

D, N = tuple(li())
print(N * 100 ** D)
