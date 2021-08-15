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
    # init with empty window
    walls = [0, 2 ** 31]
    for left, right in windows:
        idx = 0
        while True:
            idx = bisect.bisect_left(walls, left, lo=idx)
            if walls[idx] > left:
                walls.insert(idx, left)
                break
            else:
                # walls[idx] == left
                left += 1
                if left > right:
                    print("No")
                    return
    # print(walls)
    print("Yes")


def run():
    Round = ii()
    for i in range(Round):
        run1()


if __name__ == '__main__':
    run()
