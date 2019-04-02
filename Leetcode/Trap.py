class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        last = -1
        stairs = []

        def add_water(total, last, stairs):
            for s in stairs:
                total += last - s
            return total, []

        for h in height:
            if h >= last:
                # cal water
                total, stairs = add_water(total, last, stairs)
                # update last
                last = h
            else:
                # add stairs can hold water
                stairs.append(h)
        # TODO: process remaining stairs
        if stairs:
            total += self.trap(reversed([last] + stairs))
        return total
