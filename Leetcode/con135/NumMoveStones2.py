class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        # min: num_interval
        # max: sum(intervals) - min(end_interval)
        stones.sort()
        # len >= 3
        num_interval, sum_intervals = 0, 0
        len_s = len(stones)
        for i in range(len_s - 1):
            interval = stones[i + 1] - stones[i]
            if interval > 1:
                num_interval += 1
                sum_intervals += interval - 1
        l_i = stones[1] - stones[0] - 1
        r_i = stones[-1] - stones[-2] - 1
        if num_interval == 0:
            num_interval = 0
        elif num_interval == 1:
            num_interval = 1 if sum_intervals == 1 else 2
        else:
            num_interval -= 1
        return [num_interval, sum_intervals - min(l_i, r_i)]
