class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        tss = set()
        def to_timestamp(timePoint):
            return int(timePoint[:2]) * 60 + int(timePoint[3:])
        for tp in timePoints:
            formatted_tp = to_timestamp(tp)
            if formatted_tp in tss:
                return 0
            tss.add(formatted_tp)
        sorted_tss = sorted(tss)
        last = sorted_tss[0]
        # only one possible underflow
        delta = sorted_tss[0] - sorted_tss[-1]
        thr = 24 * 60
        if delta < 0:
            delta += thr

        for ts in sorted_tss[1:]:
            delta = min(delta, ts - last)
            last = ts
        return delta
        