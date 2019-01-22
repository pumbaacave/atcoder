from math import pow
from collections import deque
from loguru import logger


# N, K = map(int, input().split())
# records = [tuple(map(int, input().split())) for i in range(N)]


def compute_score(target_collection):
    keys = {neta_point[0] for neta_point in target_collection}
    points = [neta_point[1] for neta_point in target_collection]
    cardinality = len(keys)
    score = pow(cardinality, 2) + sum(points)
    return score

# exchange one record and compare
def optimize(full_collection, target_collection, target_collection_len, forward_idx):
    backward_idx = forward_idx - 1
    while True:
        logger.debug(forward_idx)
        logger.debug(target_collection)
        # check on the forward_idx-th record
        ex_record = full_collection[forward_idx]
        # bump up for return value
        forward_idx += 1
        score =  compute_score(target_collection)
        if ex_record in target_collection:
            continue # cardinality score will not increase
        else:
            while True:
                if backward_idx < 1:
                    logger.debug(target_collection)
                    return score
                if target_collection[backward_idx][0] != target_collection[backward_idx-1][0]:
                    backward_idx -= 1
                else:
                    target_collection[backward_idx] = ex_record
                    new_score = compute_score(target_collection)
                    backward_idx -= 1
                    if new_score >= score:
                        score = new_score
                        break
                    else:
                        logger.debug(target_collection)
                        return score


def cal_score(N, K, records):
    sorted_recs = sorted(records, reverse=True, key=lambda x: x[1])
    target_collection = deque(sorted_recs[0:K])

    # optimzie at most K times
    idx = K
    score = optimize(sorted_recs, target_collection, K, idx)
    return int(score)

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
