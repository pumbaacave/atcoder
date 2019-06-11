from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s: return -1
        cnt = Counter(s)
        for i, c in enumerate(s):
            if cnt[c] == 1:
                return i
        return -1