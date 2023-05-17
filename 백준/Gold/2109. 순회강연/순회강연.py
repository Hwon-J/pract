import heapq
n = int(input())

q = []

mx = 0
for _ in range(n):
    price, day = map(int, input().split())
    mx = max(mx, day)
    heapq.heappush(q, (-price, day))

rlt = [0]*(mx+1)
while q:
    tm = heapq.heappop(q)
    cn = tm[1]
    while cn>=1:
        if rlt[cn]==0:
            rlt[cn]=-tm[0]
            break
        else:
            cn-=1

print(sum(rlt))