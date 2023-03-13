import heapq
N=int(input())
q=[]

for _ in range(N):
    tm=int(input())
    heapq.heappush(q,tm)

for i in range(N):
    print(heapq.heappop(q))