import sys
import bisect
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def li(): return map(int, stdin.readline().split())

A, B = tuple(li())

def F(num):
    if num == 0:
        return 0
    # there are a pair: (0,1), (2,3)... where xor in every pair is 1
    a = (num + 1) // 2
    ret = 0 if a % 2 == 0 else 1
    ret = ret ^ num if num % 2 == 0 else ret
    return ret
res = F(A - 1) ^ F(B)
print(res)
