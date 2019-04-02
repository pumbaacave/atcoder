class Solution:
    def queryString(self, S: str, N: int) -> bool:
        for n in range(N, 0, -1):
            if format(n, 'b') not in S:
                return False
        return True
