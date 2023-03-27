from collections import deque
N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
visited2 = [False for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(level, num):
    print(num, end=' ')
    if level == N:
        return

    for i in sorted(graph[num]):
        if visited[i] == False:
            visited[i] = True
            dfs(level + 1, i)

def bfs(num):
    q=deque()
    q.append(num)
    while q:
        tm=q.popleft()
        print(tm, end=' ')
        lst=sorted(graph[tm])
        for i in lst:
            if visited2[i]==False:
                q.append(i)
                visited2[i]=True

visited[V]=visited2[V]= True
dfs(1, V)
print()
bfs(V)
