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

def find_parent(idx, parents):
    p = parents[idx]
    if p == idx:
        return p
    else:
        return find_parent(p, parents)


def run():
    # dfs
    N = ii()
    nei = collections.defaultdict(list)
    # weight -> left_right
    w = list()
    for i in range(N-1):
        a, b, c = li()
        nei[b].append(a)
        nei[a].append(b)
        w.append((c, key(a, b)))
    # increasing on weight
    w.sort()
    # Union find
    # id -> parent_id
    parents = dict()
    # id -> group_size
    # only group_size at parent id is consistent(correct)
    size = dict()
    for i in range(1, N+1):
        parents[i] = i
        size[i] = 1
    total_weight = 0
    for weight, (left, right) in w:
        left_group = find_parent(left, parents)
        right_group = find_parent(right, parents)
        size_l = size[left_group]
        size_r = size[right_group]
        total_weight += weight * (size_l * size_r)
        # merge Union
        if size_l < size_r:
            left_group, right_group = right_group, left_group
            size_l, size_r = size_r, size_l
        parents[right_group] = left_group
        size[left_group] += size_r
        
    print(total_weight)


if __name__ == '__main__':
    run()
