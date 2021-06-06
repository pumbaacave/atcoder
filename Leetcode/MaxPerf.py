from typing import Tuple, List
from pprint import PrettyPrinter


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        # choss
        # Performance = sumTotalSpeed * minEfficiencyAmongTheGroup
        # dp [k][n][(total_sp, eff)]
        # dp[k][n] = max (dp[k][n - 1], cal(dp[k-1][n-1] dp[1][n])

        dp = [[(0, 0) for _ in range(n)] for _ in range(k)]
        # first row: k = 1
        for i in range(n):
            dp[0][i] = (speed[i], efficiency[i])
        for row in range(1, k):
            # choose `row` + 1(0-indexed) number from 0~i number group
            for i in range(row, n):
                sp_ef_without_i = dp[row][i-1]
                sp_ef_i = dp[0][i]
                sp_ef_with_i = (0, 0)
                for s in range(i):
                    total_sp = dp[row - 1][s][0] + sp_ef_i[0]
                    min_ef = min(dp[row - 1][s][1], sp_ef_i[1])
                    perf = total_sp * min_ef
                    last_perf = self.get_perf(sp_ef_with_i)
                    # TODO deal with == case, preserve max ef pair
                    if perf > last_perf:
                        sp_ef_with_i = (total_sp, min_ef)
                    if perf == last_perf and min_ef > sp_ef_with_i[1]:
                        # preserve higher ef
                        sp_ef_with_i = (total_sp, min_ef)
                dp[row][i] = sp_ef_without_i if self.get_perf(
                    sp_ef_without_i) > self.get_perf(sp_ef_with_i) else sp_ef_with_i
        # choose at most k
        ans = max(s*e for row in range(k) for s, e in dp[row])

        #pp = PrettyPrinter()
        # print(ans)
        # pp.pprint(dp)
        return ans

    def get_perf(self, sp_ef: Tuple[int, int]) -> int:
        return sp_ef[0] * sp_ef[1]


if __name__ == '__main__':
    s = Solution()
    #s.maxPerformance(6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 4)
    s.maxPerformance(3, [2, 8, 2], [2, 7, 1], 2)
