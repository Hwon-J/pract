from collections import deque

def dfs(num):
    print(num, end=' ')
    if sum(visited)==N:
        return
    lst = sorted(graph[num])
    for i in lst:
        if visited[i] == False:
            visited[i] = True
            dfs(i)

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


# N: 정점의 개수, M: 간선의 개수, V: 탐색을 시작할 번호
N, M, V = map(int, input().split())
# 인접리스트를 위한 빈리스트 만들기
graph = [[] for _ in range(N + 1)]
# DFS의 방문체크
visited = [False for _ in range(N + 1)]
# Bfs의 방문체크
visited2 = [False for _ in range(N + 1)]
# 인접리스트 채우기
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited[V]=visited2[V]= True
dfs(V)
print()
bfs(V)
