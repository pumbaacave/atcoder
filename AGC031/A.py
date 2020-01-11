import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def li(): return map(int, stdin.readline().split())
def ni(): return int(stdin.readline())
def ns(): return stdin.readline().rstrip()

N = ni()
S = ns()
#  S = 'abcab'
#  N = len(S)

num_comb = 0
state = []
selected = set()

def iter_helper(idx):
    # print(idx)
    for i in range(idx, N):
        if S[i] in selected:
            continue
        else:
            state.append(S[i])
            selected.add(S[i])
            # print(f'add {S[i]} at {i}')
            iter_helper(i + 1)
            global num_comb
            num_comb += 1
            # print(state)
            # print(f'discard {S[i]} at {i}')
            selected.discard(S[i])
            state.pop()
iter_helper(0)
print(num_comb % (10**9 +7))


