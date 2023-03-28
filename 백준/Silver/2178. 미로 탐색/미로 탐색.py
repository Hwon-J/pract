def bfs(y,x):
    q=[]
    q.append([y,x,1])
    while 1:
        ny,nx,cnt = q.pop(0)
        if ny==N-1 and nx==M-1:
            break

        for i in range(4):
            dy = ny + directy[i]
            dx = nx + directx[i]
            if 0 <= dy < N and 0 <= dx < M and visited[dy][dx]==0:
                if maze[dy][dx]==1:
                    visited[dy][dx]=1
                    q.append([dy,dx,cnt+1])
    return cnt


# N: 세로줄 M: 가로줄
N, M = map(int, input().split())
maze = [list(map(int,input())) for _ in range(N)]
visited=[[0]*M for _ in range(N)]
directy = [1,-1,0,0]
directx = [0,0,1,-1]

visited[0][0]=1
print(bfs(0,0))