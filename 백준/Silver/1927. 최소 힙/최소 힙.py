import heapq,sys
input = sys.stdin.readline

N = int(input())
cnt = 0
q =[]
for i in range(N):
    a = int(input())
    if a == 0 and q:
        print(heapq.heappop(q))
    elif a == 0 and not q:
        print(0)
    else:
        heapq.heappush(q,a)