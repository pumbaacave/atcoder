import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def ii(): return int(stdin.readline())
def li(): return map(int, stdin.readline().split())
N = ii()
nums = tuple(li())
cnt = 0
bar = -1
for n in nums:
    cnt += 1 if n >= bar else 0
    bar = max(bar, n)
print(cnt)
