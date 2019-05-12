class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c = sorted((a, b, c))
        if b - a == 1 and  c - b == 1:
            return [0, 0]

        max_move = c - a - 2
        min_move = 1 if c - b <= 2 or b - a <= 2 else 2
        return [min_move, max_move]
