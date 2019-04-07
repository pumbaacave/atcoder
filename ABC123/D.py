
import heapq
import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
def li(): return map(int, stdin.readline().split())
i_a, i_b, i_c, K = tuple(li())
A = list(li())
B = list(li())
C = list(li())
A.sort()
B.sort()
C.sort()

memo = {}
heap = []
def val(a,b,c):
    if a<0 or b<0 or c<0:
        return False
    return A[a] + B[b] + C[c]
total = val(i_a-1, i_b-1, i_c-1)
heap = [(-total, i_a-1, i_b-1, i_c-1)]
while K > 0:
    K -= 1
    cur = heapq.heappop(heap)
    print(-cur[0])
    a,b,c = cur[1], cur[2], cur[3]
    if (a-1, b,c) not in memo:
        va = val(a-1,b,c)
        if va:
            memo[(a-1,b,c)] = True
            heapq.heappush(heap, [-va, a-1, b, c])
    if (a, b-1,c) not in memo:
        vb = val(a,b-1,c)
        if vb:
            memo[(a,b-1,c)] = True
            heapq.heappush(heap, [-vb, a, b-1, c])

    if (a, b,c-1) not in memo:
        vc = val(a,b,c-1)
        if vc:
            memo[(a,b,c-1)] = True
            heapq.heappush(heap, [-vc, a, b, c-1])


