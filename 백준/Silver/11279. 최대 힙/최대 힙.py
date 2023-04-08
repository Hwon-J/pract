import heapq,sys
input = sys.stdin.readline
N = int(input())
q =[]
for _ in range(N):
    a = int(input())
    if a != 0:
        heapq.heappush(q,-a)
    else:
        if not q:
            print(0)
        else:
            print(-heapq.heappop(q))