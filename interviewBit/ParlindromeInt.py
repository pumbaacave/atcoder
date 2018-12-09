"""
Determine whether an integer is a palindrome. Do this without extra space.

A palindrome integer is an integer x for which reverse(x) = x where reverse(x) is x with its digit reversed.
Negative numbers are not palindromic.
# actually, string is banned but int var is ok

"""
class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        if A < 0:
            return 0
        exp = 0
        temp = A
        while temp >= 10:
            temp /= 10
            exp += 1
        #print(exp)
        for i in range(1, (exp +1)/2+1):
            #print(A)
            a = A % 10
            b = A / 10 ** ( exp-2*(i-1) )
            #print(a)
            #print(b)
            if a != b:
                return 0
            A -= b * 10 ** (exp-2*(i-1))
            A /= 10
        return 1

