import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        for s in stones:
            heapq.heappush(pq, (-s , s))
        while len(pq) > 1:
            f, fv = heapq.heappop(pq)
            s, sv = heapq.heappop(pq)
            if fv != sv:
                val_abs = abs(sv - fv)
                heapq.heappush(pq, (-val_abs , val_abs))
        if len(pq) == 1:
            return pq[-1][1]
        else:
            return 0

