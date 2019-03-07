from typing import *
from collections import Counter
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if not A:
            return []
        cnts = []
        for word in A:
            cnts.append( Counter(word) )
        tmp = cnts[0]
        for cnt in cnts[1:]:
            for k, v in tmp.items():
                if cnt[k] < tmp[k]:
                    tmp[k] = cnt[k]

        ans = []
        for ch, times in tmp.items():
            while times > 0:
                times -= 1
                ans.append(ch)

        return ans

def test_dup():
    A = ["bella", "label","roller"]
    s = Solution()
    assert s.commonChars(A) == ["l", "l", "e"]

