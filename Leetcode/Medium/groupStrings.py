from collections import defaultdict
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def build_key(word):
            if len(word) == 1:
                return 0
            stack = []
            cur = None
            for ch in word:
                if cur is None:
                    cur = ch
                else:
                    stack.append( (ord(ch) - ord(cur)) % 26)
                    cur = ch
            return tuple(stack)

        if not strings: return []
        groups = defaultdict(list)
        for s in strings:
            key = build_key(s)
            groups[key].append(s)

        ret = []
        for k, v in groups.items():
            ret.append(v)
        return ret
