
import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def li(): return int(stdin.readline())

a = li()
b = li()
c = li()
d = li()
e = li()
total = 0
delta = 0
for elem in [a, b, c, d, e]:
    mod = elem % 10
    if mod == 0:
        total += elem
    else:
        d = 10 - mod
        total += elem + d
        delta = max(delta, d)
print(total - delta)
