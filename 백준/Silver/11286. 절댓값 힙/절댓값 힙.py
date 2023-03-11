import heapq
import sys
input = sys.stdin.readline
N=int(input())

q=[]

for _ in range(N):
    tm=int(input())
    if tm !=0:
        heapq.heappush(q,(abs(tm),tm))
    else:
        if not q:
            print(0)
        else:
            rlt=heapq.heappop(q)
            print(rlt[1])