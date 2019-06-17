from collections import numadtuple
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        Point = numadtuple("Point", "row col")
        start = Point(0, 0)
        end = Point(0, 0)
        empty_cnt = 0
        # grid ++ search coordinate
        memo = {}
        M, N = len(grid), len(grid[0])
        for r, row in enumerate(grid):
            for c, elem in enumerate(row):
                if elem == 1:
                    start.row, start.col = r, c
                elif elem == 2:
                    end.row, end.col = r, c
                elif elem == 0:
                    empty_cnt += 1
        # hash func of the state
        def hash_grid_poind(grid, point):
            h = 0
            for row in grid:
                for c in row:
                    h *= 2
                    h += c
            return (h, point)
        def search(grid, point):
            cur = grid[point.row][point.col]
            # bound check
            if point.row < 0 or point.row >= M:
                return 0
            if point.col < 0 or point.col >= N:
                return 0

            if cur == -1:
                return 0
            h = hash_grid_poind(grid, point)
            if h in memo: return memo[h]

            # no cache
            if point == end:
                if empty_cnt == 0:
                    memo[h] = 1
                    return 1
                else:
                    memo[h] = 0
                    return 0
            else:
                # impl of backtrack
                grid[point.row][point.col] = -1
            
