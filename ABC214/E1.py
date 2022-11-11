import sys
import collections
import bisect
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


def run1():
    N = ii()
    windows = []
    for i in range(N):
        l, r = li()
        windows.append((l, r))
    # lesser r side come first, because r is strongest restriction
    windows = sorted(windows, key=lambda lr: lr[1])
    used = set()
    for left, right in windows:
        target_box = left
        while target_box in used:
            target_box += 1
        if target_box > right:
            print("No")
            return
        used.add(target_box)
    # print(walls)
    print("Yes")


def run():
    Round = ii()
    for i in range(Round):
        run1()


if __name__ == '__main__':
    run()
