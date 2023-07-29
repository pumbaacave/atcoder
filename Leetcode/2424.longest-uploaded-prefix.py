#
# @lc app=leetcode id=2424 lang=python3
#
# [2424] Longest Uploaded Prefix
#

# @lc code=start

# sort only when needed and possible
from heapq import heappush, heappop


class LUPrefix:

    def __init__(self, n: int):
        # buffer is a min heap
        self.buffer = []
        self._longest = 0

    def upload(self, video: int) -> None:
        # no general optimize but a quick path
        if video == self._longest + 1:
            self._longest += 1
            while self.buffer and self.buffer[0] == self._longest + 1:
                self._longest = heappop(self.buffer)

        else:
            heappush(self.buffer, video)

    def longest(self) -> int:
        return self._longest


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()
# @lc code=end
