class solution:
    def searchmatrix(self, matrix, target):
        """
        :type matrix: list[list[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]: return False
        a, b ,c ,d = 0, 0, len(matrix)-1, len(matrix[0])-1
        def search(a, b, c, d):
            if a > c or b > d: return False
            if a == c and b == d: return matrix[a][b] == target
            # cal middle
            e = (a + c) // 2
            f = (b + d) // 2
            if target == matrix[e][f]: return True
            elif target > matrix[e][f]:
                return search(a, f+1, e, d) or search(e+1, b, c, f) or search(e+1, f+1, c, d)
            elif target < matrix[e][f]:
                return search(a, b, e, f) or search(e+1, b, c, f) or search(a, f+1, e, d)
        return search(a, b, c, d)

class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]: return False
        # start from topright
        M, N = len(matrix), len(matrix[0])
        i, j = 0, N -1
        while i < M and 0 <= j:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
        return False
