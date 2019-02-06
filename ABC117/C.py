import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def li(): return map(int, stdin.readline().split())
N, M = tuple(li())
coods = list(li())
if len(coods) == 1:
    print(0)
elif N >= M:
    print(0)
else:

    coods = sorted(coods)
    deltas = []
    former = coods[0]
    for cood in coods:
        delta = cood - former
        deltas.append(delta)
        former = cood

    deltas = sorted(deltas, reverse=True)
    total_dis = coods[-1] - coods[0]
    for i in range(N-1):
        total_dis -= deltas[i]

    print(total_dis)

