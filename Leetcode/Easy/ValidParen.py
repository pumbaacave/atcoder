class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return True
        stack = []
        mapping = {
                ")":"(",
                "]":"[",
                "}":"{"
                }
        for c in s:
            if c in ("(", "[", "{"):
                stack.append(c)
            else:
                if not stack or stack[-1] != mapping[c]:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0
