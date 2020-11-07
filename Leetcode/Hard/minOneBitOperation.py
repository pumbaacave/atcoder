class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        n_str = reversed(format(n, 'b'))
        cost = 0
        """
        To erase the leftmost bit must turn to the form 1000000...00,
        it will defenitely require 2 ** n + 1 streps, n = num.bit_length()
        from LSB to MSB, lower bit's cost to reset can counter higher bits' cost
        """
        for i, c in enumerate(n_str):
            if c == '0':
                continue
            cost = (1 << (i + 1)) - 1 - cost
        return cost


if __name__ == "__main__":
    s = Solution()
    s.minimumOneBitOperations(9)
