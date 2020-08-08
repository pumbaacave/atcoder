class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        # build accumulative and map
        # Q(n) binary search
        n = len(arr)
        and_map = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            cu = arr[i]
            for j in range(i, n):
                # build accumulative 'and' map
                cu &= arr[j]
                and_map[i][j] = cu

        # Q(n) binary search
        # stop cond r <= l or target found

        def search(fix, l, r):
            #print(l, r)
            if r <= l:
                return r
            mid = l + (r - l) // 2
            cur = and_map[fix][mid]
            if cur == target:
                return mid
            if cur < target:
                return search(fix, l, mid - 1)
            else:
                return search(fix, mid + 1, r)

        def probe(fix):
            idx = search(fix, fix, n - 1)
            left = and_map[fix][idx - 1] if idx > 0 else float('inf')
            left = abs(left - target)
            mid = and_map[fix][idx]
            mid = abs(mid - target)
            right = and_map[fix][idx + 1] if idx < n - 2 else float('inf')
            right = abs(right - target)
            return min(left, mid, right)
        val = float('inf')
        for i in range(n):
            val = min(val, probe(i))

        return val

