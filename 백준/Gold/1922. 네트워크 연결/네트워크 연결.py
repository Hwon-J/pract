import sys
input = sys.stdin.readline

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(a,b):
    a, b = find(a),find(b)
    if a < b:
        parents[b]=a
    else:
        parents[a]=b

N = int(input())
M = int(input())
edges = []
for _ in range(M):
    a,b,c = map(int, input().split())
    edges.append([c, a, b])
edges.sort()
answer = 0
parents = [i for i in range(N+1)]
for edge in edges:

    cost, node1, node2 = edge
    if find(node1) != find(node2):
        union(node1, node2)
        answer+=cost
print(answer)
