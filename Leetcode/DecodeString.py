class Solution:
    def decodeString(self, s: str) -> str:
        if not s: return s
        s = "".join(["[",s,"]"])
        ls = len(s)
        stack = []
        def process():
            num = 0
            temp = []
            while stack and stack[-1] != '[':
                cur = stack.pop()
                if isinstance(cur, int):
                    temp[-1] = cur * temp[-1]
                else:
                    temp.append(cur)
            if not stack:
                stack.pop()
            stack.append(''.join(reversed(temp)))


        new_s = []
        i = 0
        while i < ls:
            if not s[i].isdigit():
                new_s.append(s[i])
                i += 1
            else:
                l = i
                while s[i].isdigit():
                    i += 1
                new_s.append(int(s[l:i]))

        for c in new_s:
            if c == "]":
                process()
            else:
                stack.append(c)

        process()
        return ''.join(stack)

