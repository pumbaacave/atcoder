import sys
stdin = sys.stdin
def li(): return map(int, stdin.readline().split())
N = li()
A = list(li())

def gcd(A, B):

    # normal gcd logic
    while B not in (1, 0):
        A, B = (A, B) if A > B else (B, A)
        _, mod = divmod(A, B)
        A, B = B, mod
    if B == 0:
        return A
    elif B == 1:
        return 1

A = list(filter(lambda x:x>0, A))
A.sort()
if len(A) == 0:
    print(0)
else:
    res = A[0]
    for a in A:
        res = gcd(a, res)
        if res == 1:
            break

    print(res)

def test_gcd():
    assert gcd(1, 1) == 1
    assert gcd(5, 3) == 1
    assert gcd(4, 2) == 2
