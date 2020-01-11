import sys
stdin = sys.stdin
def ls(): return stdin.readline()
S = ls()
first, second = int(S[:2]), int(S[2:])
def is_my(f, s):
    return 0 < f < 13

def is_ym(f, s):
    return 0 < s < 13
ym, my = is_ym(first,second), is_my(first, second)
if ym and my:
    print("AMBIGUOUS")
elif ym and not my:
    print("YYMM")
elif my and not ym:
    print("MMYY")
else:
    print("NA")
