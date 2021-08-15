import sys
import collections
stdin = sys.stdin

# sys.setrecursionlimit(10**5)


def ii(): return int(stdin.readline())


def li(): return map(int, stdin.readline().split())


def li_(): return map(lambda x: int(x)-1, stdin.readline().split())


def lf(): return map(float, stdin.readline().split())


def ls(): return stdin.readline().split()


def ns(): return stdin.readline().rstrip()


def lc(): return list(ns())


def ni(): return int(stdin.readline())


def nf(): return float(stdin.readline())



def run():
    global N
    N = ii()
    nei = collections.defaultdict(list)
    for i in range(N-1):
        l, r = li()
        nei[l].append(r)
        nei[r].append(l)
    for i in range(len(nei)):
        nei[i+1].sort()
    seen = set([1])
    ret = [1]
    dfs(1, seen, nei, ret)
    print(ret)


def dfs(cur, seen, nei, ret):
    global N
    for n in nei[cur]:
        if(len(seen) == N):
            break
        if n in seen:
            continue
        ret.append(n)
        seen.add(n)
        dfs(n, seen, nei, ret)
        ret.append(cur)


if __name__ == '__main__':
    run()
