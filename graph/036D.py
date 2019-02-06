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

from loguru import logger
from itertools import chain
from functools import reduce
from collections import Counter, deque
import weakref
class WBTree(object):
    class Node(object):
        def __init__(self, children_ids=[], node_id=0, parent_id=0, tree=None):
            self.children_ids = children_ids
            self.children = []
            self.parent_id = parent_id
            self.node_id = node_id
            self.tree = weakref.ref(tree)
            [self.children.append(WBTree.Node(filter(lambda x:x != node_id, self.tree().con_list[c_id]), c_id, node_id, tree)) \
                    for c_id in self.children_ids]


        def white(self):
            if not self.children:
                return 1
            else:
                return reduce(lambda x, y: x * y , [c.white() + c.black() for c in self.children])
        def black(self):
            if not self.children:
                return 1
            else:
                return reduce(lambda x, y: x * y , [c.white() for c in self.children])
        def __repr__(self):
            return ' '.join(chain('value {}\n'.format(self.node_id), [repr(child) for child in self.children]))

        def comb(self):
            return self.black() + self.white()

    def __init__(self, N, bridges):
        bridge_cnt = Counter()
        bw_list = [[0,0] for _ in range(N+1)]
        con_list = [[] for _ in range(N+1)]
        for l, r in bridges:
            bridge_cnt[r] += 1
            bridge_cnt[l] += 1
            con_list[l].append(r)
            con_list[r].append(l)
        self.bw_list = bw_list
        self.con_list = con_list
        sorted_c = sorted(bridge_cnt, key=lambda key: bridge_cnt[key]) # cnt min first
        root_id = sorted_c[-1]
        self.root = WBTree.Node(filter(lambda x:x!=root_id, con_list[root_id]), root_id, parent_id=0, tree=self)
    def __repr__(self):
        return repr(self.root)

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
    tree = WBTree(N, bridges)
    assert  14 == tree.root.comb()

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
    tree = WBTree(N, bridges)
    assert  192 == tree.root.comb()

test_sample2()