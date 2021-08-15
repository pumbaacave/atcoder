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
    N = ii()
    S = list(li())
    T = list(li())
    ret = [0] * N
    min_T = min(T)
    start = T.index(min_T)
    time_to_pass = min_T
    for i in range(start, N):
        received = T[i]
        ret[i] = min(received, time_to_pass)
        time_to_pass = ret[i] + S[i]
    for i in range(start):
        received = T[i]
        ret[i] = min(received, time_to_pass)
        time_to_pass = ret[i] + S[i]
    for n in ret:
        print(n)


if __name__ == '__main__':
    run()
