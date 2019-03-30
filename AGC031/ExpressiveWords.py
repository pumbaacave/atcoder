from typing import *
from collections import deque
class Solution:
    def build(self, S):
        queue = deque()
        for s in S:
            if not queue or s != queue[-1][0]:
                queue.append([s])
            else:
                queue[-1].append(s)
        return queue

    def expressiveWords(self, S: str, words: List[str]) -> int:
        # build tokens
        # num_occur <= 2 ver batim, else strechy
        queue = self.build(S)
        print(queue)

        def is_stretchy(word):
            ref = queue.copy()
            w_q = self.build(word)
            if len(ref) != len(w_q): return False
            def ok(r, w):
                if r[0] != w[0]:
                    return False
                if len(r) < 3:
                    return len(r) == len(w)
                else:
                    # w string can not srink
                    return len(r) >= len(w)
            if all([ok(r, w) for r, w in(zip(ref, w_q))]):
                return 1
            return 0
        return sum(map(is_stretchy, words))

def test_build():
    s = Solution()
    text = "hello"
    print(s.build(text))
