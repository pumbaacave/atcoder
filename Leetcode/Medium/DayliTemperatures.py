from collections import namedtuple
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        Temp = namedtuple("Temp", ('t', 'idx'))
        lt = len(T)
        stack = []
        ret = [0] * lt
        for i, t in enumerate(T):
            if not stack:
                stack.append(Temp(t, i))
                continue
            while stack and t > stack[-1].t:
                last_temp = stack.pop()
                ret[last_temp.idx] = i - last_temp.idx

            stack.append(Temp(t, i))

        return ret
