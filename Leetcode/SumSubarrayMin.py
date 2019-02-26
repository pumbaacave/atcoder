class Solution:
    def sumSubarrayMins(self, A: 'List[int]') -> 'int':
        length = len(A)
        # validation
        if length < 2:
            return sum(A)

        stack = []
        former_less_num_idx = [-1] * len(A)
        dp = [0] * len(A)
        total = 0
        for i, a in enumerate(A):
            while stack and stack[-1][1] > a:
                stack.pop()
            if stack:
                former_less_num_idx[i] =stack[-1][1]
            stack.append([i, a])
        for i, a in enumerate(A):
            if former_less_num_idx[i] < 0:
                dp[i] = (i+1) * A[i]
                total += dp[i]
            else:
                dp[i] = (i - former_less_num_idx[i])*A[i] + dp[former_less_num_idx[i]]
                total += dp[i]


        return total

def test_sum_subarrays_mins():
    s = Solution()
    A = [3, 1, 2, 4]
    assert s.sumSubarrayMins(A) == 17

def test_sum_subarrays_mins_desc():
    s = Solution()
    A = [3, 2, 2, 2, 1]
    assert s.sumSubarrayMins(A) == 10

def test_sum_subarrays_empty():
    s = Solution()
    A = []
    assert s.sumSubarrayMins(A) == 0
