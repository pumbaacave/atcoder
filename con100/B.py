
import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def li(): return map(int, stdin.readline().split())
N = int(stdin.readline())
nums = tuple(li())
total = 0
for n in nums:
    while n % 2 == 0:
        total += 1
        n = n / 2
print(total)
