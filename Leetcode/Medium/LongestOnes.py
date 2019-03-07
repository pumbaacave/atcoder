class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        """
        use Window
        """
        if not A:
            return 0
        num_zero = 0
        l = 0
        L = len(A)
        longest = 0
        for r in range(L):
            if A[r] == 0:
                num_zero += 1
                while num_zero > K and l < r:
                    # start droping left side
                    num_zero -= (1 - A[l])
                    l += 1
            longest = max(longest, r - l + 1)
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
