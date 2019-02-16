import sys
stdin = sys.stdin
def li(): return map(int, stdin.readline().split())
a, b = tuple(li())
div, mod = divmod(b, a)
if mod == 0:
    print(a + b)
else:
    print(b - a)
