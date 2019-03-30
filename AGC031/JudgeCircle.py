from collections import Counter
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if not moves: return True
        cnt = Counter(moves)
        return cnt["L"] == cnt["R"] and cnt["U"] == cnt["D"]

