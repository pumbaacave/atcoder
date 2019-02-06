# recursive
class Solution:
    def isSubsequence(self, s: 'str', t: 'str') -> 'bool':
        if not s:
            return True
        elif not t:
            return False

        is_sub_1 = self.isSubsequence(s[:-1], t[:-1])
        # is_sub_2 = self.isSubsequence(s[:-1], t)
        is_sub_3 = self.isSubsequence(s, t[:-1])
        if s[-1] == t[-1]:
            return is_sub_1
        else:
            return is_sub_3

# iteration
class Solution:
    def isSubsequence(self, s: 'str', t: 'str') -> 'bool':
        if not s:
            return True
        elif not t:
            return False

        len_s = len(s)
        len_t = len(t)
        dp = [[False] * (len_t+1) for _ in range(len_s+1)]
        dp[0] = [True] * (len_t+1)
        for i in range(len_s):
            for j in range(len_t):
                if s[i] == t[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = dp[i+1][j]
        return dp[-1][-1]
