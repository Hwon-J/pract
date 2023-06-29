from collections import deque

n,m,k = map(int, input().split())
arr = [[0]*m for _ in range(n)]
visit = [[0]*m for _ in range(n)]

directy = [0,0,1,-1]
directx = [1,-1,0,0]

for _ in range(k):
    r,c = map(int, input().split())
    arr[r-1][c-1]=1

mx = 0

def bfs(i,j):
    visit[i][j]=1
    q = deque()
    q.append((i,j))
    cnt=1
    while q:
        y,x = q.popleft()
        for t in range(4):
            dy = directy[t]+y
            dx = directx[t]+x
            if 0<=dy<n and 0<=dx<m and arr[dy][dx]==1 and visit[dy][dx]==0:
                visit[dy][dx]=1
                cnt+=1
                q.append((dy,dx))
    return cnt

for i in range(n):
    for j in range(m):
        if arr[i][j]==1 and visit[i][j]==0:
            mx = max(bfs(i,j), mx)

print(mx)
