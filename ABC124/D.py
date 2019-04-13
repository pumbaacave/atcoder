
from itertools import groupby
import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def ii(): return int(stdin.readline())
def li(): return map(int, stdin.readline().split())
N, K = tuple(li())
S = stdin.readline() + "2"
# use window
l, r = 0, 0
cnt = 0
r_iter = groupby(S)
l_iter = groupby(S)
r_next = next(r_iter)
l_next = next(l_iter)
while r < N:
    # print(l, r, K)
    if K > 0:
        if r_next[0] == '1' and r > 0:
            K -= 1
        r += len(list(r_next[1]))
        r_next = next(r_iter)
        cnt = max(cnt, r - l)
    elif K == 0 and r_next[0] == "1":
        cnt = max(cnt, r - l)
        r += len(list(r_next[1]))
        r_next = next(r_iter)
        cnt = max(cnt, r - l)
    else:
        if l_next[0] == "0":
            K += 1
        l += len(list(l_next[1]))
        l_next = next(l_iter)
# print(l,r,K)
if r_next[0] == '1':
    cnt = max(cnt, r-l)
print(cnt)
