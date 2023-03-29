import sys
input = sys.stdin.readline
from collections import deque

V = int(input())
tree= [[] for _ in range(V+1)]
for i in range(V):
    lst = list(map(int, input().split()))
    for j in range(1,len(lst)-1,2):
        tree[lst[0]].append((lst[j],lst[j+1]))

def bfs(n):
    tm ,mx=0,0
    visited=[0]*(V+1)
    visited[n]=1
    q=deque()
    q.append([n,0])
    while q:
        now, summ = q.popleft()
        if summ>mx:
            mx=summ
            tm=now
        for i in range(len(tree[now])):
            if visited[tree[now][i][0]] ==1 : continue
            visited[tree[now][i][0]] = 1
            q.append([tree[now][i][0], summ+tree[now][i][1]])

    return tm,mx


temp,maxx=bfs(1)
temp2, rlt = bfs(temp)


print(rlt)