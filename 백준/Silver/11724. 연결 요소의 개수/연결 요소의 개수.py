import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def ans(temp):
    for i in range(1,N+1):
        if arr[temp][i]==1 and visit[i]==0:
            visit[i]=1
            ans(i)

N,M= map(int,input().split())
arr=[[0]*(N+1) for _  in range(N+1)]
visit=[0]*(N+1)
cnt=0
for i in range(M):
    u,v =map(int, input().split())
    arr[u][v]=arr[v][u]=1

for i in range(1,N+1):
    if visit[i]==0:
        ans(i)
        cnt+=1
print(cnt)