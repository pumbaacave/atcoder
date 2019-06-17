from collections import deque
class Solution:
  ### need propocess pattern first
  def isMatch(self, s: str, p: str) -> bool:
    # input check
    if not s and p: return False
    #  add dummy start character
    s = s + '#'
    p = p + '#'
    ls, lp = len(s), len(p)
    def match(ch, p):
        return ch == p or p == "."

    dp = [[False] * lp for _ in range(ls)]
    dp[-1][-1] = True
    # for matching by p[-1] when p[-1] == "*"
    #for i in range(ls):
    #    dp[i][lp-1] = True

    for i in reversed(range(ls-1)):
        for j in reversed(range(lp-1)):
            is_match = False
            first = p[j] in (s[i], '.')
            if j + 2 < lp and p[j+1] == "*":
                is_match = first and (dp[i+1][j] or i + 2 == ls) or dp[i][j+2]
            else:
                is_match = first and dp[i+1][j+1]
            dp[i][j] = is_match
    print(dp)
    return dp[0][0]


class Solution1:
  # start from head
  def isMatch(self, s: str, p: str) -> bool:
    # input check
    if not s and p: return False
    #  add dummy start character
    s = s
    p = p
    ls, lp = len(s) + 1, len(p) + 1

    dp = [[False] * lp for _ in range(ls)]
    dp[0][0] = True

    for i in range(1, ls):
        for j in range(1, lp):
            is_match = False
            first = p[j] in (s[i], '.')
            if j + 2 < lp and p[j+1] == "*":
                is_match = first and (dp[i+1][j] or i + 2 == ls) or dp[i][j+2]
            else:
                is_match = first and dp[i+1][j+1]
            dp[i][j] = is_match
    print(dp)
    return dp[0][0]

import pytest
@pytest.mark.parametrize("s, p, expected",[
  # ('aa', 'a', False),
  ('aa', 'a*', True),
  ('aaa', 'ab*a*c*a', True),
  ('aab', 'a*b', True),
  ('aaa', 'a*a', True),
  ('aab', 'a*b*c', False),
  ('abc', '.*', True),
  ])
def test_rg(s, p, expected):
  so = Solution()
  assert so.isMatch(s, p) == expected
