class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not len(grid) or not len(grid[0]): return 0
        M, N = len(grid), len(grid[0])

        # state: 1 land, 0 water, -1 visited land
        num_islands = 0

        def traverse(r, c):
            if r < 0 or M <= r: return
            if c < 0 or N <= c: return
            if grid[r][c] in ("0", "-1"): return
            elif grid[r][c] == "1":
                grid[r][c] = "-1"
                traverse(r - 1, c)
                traverse(r + 1, c)
                traverse(r, c - 1)
                traverse(r, c + 1)
        for r in range(M):
            for c in range(N):
                if grid[r][c] in ("0", "-1"):
                    continue
                else:
                    num_islands += 1
                    traverse(r, c)

        # return
        return num_islands
