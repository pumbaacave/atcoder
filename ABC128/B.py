from collections import defaultdict
import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def ii(): return int(stdin.readline())
def li(): return map(int, stdin.readline().split())
def ls(): return stdin.readline().split()
N = ii()
city_r = defaultdict(list)
for i in range(1, N + 1):
    c, s = ls()
    s = int(s)
    city_r[c].append( (s, i) )
keys = sorted(city_r.keys())
for k in keys:
    vs = city_r[k]
    vs.sort(key=lambda x:-x[0])
    for v in vs:
        print(v[1])

