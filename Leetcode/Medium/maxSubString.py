from collections import defaultdict


class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        bound_l, bound_r = -1, 100001
        # leftmost idx of letters
        left = defaultdict(lambda: bound_r)
        # rightmost idx of letters
        right = defaultdict(lambda: bound_l)
        for i, ch in enumerate(s):
            left[ch] = min(i, left[ch])
            right[ch] = max(i, right[ch])

        # we should extend right bound since valid sub should contain all occurrance of the letter
        def check(i):
            l = i
            new_r = right[s[i]]
            while i <= new_r:
                if left[s[i]] < l:
                    # no valid sub
                    return -1
                new_r = max(new_r, right[s[i]])
                i += 1
            return new_r

        subs = []
        r = -1
        for i, ch in enumerate(s):
            if i == left[ch]:
                new_r= check(i)
                if new_r== -1:
                    continue
                else:
                    # new sub is shorter
                    if i < r:
                        subs[-1] = s[i:new_r+1]
                    else:
                        subs.append(s[i:new_r+1])
                r = new_r

        return subs
