from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def valid_group(nums):
            c = Counter(nums)
            c.pop('.')
            if not c:
                return True
            if c.most_common()[0][1] > 1:
                return False
            return True

        # rows
        v_rows = all([valid_group(nums) for nums in board])
        if not v_rows: return False

        # cols
        v_cols = all([valid_group(nums) for nums in zip(*board)])
        if not v_cols: return False

        # sub_boards
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                s = []
                s.extend(board[i][j:j + 3])
                s.extend(board[i + 1][j:j + 3])
                s.extend(board[i + 2][j:j + 3])
                if not valid_group(s):
                    return False

        return True
