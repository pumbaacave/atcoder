import sys
stdin = sys.stdin

def li(): return map(int, stdin.readline().split())

A, B, C = tuple(li())
times = B // A
print(min(times, C))
