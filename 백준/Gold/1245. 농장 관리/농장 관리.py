n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visit = [[0]*m for _ in range(n)]
directy = [-1, 1, 0, 0, 1, 1, -1, -1]
directx = [0, 0, -1, 1, 1, -1, 1, -1]
cnt = 0

def dfs(y,x):
    global flag
    visit[y][x] = 1
    for k in range(8):
        dy = y + directy[k]
        dx = x + directx[k]
        if 0<= dy < n and 0 <= dx <m:
            if arr[dy][dx] > arr[y][x]:
                flag = 0
            if  visit[dy][dx]==0 and arr[dy][dx] == arr[y][x]:
                dfs(dy, dx)


for i in range(n):
    for j in range(m):
        if visit[i][j]==0:
            flag = 1
            dfs(i, j)
            if flag:
                cnt += 1

print(cnt)