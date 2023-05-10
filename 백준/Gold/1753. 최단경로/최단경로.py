import sys, heapq
input = sys.stdin.readline

# V: 정점의 개수, E: 간선의 개수
V, E = map(int, input().split())
# S: 시작 간선
S = int(input())
# 인접 리스트
graph = [[] for _ in range(V+1)]
INF = int(21e8)
visit = [0]*(V+1)
rlt = [INF]*(V+1)

# 인접리스트 채우기
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v,w])


def dijk(st):
    q = []
    heapq.heappush(q, (0,st))
    rlt[st] = 0
    while q:
        dist, now = heapq.heappop(q)
        if rlt[now] < dist: continue

        # 거리를 계산하여 갱신한다.
        for i in graph[now]:
            tm = dist + i[1]
            if tm < rlt[i[0]]:
                rlt[i[0]] = tm
                heapq.heappush(q, (tm, i[0]))

dijk(S)

for i in range(1,V+1):
    if rlt[i]==INF:
        print('INF')
    else:
        print(rlt[i])