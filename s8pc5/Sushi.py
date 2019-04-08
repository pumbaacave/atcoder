import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
#def ii(): return int(stdin.readline())
def li(): return map(int, stdin.readline().split())

N, T = tuple(li())

last = 0
nums = tuple(li())
num_inter = 0
for t in nums:
    if t >= last:
        last = t
    else:
        while t < last:
            t += T
        last = t
print(last)
