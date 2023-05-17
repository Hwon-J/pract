import heapq
n = int(input())
q = []
mx = 0
for _ in range(n):
    day, score = map(int, input().split())
    mx = max(mx, day)
    heapq.heappush(q, (-score, day))
rlt = [0]*(mx+1)
while q:
    tm = heapq.heappop(q)
    cn = tm[1]
    while 1:
        if cn<1:
            break
        else:
            if rlt[cn]==0:
                rlt[cn]=-tm[0]
                break
            else:
                cn-=1

print(sum(rlt))