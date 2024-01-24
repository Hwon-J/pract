from collections import deque

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
visit = [[0]*M for _ in range(N)]
directy = [1,-1,0,0]
directx = [0,0,1,-1]
q = deque()

for i in range(N):
    for j in range(M):
        if box[i][j]==1:
            q.append([i,j])
            visit[i][j] = 1
        elif box[i][j]== -1:
            visit[i][j] = -1

while q:
    tm = q.popleft()
    for i in range(4):
        dy = directy[i]+tm[0]
        dx = directx[i]+tm[1]
        if 0 <= dy < N and 0 <= dx < M and visit[dy][dx]==0:
            visit[dy][dx] = visit[tm[0]][tm[1]]+1
            q.append([dy,dx])

zero = 0
for i in visit:
    zero += i.count(0)

if zero == 0:
    print(max(map(max,visit))-1)
else:
    print(-1)