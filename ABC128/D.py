import heapq
import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def ii(): return int(stdin.readline())
def li(): return map(int, stdin.readline().split())
N, K = tuple(li())
nums = tuple(li())
ls = [0] * K
rs = [0] * K

pq = []
total = 0
idx = 0
for k in range(0, K):
    num = nums[idx]
    if not pq:
        heapq.heappush(pq, num)
        total += num
        ls[k] = total
        idx += 1
        continue

    cur_min = heapq.heappop(pq)
    if -cur_min > num:
        # drop
        total -= cur_min
        ls[k] = total
    else:
        # take
        total += num
        ls[k] = total
        idx += 1
        heapq.heappush(pq, num)
        heapq.heappush(pq, cur_min)


pq_r = []
total = 0
idx = 0
for k in range(0, K):
    num = nums[~idx]
    if not pq:
        heapq.heappush(pq, num)
        total += num
        rs[k] = total
        idx += 1
        continue

    cur_min = heapq.heappop(pq)
    if -cur_min > num:
        # drop
        total -= cur_min
        rs[k] = total
    else:
        # take
        total += num
        rs[k] = total
        idx += 1
        heapq.heappush(pq, num)
        heapq.heappush(pq, cur_min)

up = 0
for i in range(K - 1):
    up = max(up, (ls[i] + rs[K - i - 2]) )
    up = max(up, (rs[i] + ls[K - i - 2]) )
up = max(up, ls[-1], rs[-1])
print(ls, rs)
print(up)
