import heapq
class Solution:
    def kClosest(self, points, k):
        pq = []
        for x, y in points:
            dis = x ** 2 + y ** 2
            heapq.heappush(pq, [-dis, [x, y]])
            k -= 1
            while k < 0:
                heapq.heappop(pq)
                k += 1
        return [item[1] for item in pq]

