class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        if not S:
            return S
        l, r  = 0, 0
        ret = []
        last = 0
        for i, s in enumerate(S):
            if s == "(":
                l += 1
            elif s == ")":
                r += 1
            if l == r:
                ret.append(S[last+1:i])
                last = i + 1
        return "".join(ret)

