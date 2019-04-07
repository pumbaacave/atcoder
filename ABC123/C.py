

import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def li(): return int(stdin.readline())

N = li()
a = li()
b = li()
c = li()
d = li()
e = li()

bottle_neck = min([a, b, c, d, e])
red = (N - 1) // bottle_neck
print(5 + red)
