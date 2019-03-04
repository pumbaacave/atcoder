class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        queue = []
        num_row = len(board)
        num_col = len(board[0])

        neighbours = [
                (-1, -1),
                (-1, 0),
                (-1, 1),
                (0, -1),
                (0, 1),
                (1, -1),
                (1, 0),
                (1, 1),
                ]

        def valid_neighbour(r, c):
            return 0 <= r < num_row and 0 <= c < num_col

        def cal_next(r, c):
            num_live = 0
            for n in neighbours:
                n_r = r + n[0]
                n_c = c + n[1]
                if valid_neighbour(n_r, n_c):
                    num_live += board[n_r][n_c]

            # live 2 dead
            if board[r][c] and num_live not in (2, 3):
                queue.append((r, c))

            # dead 2 live
            if not board[r][c] and num_live == 3:
                queue.append((r, c))

        for i in range(num_row):
            for j in range(num_col):
                cal_next(i, j)

        for r, c in queue:
            board[r][c] ^= 1
