import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def ii(): return int(stdin.readline())
def li(): return map(int, stdin.readline().split())
S = stdin.readline()
L = len(S)
cnt = 0
cnt1 = 0
# 0101010101
for i, s in enumerate(S):
    if i & 1 == 1:
        incr = 1 if s == '1' else 0
        cnt += incr
    else:
        incr = 1 if s == '0' else 0
        cnt += incr
for i, s in enumerate(S):
    if i & 1 == 1:
        incr = 1 if s == '0' else 0
        cnt1 += incr
    else:
        incr = 1 if s == '1' else 0
        cnt1 += incr
print(min(cnt, cnt1))
