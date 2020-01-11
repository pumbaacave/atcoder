import heapq


class ExamRoom:

    def dis(self, l, r):
        return (r - l) // 2 - l
    def __init__(self, N: int):
        # len_interval, start_idx, end_idx
        self.l = 0
        self.r = N-1
        self.le = 0
        self.la = N - 1
        self.intervals = [(-self.dis(0, N-1), 0, N-1)]

    def seat(self) -> int:
        pq = self.intervals
        i, l, r = heapq.heappop(pq)
        idx = (l + r) // 2
        heapq.heappush(pq, (l - idx, l , idx))
        heapq.heappush(pq, (idx - r, idx , r))
        return idx

    def leave(self, p: int) -> None:
        pq = self.intervals
        def get_del_list():
            del_list = []
            for i, data in enumerate(pq):
                if p in data[1:]:
                    del_list.append(i)
            return del_list

        if p in (self.l, self.r):
            del_list = get_del_list()
            del pq[del_list[0]]
            heapq.heapify(pq)
            return

        del_list = get_del_list()
        data1 = list(pq[del_list[0]][1:])
        data2 = list(pq[del_list[1]][1:])
        a, b, c = sorted(set(data1 + data2))
        del pq[del_list[1]]
        del pq[del_list[0]]
        pq.append( (-self.dis(a, c), a, c) )
        heapq.heapify(pq)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
