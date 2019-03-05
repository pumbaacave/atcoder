class Solution:
    def isValid(self, S: str) -> bool:
        if not S:
            return True
        idx = S.find("abc")
        if idx == -1:
            return False
        else:
            return self.isValid(S[:idx] + S[idx+3:])
