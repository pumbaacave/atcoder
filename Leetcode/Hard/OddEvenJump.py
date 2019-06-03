class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        if not A:
            return 0
        len_A = len(A)
        up = [None] * len_A
        down = [None] * len_A
        stack = []

        # build monotonic stack
        idxs = sorted(range(len_A), key=lambda i:A[i])

        # populate up
        for idx in idxs:
            if not stack:
                stack.append( idx )
            # val monotonic AND can accept succeding index only
            while stack and idx > stack[-1]:
                last = stack.pop()
                up[last] = idx
            stack.append( idx )
        stack.clear()

        idxs.sort(key=lambda i:-A[i])
        # populate down
        for idx in idxs:
            if not stack:
                stack.append( idx )
            while stack and idx > stack[-1]:
                last = stack.pop()
                down[last] = idx
            stack.append( idx )

        up[-1] = down[-1] = True
        for i in reversed(range(len_A - 1)):
            # some idx has no next up or down idx
            if up[i]:
                up[i] = down[up[i]]
            if down[i]:
                down[i] = up[down[i]]
        return sum([bool(v) for v in up if v])


