from collections import defaultdict, Counter, deque
class Solution(object):
    def countSubTrees(self, n, edges, labels):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :rtype: List[int]
        """
        #build tree
        ch = defaultdict(set)
        for l, r in edges:
            ch[l].add(r)
            ch[r].add(l)
        q = deque()
        q.append(0)
        while q:
            cur = q.popleft()
            for c in ch[cur]:
                q.append(c)
                ch[c].discard(cur)
        #DFS
        self.peer= [1] * n
        def dfs(idx):
            # base case
            if len(ch[idx]) == 0:
                return Counter(labels[idx])

            if len(ch[idx]) == 1:
                cnt = dfs(ch[idx].pop())
            else:
                cnt = Counter()
                for c in ch[idx]:
                    cnt += dfs(c)
            cnt[labels[idx]] += 1
            self.peer[idx] = cnt[labels[idx]]
            return cnt
        dfs(0)
        return self.peer
