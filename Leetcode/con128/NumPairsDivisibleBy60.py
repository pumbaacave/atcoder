from collections import Counter
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # preprocess
        L = len(time)
        for i in range(L):
            time[i] %= 60

        cnt = Counter(time)
        total = 0
        for t in time:
            # t == 0 is special
            if t == 0:
                cnt[t] -= 1
                total += cnt[t]
            else:
            # decr self cnt first
                cnt[t] -= 1
                total += cnt[60 - t]
        return total
