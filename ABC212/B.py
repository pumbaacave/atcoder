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


weak_str = "Weak"


def run():
    line = ns()
    if len(set(list(line))) == 1:
        print(weak_str)
        return
    last = None
    for num in map(int, list(line)):
        if last is not None and last != num:
            print("Strong")
            return
        # prepare next last
        last = (num + 1) % 10
    print(weak_str)


if __name__ == '__main__':
    run()
