import sys
stdin = sys.stdin
def ls(): return stdin.readline()

S = ls()
num_1, num_0 = 0, 0

for s in S:

    if s == '1':
        num_1 += 1
    # maybe \n
    elif s == '0':
        num_0 += 1
print( 2 * min(num_1, num_0) )
