# definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        intervals.sort(key=lambda x:(x.start, x.end))
        merged = []
        for i in intervals:
            if not merged:
                merged.append(i)
            else:
                # not overlap
                if i.start > merged[-1].end:
                    merged.append(i)
                else:
                    merged[-1].end = max(i.end, merged[-1].end)
        return merged
