N = int(input())
M = int(input())
graph = [[0]*(N+1)]+[[0]+list(map(int, input().split())) for _ in range(N)]
path = list(map(int, input().split()))
parent = [i for i in range(N+1)]
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

for i in range(N+1):
    for j in range(N+1):
        if graph[i][j]==1:
            union(i,j)

flag = 1
for k in range(M-1):
    if parent[path[k]]!=parent[path[k+1]]:
        flag=0
        break
if flag:
    print('YES')
else:
    print('NO')
