class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        pos = set(range(6))
        for domino in zip(A, B):
            pos = pos.intersection(domino)

        if not pos:
            return -1
        common = pos.pop()
        return min( len(A) - A.count(common), len(B) - B.count(common) )
