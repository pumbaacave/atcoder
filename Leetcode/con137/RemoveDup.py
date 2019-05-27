class Solution:
    def removeDuplicates(self, S: str) -> str:
        if not S:
            return S
        stack = []
        for c in S:
            if not stack:
                stack.append(c)
            elif c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)
