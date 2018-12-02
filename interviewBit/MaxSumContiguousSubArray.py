"""
https://www.interviewbit.com/problems/max-sum-contiguous-subarray/
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example:

Given the array [-2,1,-3,4,-1,2,1,-5,4],

the contiguous subarray [4,-1,2,1] has the largest sum = 6.

Solution:
    1. Parse array as Non-negative part, sum is M
    2. Parse contiguous array as negative part, sum is N
    3. 1. if M + N < 0: max(M, maxSubArray(laterPartOfArray))
       2. if M + N >= 0: max(M, maxSubArray([M+N, ...laterPartOfArray])) # recursion comes
    * optimization requires because python is slow here
"""
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        M = 0 # maximum
        N = 0
        i = 0
        L = len(A)


        # i refers to  first postive Num
        while i < L and A[i]  >= 0:
            M += A[i]
            i += 1
        if i >= L:
            return M
        # to Negative Slope
        while i < L and A[i] < 0:
            N += A[i]
            i += 1
        if i >= L:
            return M

        # later positive Sequense is waiting
        if M + N > 0:
            n_temp = [M + N]
            n_temp.extend(A[i:])
            temp = max(M, self.maxSubArray(n_temp))
            return temp
        else:
            temp = max(M, self.maxSubArray(A[i:]))
            return temp
