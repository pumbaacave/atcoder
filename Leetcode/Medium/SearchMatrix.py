from typing import *
import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        cols = iter(zip(*matrix))
        first_col = list(next(cols))
        row_idx = bisect.bisect_left(first_col, target) - 1
        return row_idx >= 0 and target in matrix[row_idx] or target in first_col

def test_search():
    s = Solution()
    m = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    target = 13
    assert s.searchMatrix(m, target) == True
