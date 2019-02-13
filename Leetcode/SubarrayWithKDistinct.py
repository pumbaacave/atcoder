class Solution:
    def subarraysWithKDistinct(self, A: 'List[int]', K: 'int') -> 'int':
        length = len(A)
        total = 0
        for l in range(length):
            # init
            num_distinct = 0
            seen = set()
            for r in range(l, length):
                if A[r] not in seen:
                    seen.add(A[r])
                    num_distinct += 1

                if num_distinct > K:
                    # num over and will decrease
                    break
                elif num_distinct == K:
                    print(A[l:r+1])
                    total += 1
        return total


s = Solution()
A = [1,2,1,2,3]
K = 2
ans = s.subarraysWithKDistinct(A, K)
assert ans == 7
