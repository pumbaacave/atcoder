class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        if sum(A) % 3 != 0:
            return False
        target = sum(A) // 3
        total = 0
        cnt = 0
        for num in A:
            total += num
            if total == target:
                total = 0
                cnt += 1
        return cnt == 3
