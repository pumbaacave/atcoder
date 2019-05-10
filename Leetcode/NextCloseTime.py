from bisect import bisect_right
class Solution:
    def nextClosestTime(self, time: str) -> str:
        def output(h1, h2, m1, m2):
            return ''.join(list(map(str, [h1, h2, ':', m1, m2])))

        h1, h2, _, m1, m2 = list(time)
        h1, h2 , m1, m2 = int(h1), int(h2), int(m1), int(m2)
        cans = sorted([h1, h2, m1, m2])
        lower = min(cans)
        # m2 [0,9]
        idx =  bisect_right(cans, m2)
        if idx < 4:
            return output(h1, h2, m1, cans[idx])

        idx1 = bisect_right(cans, m1)
        if idx1 < 4 and cans[idx1] < 6:
            return output(h1, h2, cans[idx1], lower)
        idx2 = bisect_right(cans, h2)
        # not carry
        if idx2 < 4 and ((h1 < 2) or (h1 == 2 and cans[idx2] < 4)):
            return output(h1, cans[idx2], lower, lower)
        idx3 = bisect_right(cans, h1)
        if idx3 < 4 and cans[idx3] < 3:
            return output(cans[idx3], lower, lower, lower)
        else:
            return output(lower, lower, lower, lower)
        

