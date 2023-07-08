import sys
import heapq

input = sys.stdin.readline

n, e = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

INF = int(1e9)


def dijkstra(start):
    dist = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        cost, cur = heapq.heappop(q)

        if dist[cur] < cost:
            continue

        for next_node, next_cost in graph[cur]:
            new_cost = cost + next_cost

            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                heapq.heappush(q, (new_cost, next_node))

    return dist


v1, v2 = map(int, input().split())

dist1 = dijkstra(1)
dist_v1 = dijkstra(v1)
dist_v2 = dijkstra(v2)

# 1 -> v1 -> v2 -> n
route1 = dist1[v1] + dist_v1[v2] + dist_v2[n]
# 1 -> v2 -> v1 -> n
route2 = dist1[v2] + dist_v2[v1] + dist_v1[n]

if route1 >= INF and route2 >= INF:
    print(-1)
else:
    print(min(route1, route2))
