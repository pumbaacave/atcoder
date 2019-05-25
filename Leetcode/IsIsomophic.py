class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        mapping = dict()
        for a, b in zip(s, t):
            if a not in mapping:
                if b in mapping.values():
                    return False
                mapping[a] = b
            elif mapping[a] != b:
                return False

        return True
