from collections import deque
import sys
input = sys.stdin.readline
# N:도시의 개수, M: 도로의 개수, K: 최단 거리 , X: 출발 도시 정보
N, M, K, X = map(int, input().split())
arr = [[] for _ in range(N+1)]
visit = [0]*(N+1)
rlt = []

for _ in range(M):
    a,b = map(int, input().split())
    arr[a].append(b)

def bfs(st):
    q = deque()
    q.append([st,0])
    visit[st] = 1
    while q:
        now, cnt = q.popleft()
        if cnt == K:
            rlt.append(now)
        for i in arr[now]:
            if not visit[i]:
                visit[i] = 1
                q.append([i, cnt+1])

bfs(X)
if not rlt:
    print(-1)
else:
    rlt.sort()
    for i in rlt:
        print(i)