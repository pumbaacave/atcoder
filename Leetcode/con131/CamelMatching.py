from typing import *
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def match(q):
            nonlocal pattern
            i, j = 0, 0
            while i < len(q) and j < len(pattern):
                if pattern[j].isupper():
                    if pattern[j] == q[i]:
                        j += 1
                        i += 1
                    else:
                        if q[i].isupper():
                            return False
                        i += 1
                else:
                    # lower pattern never match
                    if q[i].isupper():
                        return False
                    elif q[i] == pattern[j]:
                        i += 1
                        j += 1
                    else:
                        i += 1
            # pattern remains
            if j < len(pattern):
                return False
            while i < len(q):
                if q[i].isupper():
                    return False
                i += 1

            return True
        return list(map(match, queries))
def test_match():
    s = Solution()
    qs = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
    p = "FB"
    assert s.camelMatch(qs, p) == [True, False, True, True, False]
