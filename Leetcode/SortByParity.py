class Solution:
    def sortArrayByParity(self, A: 'List[int]') -> 'List[int]':
        if len(A) < 2:
            return A

        l, r = 0, len(A) - 1
        while l < r:
            while l < len(A) and A[l] % 2 == 0:
                l += 1
            while r >= 0 and A[r] % 2 == 1:
                r -= 1
            if l < r:
                A[l], A[r] = A[r], A[l]

        return A

def test_sort():
    A = [0, 0]
    s = Solution()
    ans = s.sortArrayByParity(A)
    print(ans)
