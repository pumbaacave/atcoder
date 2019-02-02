from itertools import cycle
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        rows = []
        [rows.append([]) for _ in range(numRows)]
        row_id_gen = self.gen_seq(numRows)
        for letter in s:
            row_id = next(row_id_gen)
            rows[row_id].append(letter)
        res = "".join(["".join(row) for row in rows])
        return res


    def gen_seq(self, num):
        # case num >= 3
        # [0, n-1]
        asc = list(range(num))
        # [n-2, 0)
        dsc = list(range(num-2, 0, -1))
        asc.extend(dsc)
        return cycle(asc)

def test_sample1():
    In = "PAYPALISHIRING"
    numRows = 3
    s = Solution()
    print(s.convert(In, numRows))

test_sample1()

def test_seq1():
    s = Solution()
    seq = s.gen_seq(1)
    for _ in range(10):
        print(next(seq))
