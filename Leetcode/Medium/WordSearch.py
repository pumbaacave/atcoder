class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def search(start, idx):
            # all chr consumed
            if idx == len(word):
                return True

            x, y = start
            if not check(x, y):
                return False
            if board[x][y] != word[idx]:
                return False
            else:
                # recorde match path only
                prev = board[x][y]
                board[x][y] = '.'
            if any(search(p, idx + 1) for p in [[x+1, y], [x-1,y], [x,y+1], [x,y-1]]):
                return True
            else:
                # remove record
                board[x][y] = prev
                return False

        if not board or not board[0]:
            return False
        M, N = len(board), len(board[0])

        def check(x, y):
            return 0<=x<M and 0<=y<N

        for i, r in enumerate(board):
            for j, c in enumerate(r):
                if search((i, j), 0):
                    return True
        return False
