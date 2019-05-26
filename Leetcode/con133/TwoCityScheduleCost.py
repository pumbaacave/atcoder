class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        total = sum(a for a, b in costs)
        costs.sort(key=lambda x: x[1] - x[0])
        L = len(costs)//2
        for i in range(L):
            total - costs[i][0] + costs[i][1]
        return total


