"""
https://www.interviewbit.com/problems/repeat-and-missing-number-array/
linear time order, constant memory requirement
"""
class Solution:
	# @param A : tuple of integers
	# @return a list of integers
	def repeatedNumber(self, A):
	    L = len(A)

	    S = (1+L)*L/2
	    newS = sum(A)
	    delta = S - newS # A - B
	    delta = int(delta)
	    sq_dif = 0

	    for i in range(1,L+1):
	        sq_dif += i ** 2
	        sq_dif -= A[i-1] ** 2

	    Sum = sq_dif / delta
	    a = (Sum +delta)/2
	    b = a - delta
            return [int(b), int(a)]
