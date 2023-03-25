def dfs(level,i):
    global flag
    if level==4:
        flag = 1
        return
    for k in friend[i]:
        if visited[k]==0:
            visited[k]=1
            dfs(level+1,k)
            visited[k]=0

N,M=map(int, input().split())
friend=[[] for _ in range(N)]
for _ in range(M):
    a,b=map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)
flag=0
for i in range(N):
    if friend[i]:
        visited=[0]*N
        visited[i]=1
        dfs(0,i)
    if flag:
        break
if flag:
    print(1)
else:
    print(0)