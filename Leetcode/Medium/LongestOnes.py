class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        """
        use Window
        """
        if not A:
            return 0
        num_zero = 0
        l, r = 0, 0
        L = len(A)
        longest = 0
        while r < L:
            if A[r] == 1:
                longest = max(longest, r - l + 1)
            else:
                num_zero += 1
                while num_zero > K:
                    # start droping left side
                    if A[l] == 0:
                        num_zero -= 1
                    l += 1
            r += 1
        return longest
    def longestOnes(self, A, K):
        res = i = 0
        for j in xrange(len(A)):
            K -= A[j] == 0
            if K < 0:
                K += A[i] == 0
                i += 1
            res = j - i + 1
        return res
