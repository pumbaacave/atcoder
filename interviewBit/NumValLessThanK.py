"""
Given a set of digits (A) in sorted order, find how many numbers of length B are possible whose value is less than number C.

this implementation not efficient
needs len(A)**B space
"""
import copy
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def check(self, testers, thrs):
        #print(testers)
        #print(thrs)
        counter = 0
        for t in testers:
            if t >= thrs:
                counter += 1
        return counter


    def solve(self, A, B, C):
        if len(A) == 0:
            return 0
        thrs = 10 ** (B-1) if B > 1 else 0
        testers = [0]
        # build integers for trial
        for i in range(B):
            #print("now is {} round".format(i))
            op = copy.copy(testers)
            testers = []
            for b in op:
                for a in A:
                    to_be_append = b*10 + a
                    #print(to_be_append)
                    if to_be_append >= C:
                        return self.check(testers, thrs)
                    testers.append(to_be_append)
        return self.check(testers, thrs)
