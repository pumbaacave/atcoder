
import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def li(): return int(stdin.readline())

a = li()
b = li()
c = li()
d = li()
e = li()
k = li()
if e - a > k:
    print(":(")
else:
    print("Yay!")
