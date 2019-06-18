class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        if not J: return 0
        dt = set(J)
        # implicit conversion True -> 1
        return sum(s in dt for s in S)
