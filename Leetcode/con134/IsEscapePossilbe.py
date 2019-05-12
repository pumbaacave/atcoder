class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        if not blocked: return True
        target = tuple(target)
        b_set =  {(r, c) for r, c in blocked}

        grid = {}
        def get_ns(r, c):
            ns = [(r + i, c + j) for (i, j) in [(0, 1), (0, -1), (1, 0), (-1, 0)]
                    if (0<= r+i < 10e5 and 0 <= c+j < 10e5 and (r, c) not in blocked)]
            delta = target[0] - r, target[1] - c
            ns.sort(key=lambda x: abs(x[0]*delta[0] + x[1]+delta[1]))
            return(ns)
        def search(r, c):
            if (r, c) in grid or (r, c) in b_set:
                return False
            print(r, c)
            # return Bool
            if (r, c) == target:
                return True
            else:
                grid[r, c] = False
                ns = get_ns(r, c)
                return any(search(*n) for n in ns)


        return search(*source)

class Solution:
    # thd trap area enclosed by blocked is limited
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        if not blocked: return True
        L = len(blocked)
        blocked = {tuple(b) for b in blocked}
        limit = L * (L - 1) // 2
        seen = set()
        def dfs(c, r, target, step=0):
            if (c, r) in blocked or (c, r) in seen or c < 0 or c >= 10e5 or r < 0 or r >= 10e5:
                return False
            elif [c, r] == target or step > limit:
                return True
            else:
                seen.add((c, r))
                return dfs(c - 1, r, target, step + 1) or \
                        dfs(c + 1, r, target, step + 1) or \
                        dfs(c, r + 1, target, step + 1) or \
                        dfs(c, r - 1, target, step + 1)

        return dfs(source[0], source[1], target, 0) and dfs(target[0], target[1], source, 0)
