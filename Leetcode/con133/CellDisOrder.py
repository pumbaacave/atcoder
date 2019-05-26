from collections import deque
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        #BST
        state = []
        memo = set()
        queue = deque([(r0, c0)])
        while queue:
            i, j = queue.popleft()
            if 0<=i<R and 0<=j<C and (i, j) not in memo:
                state.append([i, j])
                memo.add((i, j))
                queue.append((i-1, j))
                queue.append((i+1, j))
                queue.append((i, j+1))
                queue.append((i, j-1))
        return state
