import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

s, t = map(int, input().split())
INF = int(21e8)
dist = [INF]*(n+1)
dist[s] = 0

def dijk(s):
    q = []
    heapq.heappush(q, (0, s))
    while q:
        cost, node = heapq.heappop(q)
        if dist[node] < cost: continue
        for i in graph[node]:
            if cost + i[1] < dist[i[0]]:
                dist[i[0]] = cost + i[1]
                heapq.heappush(q, (cost + i[1], i[0]))

dijk(s)
print(dist[t])
