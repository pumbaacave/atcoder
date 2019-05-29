from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if not s: return s
        # dp
        cnt = Counter(s)
        seen = set()
        stack = []
        for ch in s:
            # already pushed sequence is locally optimised
            # so duplicate character will be ignored
            if ch in seen:
                cnt[ch] -= 1
                continue
            # all popable char in the stack has remaining counterpart appear later
            # which ensured by cnt
            while stack and stack[-1] > ch and cnt[stack[-1]] > 0:
                last = stack.pop()
                seen.discard(last)

            stack.append(ch)
            cnt[ch] -= 1
            seen.add(ch)

        return ''.join(stack)
