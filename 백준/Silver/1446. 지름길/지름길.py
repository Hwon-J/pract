import sys
input = sys.stdin.readline

n, d = map(int, input().split())

dist = [i for i in range(d+1)]

graph = []

for _ in range(n):
    s, e, r = map(int, input().split())
    graph.append([s,e,r])

for i in range(d+1):
    dist[i] = min(dist[i], dist[i-1] + 1)
    for j in graph:
        if i == j[0] and j[1] <= d and dist[i] + j[2] < dist[j[1]]:
            dist[j[1]] = dist[i] + j[2]

print(dist[d])