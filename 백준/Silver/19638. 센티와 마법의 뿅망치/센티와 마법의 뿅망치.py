import heapq, sys
input = sys.stdin.readline

n, c, t = map(int, input().split())
arr = []
cnt = 0
for i in range(n):
    h = int(input())
    heapq.heappush(arr, -h)

for j in range(t):
    tm= -heapq.heappop(arr)
    if tm==1:
        heapq.heappush(arr,-tm)
    elif tm < c:
        heapq.heappush(arr,-tm)
        break
    else:
        heapq.heappush(arr,-(tm//2))
        cnt+=1

mx = -heapq.heappop(arr)

if mx >= c:
    print("NO")
    print(mx)
else:
    print("YES")
    print(cnt)

