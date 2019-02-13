from collections import deque
class Solution():
    def conbination(self, candidates):
        stack = deque()
        length = len(candidates)
        superset = [[]]
        """
        basic backtracking algo impl
        """
        def bt(start, candidates):
            for i in range(start, length):
                stack.append(candidates[i])
                print(stack)
                superset.append(stack)
                # search next elem
                bt(i+1, candidates)

                stack.pop()


        bt(0, candidates)
        return superset

def test_num_combi():
    s = Solution()
    candidates = [1, 2, 3]
    ans = s.conbination(candidates)
    assert len(ans) == 2 ** len(candidates)
