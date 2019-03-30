class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        double_a = A * 2
        if double_a.find(B) >= 0:
            return True
        return False
