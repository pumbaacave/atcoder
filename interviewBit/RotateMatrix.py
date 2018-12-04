"""
https://www.interviewbit.com/problems/rotate-matrix/
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

You need to do this in place.

Note that if you end up using an additional array, you will only receive partial score.

solution:
    swap two variable inplace
    1. b = a + b
    2. a = b - a
    3. b = b - a

    this question, four element swap is needed(seemingly)
    0degree to 90, 90 to 180, 180 to 270, 270 to 360(0)
    but found out all are interchangeable
    so:
    0 to 90, 0(now 90) to 180, 0(now 180) to 270,
    Finally rotate clockwise 90 degree in place mission is done
"""
class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def swap(self, a,b,c,d,A):
        A[c][d] = A[c][d] + A[a][b]

        A[a][b] = A[c][d] - A[a][b]

        A[c][d] = A[c][d] - A[a][b]

    def rotate(self, A):
        #print(A)
        #self.swap(0,0,1,1,A)
        #print(A)
        import math
        L = len(A)
        N = math.ceil(L/2)
        N = int(N)
        #print(N)
        for i in range(N):
            for j in range(i, L-1-i):
                self.swap(i, j, j, L-1-i, A)
                self.swap(i, j, L-1-i, L-1-j, A)
                self.swap(i, j, L-1-j, i, A)
            #print(A)
        return A
