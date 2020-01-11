import sys
stdin = sys.stdin
def ls(): return stdin.readline()

def li(): return map(int, stdin.readline().split())
N, K = tuple(li())
S = ls()
sl = []
for i, c in enumerate(S):
    if i == K -1:
        sl.append(c.lower())
    else:
        sl.append(c)

print(''.join(sl))
