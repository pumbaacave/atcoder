class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        # people are labeled from 1 to N
        believe = [ [] for _ in range(N + 1)]

        for t in trust:
            believe[ t[0] ].append( t[1] )

        possible_judges = set(range(1, N+1))
        num_believer = 0
        judge_idx = 0
        for i, b in enumerate(believe):
            if not b:
                # initial i = 0 will be update
                judge_idx = i
                continue
            else:
                num_believer += 1
                possible_judges = possible_judges.intersection(b)

        if num_believer != N-1:
            return -1

        if bool(believe[judge_idx]) or len(possible_judges) != 1:
            return -1

        return possible_judges.pop()

import pytest

@pytest.mark.parametrize("n, trust, expected",[
    (2, [[1,2]], 2),
    (3,[[1,3],[2,3]], 3),
    (3,[[1,3],[2,3],[3,1]], -1),
    (3,[[1,2],[2,3]], -1),
    (4,[[1,3],[1,4],[2,3],[2,4],[4,3]], 3)
    ])
def test_findjudge(n, trust,  expected):
    s = Solution()
    ans = s.findJudge(n, trust)
    assert ans == expected

