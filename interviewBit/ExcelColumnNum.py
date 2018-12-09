"""
Given a column title as appears in an Excel sheet, return its corresponding column number.
"""
class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        count = 0
        for a in A:
            if a == None:
                break
            else:
                count *= 26
                count += ord(a) - ord('A') + 1

        return count

