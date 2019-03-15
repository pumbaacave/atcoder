class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n <= 0:
            return []
        board = [ [0] * n for i in range(n) ]
        # Bound
        L, R = 0, n - 1
        T, B = 0, n - 1

        next_num = iter(range(1, n * n + 1))

        # end at -1 in order to take 0
        for i in range(n-1, -1, -2):
            if L == R:
                # put last one in middle
                board[L][B] = next(next_num)
            else:
                # top row
                for j in range(i):
                    board[T][L + j] = next(next_num)
                # right col
                for j in range(i):
                    board[T + j][R] = next(next_num)
                # bottom row
                for j in range(i):
                    board[B][R - j] = next(next_num)
                # left col
                for j in range(i):
                    board[B - j][L] = next(next_num)
                L += 1
                R -= 1
                T += 1
                B -= 1

        return board

def test_gen():
    n = 3
    s = Solution()
    assert s.generateMatrix(n) == [
            [1,2,3],
            [8,9,4],
            [7,6,5]
            ]
