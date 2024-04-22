import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n+1)]
visit = [-1]*(n+1)

def dfs(st, dist):
    for node, n_dist in graph[st]:
        if visit[node] == -1:
            visit[node] = dist + n_dist
            dfs(node, dist + n_dist)

for i in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
visit[1] = 0
dfs(1,0)
max_dist_node = visit.index(max(visit))

visit = [-1] * (n + 1)
visit[max_dist_node] = 0
dfs(max_dist_node, 0)

print(max(visit))