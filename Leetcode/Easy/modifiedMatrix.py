class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        M, N = len(matrix), len(matrix[0])
        col_max = [-1 for i in range(N)]
        for j in range(N):
            for i in range(M):
                col_max[j] = max(matrix[i][j], col_max[j])
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == -1:
                    matrix[i][j] = col_max[j]
        return matrix
