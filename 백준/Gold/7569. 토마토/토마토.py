import sys
input = sys.stdin.readline
from collections import deque

M, N, H = map(int, input().split())
tomato = []
for i in range(H):
    arr = [list(map(int, input().split())) for _ in range(N)]
    tomato.append(arr)

directx = [0,0,1,-1,0,0]
directy = [1,-1,0,0,0,0]
directz = [0,0,0,0,1,-1]

q = deque()
zero=0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k]==1:
                q.append((0,i,j,k))
            elif tomato[i][j][k]==0:
                zero+=1

rlt=0
if zero==0:
    print(0)
else:
    while q:
        day,i,j,k = q.popleft()
        rlt=day
        for dr in range(6):
            dx = directx[dr] + k
            dy = directy[dr] + j
            dz = directz[dr] + i
            if 0<=dx<M and 0<=dy<N and 0<=dz<H:
                if tomato[dz][dy][dx]==0:
                    q.append((day+1,dz,dy,dx))
                    tomato[dz][dy][dx] = 1
                    zero-=1
    if zero==0:
        print(rlt)
    else:
        print(-1)
