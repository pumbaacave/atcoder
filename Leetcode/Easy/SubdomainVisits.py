from collections import Counter
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        if not cpdomains: return []
        cnt = Counter()
        for cd in cpdomains:
            c, d = cd.split(" ")
            c = int(c)
            idx = 0
            while idx >= 0:
                if idx != 0:
                    idx += 1
                cnt[d[idx:]] += c
                idx = d.find(".", idx)
        return [' '.join([str(v), k]) for k, v in cnt.items() ]



