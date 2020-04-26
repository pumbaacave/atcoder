"""
Definition for an Interval.
"""
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
class Solution:
    # do union and substract from full set
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = sorted((interval for person_sch in schedule
                                for interval in person_sch) 
                            , key=lambda iv: (iv.start, -iv.end))
        unions = []
        for interval in intervals:
            # not intersect case
            if not unions or unions[-1].end < interval.start:
                unions.append(interval)
            # intersect case
            else:
                unions[-1].end = max(unions[-1].end, interval.end)
        emptys = []
        last = None
        for union in unions:
            if not last:
                last = union
            else:
                emptys.append(Interval(last.end, union.start))
                last = union
        return emptys