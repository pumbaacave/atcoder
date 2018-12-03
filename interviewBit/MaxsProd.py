"""
https://www.interviewbit.com/problems/maxspprod/
"""
class Solution:
    # @param A : list of integers
    # @return an integer
    def maxSpecialProduct(self, A):
        L = 0
        R = 0
        M = 0
        Len = len(A)
        data = [[-1,-1,-1] for _ in range(Len)] # left, right, product
        for i in range(1, Len-1):
            M = A[i]

            if data[i][0] == -1:
                data[i][0] = 0
                for delta in range(1,i):
                    if A[i-delta] > M:
                        data[i][0] = i -delta
                        #data[i-delta][1] = i
                        break

            if data[i][1] == -1:
                data[i][1] = 0 # flag checked 
                for delta in range(1, Len-i):
                    if A[i+delta] > M:
                        data[i][1] = i + delta
                        #data[i+delta][0] = i
                        break
            data[i][2] = data[i][0] * data[i][1]

        data[0] = [0,0,0]
        data[Len-1] = [0,0,0]
        #print(data)
        s_data = sorted(data, key=lambda d:d[2])
        #print(s_data)
        return s_data[Len-1][2]
