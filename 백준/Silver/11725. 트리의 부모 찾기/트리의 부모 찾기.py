import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N = int(input())

graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N + 1)]
answer = [0 for _ in range(N + 1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(num):
    for i in graph[num]:
        if not visited[i]:
            answer[i] = num
            visited[i] = 1
            dfs(i)

visited[1] = 1
dfs(1)
for i in range(2, N+1):
    print(answer[i])