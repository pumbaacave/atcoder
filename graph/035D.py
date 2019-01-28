from loguru import logger
from collections import defaultdict
from heapq import heappush, heappop
import sys
stdin = sys.stdin


def li(): return map(int, stdin.readline().split())


def debug(*params):
    logger.debug(params)


class Solution(object):  # pylint: disable=too-few-public-methods
    def __init__(self):
        pass

    def dijkstra(self, distances, edge_dict):
        distances[0] = 0
        # cost to dest, dest_id
        sorted_q = [(0, 0)]
        searched = set()
        # suppose all edge cost are positive
        while sorted_q:
            cost_to_cur, cur = heappop(sorted_q)
            if cur in searched:
                continue
            else:
                searched.add(cur)

            for dest_cost in edge_dict[cur]:
                old_dis_to_nei = distances[dest_cost[0]]
                new_dis_to_nei = cost_to_cur + dest_cost[1]
                if old_dis_to_nei > new_dis_to_nei:
                    distances[dest_cost[0]] = new_dis_to_nei
                heappush(sorted_q, (distances[dest_cost[0]], dest_cost[0]))
        return distances

    def treasure_hunt(self, params, treasure_points, edges):
        num_towns, num_edges, time_limit = params
        distances = []
        rev_dis = []
        inf = float('INF')
        for _ in range(num_towns):
            # distances.append([inf for _ in range(num_towns)])
            distances.append(inf)
            rev_dis.append(inf)

        edge_dict = defaultdict(list)
        rev_edge_dict = defaultdict(list)
        for e in edges:
            # key:value :: source:(dest, dis)
            # -1 adjust idx
            edge_dict[e[0]-1].append((e[1]-1, e[2]))
            rev_edge_dict[e[1]-1].append((e[0]-1, e[2]))

        distances[0] = 0
        rev_dis[0] = 0
        distances = self.dijkstra(distances, edge_dict)
        rev_dis = self.dijkstra(rev_dis, rev_edge_dict)

        treasure = [(time_limit - distances[town_id] - rev_dis[town_id])
                    * treasure_points[town_id] for town_id in range(num_towns)]
        debug(distances)
        debug(rev_dis)
        debug(treasure)
        return max(treasure)
# params = tuple(li())
# treasure_points = tuple(li())
# edges = [tuple(li()) for _ in range(params[1])]
# s = Solution()
# print(s.treasure_hunt(params, treasure_points, edges))


def test_1():
    s = Solution()
    params = [2, 2, 3]
    treasure_points = [1, 3]
    edges = [
            [1, 2, 2],
            [2, 1, 1],
    ]
    assert 3 == s.treasure_hunt(params, treasure_points, edges)


test_1()


def test_2():
    s = Solution()
    params = [2, 2, 5]
    treasure_points = [1, 3]
    edges = [
            [1, 2, 2],
            [2, 1, 1],
    ]
    assert 6 == s.treasure_hunt(params, treasure_points, edges)


def test_3():
    s = Solution()
    params = [8, 5, 120]
    treasure_points = [1, 2, 6, 16, 1, 3, 11, 9]
    edges = [
            [1, 8, 1],
            [7, 3, 14],
            [8, 2, 13],
            [3, 5, 4],
            [5, 7, 5],
            [6, 4, 1],
            [6, 8, 17],
            [7, 8, 5],
            [1, 4, 2],
            [4, 7, 1],
            [6, 1, 3],
            [3, 1, 10],
            [2, 6, 5],
            [2, 4, 12],
            [5, 1, 30],
    ]
    assert 1488 == s.treasure_hunt(params, treasure_points, edges)
