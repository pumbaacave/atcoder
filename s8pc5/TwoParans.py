from collections import Counter
from math import sqrt
import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
def li(): return map(int, stdin.readline().split())
#def ii(): return int(stdin.readline())
N = int(stdin.readline())

def check(Q):
    cnt = Counter(Q)
    if cnt["("] != cnt[")"]: return False
for i in range(N):
    if check(Q):
        print("Yes")
    else:
        print("No")
