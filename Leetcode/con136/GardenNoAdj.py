from collections import defaultdict
class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        if N == 1: return [1]
        # BFS
        # adjacent list
        seen = dict()
        adjs = defaultdict(list)
        colors = {1, 2, 3, 4}
        for l, r in paths:
            adjs[l].append(r)
            adjs[r].append(l)
        ans = [0] * N

        def dfs(node):
            if node in seen: return
            bad = {seen[nei] for nei in adjs[node] if nei in seen}
            diff = colors - bad
            c = diff.pop()
            seen[node] = c
            ans[node - 1] = c
            for nei in adjs[node]:
                if nei not in seen:
                    dfs(nei)
        for i in range(N):
            dfs(i)
        return ans

