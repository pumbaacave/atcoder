class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        step = 0
        while True:
            step += 1
            if memory1 >= memory2:
                if step > memory1:
                    return [step, memory1, memory2]
                else:
                    memory1 -= step
            else:
                if step > memory2:
                    return [step, memory1, memory2]
                else:
                    memory2 -= step
