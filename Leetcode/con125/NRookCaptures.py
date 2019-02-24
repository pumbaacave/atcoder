class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """

        def find_pawn(r, c, d):
            while 0 <= r <= 7 and 0 <= c <= 7 and board[r][c] != 'B':
                if board[r][c] == 'p':
                    return 1

                # move
                r += d[0]
                c += d[1]
            return 0

        DIRECTIONS = [
                (-1, 0),
                (1, 0),
                (0, 1),
                (0, -1),
                ]

        rook_r, rook_c = 0, 0
        # find position of Rook
        for idx in range(64):
            r, c = divmod(idx, 8)
            if board[r][c] == 'R':
                rook_r, rook_c = r, c
                break

        total = sum( [find_pawn(rook_r, rook_c, d) for d in DIRECTIONS] )
        return total

import pytest
@pytest.mark.parametrize("board, expected",[
    ([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]], 3),
    ([[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]], 0),
    ([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]], 3),
    ])
def test_numRookCaptures(board, expected):
    s = Solution()
    ans = s.numRookCaptures(board)
    assert ans == expected

