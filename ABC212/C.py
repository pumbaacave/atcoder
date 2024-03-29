import sys
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

# n,k = li()
# td = [tuple(li()) for _ in range(n)]

def run():
    M, N = li()
    A = sorted(li())
    B = sorted(li())
    delta = float('INF')
    l, r = 0, 0
    while l < len(A) and r < len(B):
        delta = min(delta, abs(A[l] - B[r]))
        if A[l] <= B[r]:
            l += 1
        else:
            r +=1

    # similar to merge sort
    print(delta)


if __name__ == '__main__':
    run()
