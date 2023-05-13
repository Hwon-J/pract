import sys, heapq
input = sys.stdin.readline

N = int(input())
q = []
for _ in range(N):
    x = int(input())
    heapq.heappush(q,x)

sum = 0
while 1:
    if len(q)==1:
        break
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    tm = a + b
    sum += tm
    heapq.heappush(q,tm)
print(sum)