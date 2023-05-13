import sys, heapq
input = sys.stdin.readline

n =int(input())
q=[]
for _ in range(n):
    x = int(input())
    if x == 0:
        if q:
            print(heapq.heappop(q))
        else:
            print(0)
    else:
        heapq.heappush(q,x)