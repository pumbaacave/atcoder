from collections import Counter
import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def li(): return map(int, stdin.readline().split())
N, K = tuple(li())
coefs = list(li())
num_coefs = len(coefs)
max_co = max(coefs)
L_e = len(format(max_co, 'b'))
L_k = len(format(K, 'b'))
L = L_k # TODO, heading bit can be set to 1, since coefs are all 0
format_spec = '0>{}b'.format(L)
formatted_co = map(lambda x:format(x, format_spec), coefs)
cnt = Counter()
# can use zip() to speed up
for coef_bin_str in formatted_co:
    for i in range(L):
        if coef_bin_str[i] == '1':
            cnt[i] += 1
res = []
for i in range(L):
    if cnt[i] > L//2:
        res.append('0')
    else:
        res.append('1')
res_str = ''.join(res)
res_int = int(res_str, 2)
if res_int > K:
    K_bin = format(K, 'b')
    res[0] = K_bin[0]

res_str = ''.join(res)
res_int = int(res_str, 2)

total = 0
for coef in coefs:
    xor = res_int ^ coef
    total += xor
print(total)
