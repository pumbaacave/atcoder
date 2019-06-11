from collections import Counter
import heapq
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        cnt = Counter(barcodes)
        pq = []
        for k, v in cnt.items():
            heapq.heappush(pq, [-v, k])
        ret = []
        while pq:
            f = heapq.heappop(pq)
            if not pq:
                ret.append(f[1])
                break
            s = heapq.heappop(pq)
            if not ret:
                ret.append(f[1])
                ret.append(s[1])
            else:
                if f[1] == ret[-1]:
                    f, s = s, f
                ret.append(f[1])
                ret.append(s[1])
            f[0] += 1
            s[0] += 1
            if s[0] < 0:
                heapq.heappush(pq, s)
            if f[0] < 0:
                heapq.heappush(pq, f)
        return ret
