#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # is Bitmap good enough?
        M, N = len(matrix), len(matrix[0])
        # bitmap for Row and Column
        R = C = 0
        for i, row in enumerate(matrix):
            for j, num in enumerate(row):
                if num == 0:
                    R |= (1 << i)
                    C |= (1 << j)
        # print(R, C)
        for i in range(M):
            for j in range(N):
                if (R & (1 << i) != 0) or (C & (1 << j) != 0):
                    matrix[i][j] = 0


# @lc code=end
