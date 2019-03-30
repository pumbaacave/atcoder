from collections import Counter
from typing import *
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        p = paragraph.lower()
        cnt = Counter()
        l = 0
        for r in range(len(p)):
            if not p[r].isalpha():
                if not r:
                    continue
                if p[l].isalpha():
                    cnt[p[l:r]] += 1
                    l = r
            else:
                if not p[l].isalpha():
                    l = r
        if p[r].isalpha():
            if p[l].isalpha():
                cnt[p[l:r+1]] += 1


        for k in banned:
            if k in cnt:
                cnt.pop(k)

        print(cnt)
        return cnt.most_common()[0][0]
        

def test_check():
    s = Solution()
    p = "Bob hit a ball, the hit BALL flew far after it was hit."
    b = ["hit"]
    assert s.mostCommonWord(p, b) == "ball"
def test_check1():
    s = Solution()
    p = "a, a, a, a, b,b,b,c, c"
    b = ["a"]
    assert s.mostCommonWord(p, b) == "b"
def test_check2():
    s = Solution()
    p = "Bob"
    b = []
    assert s.mostCommonWord(p, b) == "bob"

