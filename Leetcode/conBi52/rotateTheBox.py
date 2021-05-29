class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for row in box:
            # in place mutation
            self.right_shake_one_row(row)
        return self.transpose(box)

    def transpose(self, box: List[List[str]]) -> List[List[str]]:
        # input with at least 1 row
        num_row = len(box[0])
        # transposed box
        t = [[]for _ in range(num_row)]
        for row in reversed(box):
            for idx, col in enumerate(row):
                t[idx].append(col)
        return t

    def right_shake_one_row(self, row: List[str]):
        """
        Similar to 2 pointer window method.
        """
        cursor = hole = len(row)
        while cursor > 0:
            cursor -= 1
            if row[cursor] == '.':
                pass
            elif row[cursor] == '#':
                # till hole == cursor where no swap possible
                while hole > cursor:
                    hole -= 1
                    if row[hole] == '.':
                        row[cursor], row[hole] = row[hole], row[cursor]
                        break
            elif row[cursor] == '*':
                hole = cursor
