from collectins import Counter
class Solution:
    def subarraysDivByK(self, A: 'List[int]', K: 'int') -> 'int':
        c = Counter()
        c[0] += 1
        P = [0]

        for a in A:
            mod = (P[-1] + a )%K
            P.append(mod)
            c[mod] += 1

        total = 0
        for v in c.values():
            total += v*(v-1)//2
        return total

