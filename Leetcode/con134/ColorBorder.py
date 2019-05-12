class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:

        # target conponet: color in (ori_c or target_c)
        if not grid or not grid[0]:
            return grid
        M, N = len(grid), len(grid[0])
        # DFS
        ori_c = grid[r0][c0]

        def helper(r, c):
            # if is target color return 1
            if r < 0 or r >= M or c < 0 or c >= N:
                return 0
            # visited
            if grid[r][c] in (-1, color): return 1
            elif grid[r][c] == ori_c:

                grid[r][c] = -1
                num_n = sum(helper(r + i, c + j) for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)])

                if num_n < 4:
                    grid[r][c] = color
                else:
                    grid[r][c] = ori_c
                return 1
            else: return 0

        for i in range(M):
            for j in range(N):
                if grid[i][j] == color:
                    grid[i][j] = -2
        print(grid)
        helper(r0, c0)
        for i in range(M):
            for j in range(N):
                if grid[i][j] == -2:
                    grid[i][j] = color

        return grid
