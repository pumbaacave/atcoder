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
 
n,k = li()
td = [tuple(li()) for _ in range(n)]

def cal_score(N, K, records):
    sorted_recs = sorted(records, key=lambda x: -x[1])
    target_queue = deque(sorted_recs[0:K]) # only allow pop() action, so use dequeue
    # logger.debug(target_queue)
    compare_queue = deque(sorted_recs[K:])
    count = Counter()
    for neta_point in target_queue:
        count[neta_point[0]] += 1
    # logger.debug(count)

    cardinality = len(count.keys())
    sum_target_points = sum([n_p[1] for n_p in target_queue])
    score = pow(cardinality, 2) + sum_target_points
    score = int(score)
    new_scores = deque()
    new_scores.append(score)
    # start iteration and comparing gain and lost
    while compare_queue:
        comp = compare_queue.popleft()
        # buggy
        # if comp[0] in count:
        if count[comp[0]] > 0:
            continue
        while target_queue:
            old = target_queue.pop()
            if count[old[0]] < 2:
                # swap this neta will not increase cardinality but lower neta point
                continue
            else: # check if score will go up
                inc = 2 * cardinality + 1
                dec = old[1] - comp[1]
                delta = inc - dec
                # logger.debug(f"delta is {delta}")
                # if delta >= 0:
                #     logger.debug("SOME")
                #     logger.debug(f"{old} out")
                #     logger.debug(f"{comp} in")
                #     cardinality += 1
                #     score += delta
                #     count[old[0]] -= 1
                #     count[comp[0]] +=1
                # else: #increase cardinality will bring more lost than gain
                #     # exit here
                #     return score
                new_score = new_scores[-1] + delta
                new_scores.append(new_score)

                cardinality += 1
                count[old[0]] -= 1
                count[comp[0]] +=1
    # both queues are drained
    return max(new_scores)


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
