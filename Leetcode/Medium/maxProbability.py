from heapq import heappop, heappush
from collections import defaultdict
from math import e, log


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        dis = [float('inf')] * n
        ch = defaultdict(list)
        for i, (l, r) in enumerate(edges):
            ch[r].append((l, succProb[i]))
            ch[l].append((r, succProb[i]))
        # dijstra

        visited = set()
        heap = []
        # - prob, point
        heappush(heap, (-1, start))

        while heap:
            dis, idx = heappop(heap)
            # end found
            if idx == end:
                return -dis
            if idx in visited:
                continue
            for nei, prob in ch[idx]:
                if nei in visited:
                    continue
                heappush(heap, (dis * prob, nei))
            visited.add(idx)
        else:
            return 0

