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
    S0, T = li()
    S = S0 + 1
    cnt = 0
    for a in range(0, S):
        for b in range(0, S):
            for c in range(0, S):
                if a + b + c > S0:
                    break
                if a * b * c <= T:
                    cnt += 1
    print(cnt)


if __name__ == '__main__':
    run()
