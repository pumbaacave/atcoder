MOD = 10 ** 9 + 7
class Solution:
    def numDecodings(self, s: str) -> int:
        self.digits = set(str(d) for d in range(1, 27))
        self.memo = dict()
        cnt = self.backtrack(s, 0)
        return cnt

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
        elif first == '*':
            cnt += 9 * self.backtrack(s, idx + 1)

        if idx + 1 < len(s):
            second = s[idx+1]
            token = ''.join([first, second])
            if token in self.digits:
                cnt += self.backtrack(s, idx + 2)
            elif token == '1*': # case A
                cnt += 9 * self.backtrack(s, idx + 2)
            elif token == '2*': # case B
                cnt += 6 * self.backtrack(s, idx + 2)
            elif token == '**': # case A + B
                cnt += 15 * self.backtrack(s, idx + 2)
            elif first == '*':
                # 11, 21
                if int(second) < 7:
                    cnt += 2 * self.backtrack(s, idx + 2)
                # 18
                else:
                    cnt += self.backtrack(s, idx + 2)

        cnt = cnt % MOD
        self.memo[idx] = cnt
        return cnt
