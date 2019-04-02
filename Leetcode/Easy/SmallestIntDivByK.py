class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0:
            return -1

        cnt = 1
        seen = set()
        # find 1...1 > K
        cmp = 1
        def find_cmp(cmp, cnt):
            while cmp < K:
                cmp = 10 * cmp + 1
                cnt += 1
            return cmp, cnt
        cmp, cnt = find_cmp(cmp, cnt)

        # try find target num
        mod = 1
        while mod:
            mod = cmp % K
            if mod in seen:
                return -1
            elif mod == 0:
                return cnt
            else:
                seen.add(mod)
                cmp = mod
                cmp, cnt = find_cmp(cmp, cnt)
        return cnt
