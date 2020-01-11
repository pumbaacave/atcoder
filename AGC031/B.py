import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def li(): return map(int, stdin.readline().split())
def ni(): return int(stdin.readline())
def ns(): return stdin.readline().rstrip()

n = ni()
old = [ni() for i in range(n) ]
c = []
for o in old:
    if not c:
        c.append(o)
    elif o != c[-1]:
        c.append(o)
n = len(c)


memo = dict()
def cal_reversi(start):
    total = 0
    gaurd = set()
    for i in range(start, n):
        if c[i] in gaurd:
            total += 1
            if i + 1 not in memo:
                total_at_after_i = cal_reversi(i + 1)
                memo[i+1] = total_at_after_i
            else:
                total_at_after_i = memo[i + 1]

            total *= total_at_after_i
            return total
        else:
            gaurd.add(c[i])
    return total
total = 0
for i in range(n):
    total += cal_reversi(i)
print(memo)
print(total)

