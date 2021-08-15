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
    H, W, N = li()
    row_set = set()
    col_set = set()
    nums = []
    for i in range(N):
        A, B = li()
        nums.append((A, B))
        row_set.add(A)
        col_set.add(B)
    row_ord = {val: idx + 1 for idx, val in enumerate(sorted(row_set))}
    col_ord = {val: idx + 1 for idx, val in enumerate(sorted(col_set))}
    for num in nums:
        print('{} {}'.format(row_ord[num[0]], col_ord[num[1]]))
    
    


if __name__ == '__main__':
    run()
