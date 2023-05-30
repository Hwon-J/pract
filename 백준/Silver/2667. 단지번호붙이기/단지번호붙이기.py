N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

# 단지의 개수, 단지내 집의 수
rlt=[]
visit = [[0] * N for _ in range(N)]
cnt = 1

directy = [1, -1, 0, 0]
directx = [0, 0, 1, -1]

def dfs(i,j):
    global cnt
    for k in range(4):
        dy, dx = i+directy[k], j+directx[k]
        if 0<= dy <N and 0<= dx <N and visit[dy][dx]==0 and arr[dy][dx]==1:
            visit[dy][dx]=1
            cnt+=1
            dfs(dy,dx)


for i in range(N):
    for j in range(N):
        if arr[i][j] ==1 and visit[i][j] == 0:
            visit[i][j] = 1
            dfs(i, j)
            rlt.append(cnt)
            cnt=1

rlt.sort()

print(len(rlt))
for i in rlt:
    print(i)