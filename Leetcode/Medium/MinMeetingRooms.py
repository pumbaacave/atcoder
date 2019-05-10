import heapq
from collections import deque
from typing import *
class Solution1:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        num = 0
        intervals.sort(key=lambda x:x[0])
        # a pq
        sametime_rooms = []
        for s, e in intervals:
            num = max(num, len(sametime_rooms))
            # print(sametime_rooms)
            if not sametime_rooms:
                sametime_rooms.append(e)
            else:
                if sametime_rooms[0] <= s:
                    heapq.heappop(sametime_rooms)
                heapq.heappush(sametime_rooms, e)
        return max(num, len(sametime_rooms))

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        num = 0
        intervals.sort(key=lambda x:x[0])
        starts = sorted(x for x, y in intervals)
        ends = sorted(y for x, y in intervals)
        j = 0
        for i, s in enumerate(starts):
            if s >= ends[j]:
                j += 1
            num = max(num, i - j + 1)
        return num

import pytest

@pytest.mark.parametrize("intervals, min_rooms",[
    ([[6,17],[8,9],[11,12],[6,9]], 3),
    ([[8,14],[12,13],[6,13],[1,9]], 3),
    ([[9,16],[6,16],[1,9],[3,15]], 3),
    ([[2,15],[36,45],[9,29],[16,23],[4,9]], 2),
    ([[2,11],[6,16],[11,16]], 2),
    ([[0, 30],[5, 10],[15, 20]], 2),
    ([[7,10],[2,4]], 1),
    ([[13,15],[1,13]], 1),
    ([[7,10]], 1),
    ([[9,10],[4,9],[4,17]], 2),
    ([], 0)
    ])
def test_min_rooms(intervals, min_rooms):
    s = Solution()
    assert s.minMeetingRooms(intervals)== min_rooms

