import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def ii(): return stdin.readline()
num = ii()
def do():
    for i in range(1,4):
        if num[i] == num[i - 1]:
            return "Bad"
    else:
        return "Good"
print(do())
