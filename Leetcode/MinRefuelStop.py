class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # maximum fuel gain with ever stops
        fuels = [startFuel]
        if startFuel >= target:
            return 0
        for dis, fuel_add in stations:
            # (TODO)should stop update for not reachable stops?
            if all(f < dis for f in fuels):
                return -1
            new_f = [startFuel]
            fuels.append(fuels[-1] + fuel_add)
            for f, next_f in zip(fuels, fuels[1:]):
                # not enough fuel to reach
                if f >= target:
                    new_f.append(f)
                    break
                else:
                    new_f.append(max(next_f, f + fuel_add))
            fuels = new_f
        for i, f in enumerate(fuels):
            if f >= target:
                # least stops
                return i
        return -1
