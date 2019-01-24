"""
https://abc036.contest.atcoder.jp/tasks/abc036_d#
問題文
N 個の島があります。 島には 1 から N までの番号がついています。 また、N−1 個の橋があります。 i 番目の橋は ai 番の島と bi 番の島をつないでいます。 どの島からどの島へも橋をいくつか経由して到達できることがわかっています。 

すぬけ君は、それぞれの島を白または黒に塗ることにしました。 ただし、両端の島が黒で塗られているような橋があってはいけません。 色の塗り方が何通りあるか、109+7 で割った余りを求めてください。
制約
2≤N≤105
1≤ai,bi≤N
どの島からどの島へも橋をいくつか経由して到達できる

"""

# from loguru import logger
from itertools import chain
from functools import reduce
from collections import Counter, deque
class WBTree(object):
    class Node(object):
        def __init__(self, children=[]):
            self.children = children

        def white(self):
            if not self.children:
                return 2
            else:
                return reduce(lambda x, y: x * y , [c.white() for c in self.children])
        def black(self):
            if not self.children:
                return 1
            else:
                return reduce(lambda x, y: x + y , [c.black() for c in self.children])

    def __init__(self, bridge_list):
        pass

def cal(N, bridges):
    bridge_cnt = Counter()
    bw_list = [[0,0] for _ in range(N+1)]
    con_list = [[] for _ in range(N+1)]
    for l, r in bridges:
        bridge_cnt[r] += 1
        bridge_cnt[l] += 1
        con_list[l].append(r)
        con_list[r].append(l)

    # logger.debug(bridge_cnt)
    sorted_c = sorted(bridge_cnt, key=lambda key: bridge_cnt[key]) # cnt min first

    max_iland = sorted_c[-1]
    sentinel = object()
    ite = chain((key for key in sorted_c), [sentinel])


    def cal_bw(nxt):
        # parent cnt > child cnt
        # so parent bw_value is [0,0]
        # logger.debug(nxt)
        bw_list[nxt][0] = reduce(lambda x,y: x*y, [bw_list[con][1] for con in con_list[nxt] if bw_list[con][0] > 0])
        bw_list[nxt][1] = reduce(lambda x,y: x*y, [bw_list[con][1] + bw_list[con][0] for con in con_list[nxt] if bw_list[con][1] > 0])
        return sum(bw_list[nxt])

    leaves = []
    parent_queue = []
    for nxt in ite:
        if bridge_cnt[nxt] > 1:
            break
        else:
            bw_list[nxt][0] = 1 #cal black value
            bw_list[nxt][1] = 1 #cal white value
            parent = con_list[nxt].pop()
            parent_queue.append(parent)

    parent_queue= deque(sorted(parent_queue, key=lambda k:bridge_cnt[k]))
    logger.debug(parent_queue)
    holder = 0
    while parent_queue:
        op = parent_queue.popleft()

        # logger.debug(parent_queue)
        # logger.debug(con_list[op])
        if bw_list[op][0] > 0:
            continue
        empty_count = [bw_list[i][0] == 0 for i in con_list[op]]
        # logger.debug(empty_count)
        if sum(empty_count) <= 1:
            parent_queue.extend(con_list[op])
            temp = cal_bw(op)
            holder = max(holder, temp)
            logger.debug(f'operand: {op}  bw_list:{bw_list[op]}')
        else:
            parent_queue.extend(con_list[op])
            parent_queue.append(op)


    # logger.debug(bw_list)
    return holder % 10 ** 9


def test_sample1():
    N = 5
    bridges = [
            [2, 5],
            [1, 5],
            [2, 4],
            [3, 2]
            ]
    assert  14 == cal(N, bridges)

def test_sample2():
    N = 10
    bridges = [
            [7, 9],
            [8, 1],
            [9, 6],
            [10, 8],
            [8, 6],
            [10, 3],
            [5, 8],
            [4, 8],
            [2, 5],
            ]
    assert  192 == cal(N, bridges)

