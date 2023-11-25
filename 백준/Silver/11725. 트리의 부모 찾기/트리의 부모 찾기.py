from collections import deque

import sys
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N + 1)]
answer = [0 for _ in range(N + 1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(num):
    q = deque()
    q.append(num)
    while q:
        tm = q.popleft()
        for i in graph[tm]:
            if not visited[i]:
                q.append(i)
                answer[i] = tm
                visited[i] = 1
visited[1] = 1
bfs(1)
for i in range(2, N+1):
    print(answer[i])
