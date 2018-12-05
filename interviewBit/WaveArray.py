"""
https://www.interviewbit.com/problems/wave-array/
Given an array of integers, sort the array into a wave like array and return it, 
In other words, arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5.....
"""
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        i = 0
        A = sorted(A)
        #print(A)
        B = []
        while(i < len(A)):
            if(i < len(A) -1):
                B.append(A[i+1])
            B.append(A[i])
            i +=2

        return B
