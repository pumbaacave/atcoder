"""
Given a positive integer which fits in a 32 bit signed integer, find if it can be expressed as A^P where P > 1 and A > 0. A and P both should be integers.
"""
import math
class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, A):
        limit = math.sqrt(A)
        limit = int(limit)
        #print(limit)
        if A == 1:
            return 1

        for i in range(2, limit+1):
            base = i
            exp = 1
            target = float(A)
            while target > 1:
                target /= base
                # print(target)
                exp += 1

            # print(target)
            # print(base)
            # print(exp)
            if target == 1:
                return 1
        return 0

