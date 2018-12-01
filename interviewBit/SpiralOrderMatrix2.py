"""
https://www.interviewbit.com/problems/spiral-order-matrix-ii/
hints: using Top, Bottom, Left, Right as border indicator
dir is a python built-in so 'dire' is  used here
"""
class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        # init
        ret =[[0] * A for i in range(A)]
        T = 0
        B = A - 1
        L = 0
        R = A - 1
        dire = 0
        gen = (i for i in range(1, A**2 +1))
        while (L<=R and T<=B):

            if dire == 0:
                for i in range(L,R+1):
                    ret[T][i] = next(gen)
                T+=1
                dire = 1
            elif dire == 1:
                for i in range(T,B+1):
                    ret[i][R] = next(gen)
                R-=1
                dire = 2
            elif dire ==2:
                for i in range(R, L-1, -1):
                    ret[B][i] = next(gen)
                B-=1
                dire =3
            elif dire == 3:
                for i in range(B, T-1, -1):
                    ret[i][L] = next(gen)
                L+=1
                dire = 0

        return ret
