from collections import defaultdict
class Solution:
    def longestDupSubstring(self, S: str) -> str:
        # actually suffix array is more fit
        # suffix needs guard to filter out prefix == suffix
        # suffix trie
        ls = len(S)
        T = defaultdict(lambda:T)
        root = T
        # "#" end of suffix, value: start index
        for i in reversed(range(ls)):
            suf = S[i:]
            cur = root
            for s in suf:
                cur = cur[s]
            cur["#"] = i
        thr = 0
        left, r = 0, 0
        for i in range(ls):
            cur = root
            for l, s in enumerate(S[i:]):
                lc, rc = 0, 0 # candidats
                if s in cur:
                    cur = cur[s]
                    if l > thr:
                        lc, rc =i, i + l
                elif "#" in cur and cur["#"] != i:
                    if l > thr:
                        left, r = i, i + l
                        thr = l
                else:
                    break
            # after break or sample ends

            if l - 1 > thr:
                left, r = i, i + l - 1
                thr = l - 1
            # end loop ops
        return S[left:r]
