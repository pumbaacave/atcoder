import bisect
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        ls = len(stones)
        if not stones: return 0
        if ls == 1: return stones[0]
        if ls == 2: return abs(stones[1] - stones[0])
        vals = set()
        vals.add(0)
        total = sum(stones)
        for s in stones:
            new_vs = set()
            for v in vals:
                new_vs.add(s+v)
            vals = vals.union(new_vs)
        pos = list(vals)
        pos.sort()
        idx = bisect.bisect_left(pos, total//2)
        del1 = abs(total - 2 * pos[idx])
        del2 = abs(total - 2 * pos[idx + 1])
        return min(del1, del2)


