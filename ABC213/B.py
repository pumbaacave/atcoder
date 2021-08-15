import sys
import collections
import heapq
stdin = sys.stdin

sys.setrecursionlimit(10**5)


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
    q = []
    N = ii()
    nums = list(li())
    for num in nums:
        q.append(num)
    one, two = heapq.nlargest(2, q)
    print(nums.index(two) + 1)


if __name__ == '__main__':
    run()
