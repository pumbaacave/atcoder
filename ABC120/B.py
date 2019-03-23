import sys
stdin = sys.stdin
from math import sqrt

def li(): return map(int, stdin.readline().split())

def gcd(A, B):
    if B > A:
        return gcd(B, A)
    while B != 0:
        A, B = B, A - B
    return A

def test_gcd():
    assert gcd(8, 4) == 4


A, B, K = tuple(li())
count = 0
g = gcd(A, B)
can = set()
cnt = 0
for i in range(1, int(sqrt(g)) + 1):
    if g % i == 0:
        cnt += 1
        can.add(i)
        can.add(g // i)
        if cnt >= K:
            break

can = sorted(can, reverse=True)
print(can[K - 1])
