import sys
stdin = sys.stdin
def li(): return map(int, stdin.readline().split())

N, M = tuple(li())
common = set(range(1,M+1))
for _ in range(N):
    answer = tuple(li())
    favs = set(answer[1:])
    common = common.intersection(favs)
print(len(common))

