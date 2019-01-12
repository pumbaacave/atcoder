"""
Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number.

NOTE A solution will always exist. read Goldbach’s conjecture
"""
import math
class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        end = int(math.floor(A/2) + 1)
        #print(end)
        can_list = []
        for i in range(2, end+1,1):
            if self.is_prime(i) and self.is_prime(A-i):
                return [i, A-i]


    def is_prime(self, num):
        #print(num)
        for i in range(2, int(math.sqrt(num)+1)):
            if num % i == 0:
                return False
        return True
