from collections import deque
import sys
input = sys.stdin.readline


T = int(input())
for tc in range(T):
    m,n,k = map(int, input().split())
    arr = [[0]*m for _ in range(n)]
    visit = [[0] * m for _ in range(n)]

    for i in range(k):
        x,y = map(int, input().split())
        arr[y][x] = 1

    directy = [1, -1, 0, 0]
    directx = [0, 0, 1, -1]

    def bfs(i,j):
        q = deque()
        q.append((i,j))
        visit[i][j]=1
        while q:
            y,x  = q.popleft()
            for k in range(4):
                dy = y +directy[k]
                dx = x + directx[k]
                if 0<=dy<n and 0<=dx<m and arr[dy][dx]==1 and visit[dy][dx]==0:
                    q.append((dy,dx))
                    visit[dy][dx]=1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j]==1 and visit[i][j]==0:
                bfs(i,j)
                cnt+=1
    print(cnt)