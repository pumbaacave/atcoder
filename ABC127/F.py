import heapq
import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def ii(): return int(stdin.readline())
def li(): return map(int, stdin.readline().split())
Q = ii()
points = []
cons = 0
def update(_opcode, point, delta):
    global cons
    cons += delta
    points.append(point)

def cal():
    points.sort()
    w = 0
    l, r = 0, len(points) - 1
    while l < r:
        w += (points[r] - points[l])
        l += 1
        r -= 1
    print("{} {}".format(points[l - 1], w + cons))

for _ in range(Q):
    ops = tuple(li())
    if len(ops) == 3:
        update(*ops)
    else:
        cal()
