from typing import *
from collections import defaultdict, deque, Counter
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # topology sort
        orders = defaultdict(set)
        cnt_parent = Counter()
        chrs = set(''.join(words))
        for c in chrs:
            cnt_parent[c] = 0
        # give every char num_parent remain
        # if parent char is append to return list
        # than num_parent -= 1
        # once the char has no dependant parent_char
        # it can be add to return list
        def build(words):
            """
            rtype bool: fail on False
            """
            if not words:
                return True
            stack = []
            for w in words:
                if not stack:
                    stack.append((w[0], w[1:]))
                elif w[0] == stack[-1][0]:
                    stack.append((w[0], w[1:]))
                else:
                    front = stack[-1][0]
                    chd = w[0]
                    if front in orders[chd]:
                        return False
                    else:
                        if chd not in orders[front]:
                            orders[front].add(chd)
                            cnt_parent[chd] += 1
                    if not build([t[1] for t in stack if t[1]]):
                        return False
                    stack.clear()
                    stack.append((w[0], w[1:]))

            if not build([t[1] for t in stack if t[1]]):
                return False
            return True

        def bfs(keys):
            #  import ipdb
            #  ipdb.set_trace()
            str_builder = []
            queue = deque(keys)
            while queue:
                cur = queue.popleft()
                str_builder.append(cur)
                for ch in orders[cur]:
                    cnt_parent[ch] -= 1
                    # chd thur to be root
                    if cnt_parent[ch] == 0:
                        queue.append(ch)
            return str_builder


        if not build(words):
            return ''
        else:
            roots = list(filter(lambda k:cnt_parent[k] == 0, cnt_parent.keys()))
            ret = ''.join(bfs(roots))
            print(orders, roots)
            return ret

def test_s():
    words = ["wrt","wrf","er","ett","rftt"]
    s = Solution()
    assert s.alienOrder(words) == "wertf"
test_s()
