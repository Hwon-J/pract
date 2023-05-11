import sys, heapq
input = sys.stdin.readline


N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
INF = int(21e8)
rlt = [INF]*(N+1)
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b,c])

S, E = map(int, input().split())

def dijk(st):
    q = []
    heapq.heappush(q, (0, st))
    rlt[st] = 0
    while q:
        dist, now = heapq.heappop(q)
        if rlt[now] < dist: continue
        for i in graph[now]:
            tm = dist + i[1]
            if tm < rlt[i[0]]:
                rlt[i[0]] = tm
                heapq.heappush(q, [tm, i[0]])


dijk(S)
print(rlt[E])