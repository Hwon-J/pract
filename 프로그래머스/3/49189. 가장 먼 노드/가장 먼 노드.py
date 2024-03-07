from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    visit = [0]*(n+1)
    for y, x in edge:
        graph[y].append(x)
        graph[x].append(y)
    
    visit[1] = 1
    q = deque()
    q.append(1)
    
    while q:
        tm = q.popleft()
        for i in graph[tm]:
            if visit[i] == 0:
                visit[i] = visit[tm]+1
                q.append(i)
                
    max_dist = max(visit)
    answer = visit.count(max_dist)
    return answer