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


def key(l, r):
    if r < l:
        return (r, l)
    else:
        return (l, r)


def run():
    # dfs
    N = ii()
    nei = collections.defaultdict(list)
    w = collections.defaultdict(int)
    for i in range(N-1):
        a, b, c = li()
        nei[b].append(a)
        nei[a].append(b)
        w[key(a, b)] = c
    q = collections.deque([1])
    # all node in left
    lefts = set()
    while q:
        cur = q.popleft()
        # already processed as pivot node
        # all touched node put in left, ensure coverage
        lefts.add(cur)
        for right in nei[cur]:
            # a->b and nei[b] has a
            if right in lefts:
                continue
            cur_wei = w[key(cur, right)]
            # for new node, caculate max seen weight
            for left in lefts:
                # allow cur == left ?
                if left == cur:
                    continue
                if right == left:
                    continue
                seen_wei = w[key(cur, left)]
                w[key(right, left)] = max(cur_wei, seen_wei)
            # push right as new pivot node
            q.append(right)
            lefts.add(right)
    #for k, v in w.items():
    #    print(k, v)
    print(sum(w.values()))


if __name__ == '__main__':
    run()
