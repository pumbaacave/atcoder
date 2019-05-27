class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        if not words:
            return 0
        def is_pre(p, s):
            lp = len(p)
            if lp + 1 != len(s):
                return False
            i, j = 0, 0
            bail_one = True
            for i in range(lp):
                if p[i] == s[j]:
                    j += 1
                elif bail_one:
                    bail_one = False
                    if p[i] != s[j+1]:
                        return False
                    else:
                        j += 2
                else:
                    return False
            return True
        lw = len(words)
        words.sort(key=lambda x:len(x))
        dp = [1] * lw
        for i in range(lw):
            if len(words[i]) == 1:
                continue

            d = max([dp[j] for j in range(i) if is_pre(words[j], words[i])] or [0]) + 1
            dp[i] = d
        return max(dp)
