import sys
stdin = sys.stdin
def li(): return map(int, stdin.readline().split())
N, L = tuple(li())
total = N * (L + N + L - 1) // 2
delta = 1 - L
if delta < 1:
    print(total - L)
elif delta > N:
    print(total - (L - 1 + N))
else:
    print(total)
