class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        def value(a, b, c):
            return a * b * c
        len_a = len(A)
        large = float('inf')
        memo = [[0] * len_a for _ in range(len_a)]
        A = A * 2
        for i in range(len_a):
            memo[i][(i+2)%len_a] = value(*A[i:i+3])
        for w in range(4, len_a + 1):
            for i in range(len_a):
                start, end = i, i + w - 1
                ide = (i + w - 1) % len_a
                least = large
                for mid in range(start + 1, end):
                    idm = mid % len_a
                    cur = value(A[start], A[end], A[mid]) + memo[idm][ide] + memo[start][idm]
                    if cur < least:
                        least = cur
                memo[i][ide] = least
        print(memo)
        return memo[0][len_a - 1]
