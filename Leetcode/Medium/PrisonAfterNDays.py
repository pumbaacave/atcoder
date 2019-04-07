class Solution:
    """
    1. once duplicate state found, means there is a Cycle of period P
    2. However init state may not within period states, should find where cycle start
    """
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        L = len(cells)
        pre, cur = 0, 0
        memo = {}
        cnt, cur_idx = -1, 0
        queue = []

        for _ in range(N):
            cnt += 1
            # examine cache
            key = tuple(cells)
            if key not in memo:
                memo[key] = cnt
                queue.append(key)
            else:
                cur_idx = cnt
                break

            # mutate
            for i in range(L):
                if i in (0, L - 1):
                    pre = cells[i]
                    cells[i] = 0
                else:
                    cur = cells[i]
                    cells[i] = 1 - (pre ^ cells[i + 1])
                    pre = cur
        if not cur_idx:
            return cells
        period = cur_idx - memo[tuple(cells)]
        base = memo[tuple(cells)]
        target_idx = (N - base) % period + base
        res = queue[target_idx]
        return list(res)
