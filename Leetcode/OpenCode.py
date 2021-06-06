from typing import List
from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        """
        Backtracking: all state inter dependant.
        """
        self.blocker = set(int(d) for d in deadends)
        # glable var
        self.target = int(target)
        inf = float('inf')
        self.dist = defaultdict(lambda: inf)
        self.bfs()
        print(self.dist[self.target])
        return self.dist[self.target]

    def bfs(self):
        heap = [(0, 0)]
        while heap:
            step, cur = heappop(heap)
            if cur in self.blocker:
                continue
            if self.dist[cur] <= step:
                continue
            self.dist[cur] = step
            if cur == self.target:
                # stop walking
                continue
            heappush(heap, (step + 1, (cur + 1) % 10000))
            heappush(heap, (step + 1, (cur + 10) % 10000))
            heappush(heap, (step + 1, (cur + 100) % 10000))
            heappush(heap, (step + 1, (cur + 1000) % 10000))
            a = cur - 1
            if a < 0:
                a + 10
            heappush(heap, (step + 1, (a) % 10000))
            b = cur - 10
            if b < 0:
                b + 100
            heappush(heap, (step + 1, (b) % 10000))
            c = cur - 100
            if c < 0:
                c + 1000
            heappush(heap, (step + 1, (c) % 10000))
            d = cur - 1000
            if d < 0:
                d + 10000
            heappush(heap, (step + 1, (d) % 10000))

    def dfs(self, cur: int, step: int):
        if cur in self.blocker:
            return
        # no possible improvement
        if self.dist[cur] < step:
            return
        # update minimum distance to reach the node
        self.dist[cur] = step
        if cur == self.target:
            return
        next_step = step + 1
        self.dfs((cur + 1) % 10000, next_step)
        self.dfs((cur + 10) % 10000, next_step)
        self.dfs((cur + 100) % 10000, next_step)
        self.dfs((cur + 1000) % 10000, next_step)
        self.dfs((cur - 1) % 10000, next_step)
        self.dfs((cur - 10) % 10000, next_step)
        self.dfs((cur - 100) % 10000, next_step)
        self.dfs((cur - 1000) % 10000, next_step)

    def find_min_step_for_right(self, unit, base):
        if unit == 0:
            # down from unit == 1, shoud end
            return 0
        mod = 10 * unit
        # 0 ~ 9
        local_target = (self.target % mod) // unit
        print(f"unit {unit}, local_target {local_target}")
        forward = backward = float('inf')
        # else continue to next step


if __name__ == "__main__":
    s = Solution()
    # s.openLock(["8888"], "0324")
    s.openLock(["8888"], "0009")
    # s.openLock(["0201", "0101", "0102", "1212", "2002"], "0202")
