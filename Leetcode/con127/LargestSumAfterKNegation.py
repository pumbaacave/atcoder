import heapq
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        heapq.heapify(A)
        def helper(A, K):
            if K <= 0:
                return A
            least = heapq.heappop(A)
            heapq.heappush(A, -least)
            return helper(A, K - 1)

        A = helper(A, K)
        return sum(A)
        
