
import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def li(): return map(int, stdin.readline().split())
A, B = tuple(li())
if A > 8 or B > 8:
    print(":(")
else:
    print("Yay!")
