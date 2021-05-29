from bisect import bisect_left


class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        cap = 10 ** 5 + 1
        total = 0
        freqs = [0] * (2 * cap)
        high = 0
        for n in nums:
            high = max(n, high)
            freqs[n] += 1
        # precomute accumuative sum
        for i, f in enumerate(freqs[1:], start=1):
            freqs[i] = f + freqs[i-1]

        memo = {}
        for n in nums:
            if n in memo:
                total += memo[n]
                total %= mod
                continue
            # assume n > 0
            multiple = 1
            last = n
            before = total
            while last <= high:
                count = freqs[last + n - 1] - freqs[last - 1]
                total += count * multiple
                total %= mod
                multiple += 1
                last += n
            memo[n] = total - before
        return total
