import sys, heapq
input = sys.stdin.readline

rlt=[]
q=[]
N = int(input())

for _ in range(N):
    a, b = map(int, input().split())
    q.append([a,b])
q.sort()

rlt = []
for a, b in q:
    if not rlt:
        heapq.heappush(rlt, b)
    else:
        if rlt[0] <= a:
            heapq.heappop(rlt)
        heapq.heappush(rlt, b)

print(len(rlt))