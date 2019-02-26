from collections import defaultdict
class Solution(object):
    def gridIllumination(self, N, lamps, queries):
        """
        :type N: int
        :type lamps: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        row_dict = defaultdict(int)
        column_dict = defaultdict(int)
        ascending_diagonal_dict = defaultdict(int)
        desending_diagonal_dict = defaultdict(int)
        lamp_set = set()
        def inc_dicts(lamp, incr):
            row_dict[lamp[0]] += incr
            column_dict[lamp[1]] += incr
            ascending_diagonal_dict[sum(lamp)] += incr
            desending_diagonal_dict[lamp[0] - lamp[1]] += incr

        def check(q):
            if row_dict[ q[0] ]:
                return True
            if column_dict[ q[1] ]:
                return True
            if ascending_diagonal_dict[ sum(q) ]:
                return True
            if desending_diagonal_dict[ q[0] - q[1] ]:
                return True
            return False

        def turn_off_lamps(q):
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    c, r = q[0] + i, q[1] + j
                    if (c, r) in lamp_set:
                        lamp_set.discard( (c, r) )
                        inc_dicts([c, r], -1)
        for l in lamps:
            inc_dicts(l, 1)
            lamp_set.add(tuple(l))
        answers = []
        for q in queries:
            if check(q):
                answers.append(1)
            else:
                answers.append(0)
            turn_off_lamps(q)


        return answers
