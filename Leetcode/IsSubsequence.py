# recursive
class Solution:
    def isSubsequence(self, s: 'str', t: 'str') -> 'bool':
        if not s:
            return True
        elif not t:
            return False

        is_sub_1 = self.isSubsequence(s[:-1], t[:-1])
        # is_sub_2 = self.isSubsequence(s[:-1], t)
        is_sub_3 = self.isSubsequence(s, t[:-1])
        if s[-1] == t[-1]:
            return is_sub_1
        else:
            return is_sub_3

# iteration
from collections import deque
from itertools import chain
class Solution:
    def isSubsequence(self, s: 'str', t: 'str') -> 'bool':
        if not s:
            return True
        elif not t:
            return False

        itr_s = chain(s, [None])
        itr_t = chain(t, [None])
        nxt_s = next(itr_s)
        nxt_t = next(itr_t)
        while nxt_t is not None:
            if nxt_s is None:
                return True
            else:
                if nxt_t == nxt_s:
                    nxt_t = next(itr_t)
                    nxt_s = next(itr_s)
                else:
                    nxt_t = next(itr_t)
        if nxt_s is None:
            return True
        else:
            return False
