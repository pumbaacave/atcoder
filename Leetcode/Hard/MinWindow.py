from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # not all test cases passed
        if s == t:
            return s
        t = Counter(t)
        seen = Counter()
        retl, retr = 0, 0
        l = 0
        ret = 2 << 10
        for r, ch in enumerate(s):
            seen[ch] += 1
            while l<=r and (seen[s[l]] > t[s[l]] or s[l] not in t):
                if s[l] not in t:
                    l += 1
                else:
                    seen[s[l]] -= 1
                    l += 1
            if len((t - seen).keys()) == 0:
                win_len = r - l + 1
                if win_len < ret:
                    ret = win_len
                    retl, retr = l, r

        if not bool(t - Counter(s[retl:retr+1])):
            return s[retl:retr+1]
        else:
            return ''
