from math import pow
from collections import deque, Counter
# from loguru import logger
import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
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

def cal_score(N, K, records):
    sorted_recs = sorted(records, key=lambda x: -x[1])
    target_queue = deque(sorted_recs[0:K]) # only allow pop() action, so use dequeue
    compare_queue = deque(sorted_recs[K:])
    distinct_set = set()
    dup_queue = deque()
    score = 0
    for neta_point in target_queue:
        score += neta_point[1]
        if neta_point[0] not in distinct_set:
            distinct_set.add(neta_point[0])
        else:
            dup_queue.append(neta_point)

    cardinality = len(distinct_set)
    score += pow(cardinality, 2)
    score = int(score)
    maybe_score = score
    # start iteration and comparing gain and lost
    while compare_queue:
        comp = compare_queue.popleft()
        if comp[0] in distinct_set:
            continue
        elif len(dup_queue) < 1:
            break
        else:
            old = dup_queue.pop()
            inc = 2 * len(distinct_set) + 1
            dec = old[1] - comp[1]
            delta = inc - dec
            maybe_score = maybe_score + delta
            score = max(score, maybe_score)

            distinct_set.add(comp[0])
    # both queues are drained
    return score


def test_sample1():
    N = 5
    K = 3
    records = [
            [1, 9],
            [1, 7],
            [2, 6],
            [2, 5],
            [3, 1],
            ]
    score = cal_score(N, K, records)
    assert score == 26


def test_sample2():
    N = 7
    K = 4
    records = [
            [1, 1],
            [2, 1],
            [3, 1],
            [4, 6],
            [4, 5],
            [4, 5],
            [4, 5],
            ]
    score = cal_score(N, K, records)
    assert score == 25


def test_sample3():
    N = 6
    K = 5
    records = [
            [5, 1000000000],
            [2, 990000000],
            [3, 980000000],
            [6, 970000000],
            [6, 960000000],
            [4, 950000000],
            ]
    score = cal_score(N, K, records)
    assert score == 4900000016
