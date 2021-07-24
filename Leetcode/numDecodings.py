from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        self.digits = set(str(d) for d in range(1, 27))
        self.memo = dict()
        cnt =  self.backtrack(s, 0)
        return cnt

    @cache
    def backtrack(self, s:str, idx: int) -> int:
        key = idx
        if key in self.memo:
            return self.memo[key]
        if idx > len(s):
            return 0
        if idx == len(s):
            return 1
        # idx < len(s)
        first = s[idx]
        cnt = 0
        if first in self.digits:
            cnt += self.backtrack(s, idx + 1)
        if idx + 1 < len(s):
            second = s[idx+1]
            if ''.join([first, second]) in self.digits:
                cnt += self.backtrack(s, idx + 2)
        self.memo[idx] = cnt
        return cnt