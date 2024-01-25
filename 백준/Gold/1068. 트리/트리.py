def dfs(node):
    node_check[node] = 1
    for child in graph[node]:
        if node_check[child] == 0:
            node_check[child] = 1
            dfs(child)

N = int(input())
node_parents = list(map(int, input().split()))
remove_node = int(input())
graph = [[] for _ in range(N)]
node_check = [0]*N
leaf = 0

for i in range(len(node_parents)):
    if node_parents[i] >= 0:
        graph[node_parents[i]].append(i)

if node_parents[remove_node] >= 0:
    graph[node_parents[remove_node]].remove(remove_node)

dfs(remove_node)

for i in range(len(node_check)):
    if node_check[i] == 0:
        if not graph[i]:
            leaf+=1

print(leaf)