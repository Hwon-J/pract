from collections import deque

def none_same(y,x,cnt):
    q = deque()
    q.append([y,x])
    none_visit[y][x] = cnt
    while q:
        tm = q.popleft()
        for k in range(4):
            dy = directy[k] + tm[0]
            dx = directx[k] + tm[1]
            if 0 <= dy < N and 0 <= dx < N and none_visit[dy][dx]==0:
                if area[tm[0]][tm[1]] == area[dy][dx]:
                    none_visit[dy][dx] = none_visit[tm[0]][tm[1]]
                    q.append([dy,dx])

def blind_same(y,x,cnt):
    q = deque()
    q.append([y,x])
    blind_visit[y][x] = cnt
    while q:
        tm = q.popleft()
        for k in range(4):
            dy = directy[k] + tm[0]
            dx = directx[k] + tm[1]
            if 0 <= dy < N and 0 <= dx < N and blind_visit[dy][dx]==0:
                if area[tm[0]][tm[1]] == 'B' and area[dy][dx]=='B':
                    blind_visit[dy][dx] = cnt
                    q.append([dy,dx])
                elif area[tm[0]][tm[1]] != 'B' and area[dy][dx] != 'B':
                    blind_visit[dy][dx] = cnt
                    q.append([dy, dx])

N = int(input())
area = [list(input()) for _ in range(N)]
none_visit = [[0]*N for _ in range(N)]
none_cnt = 1
blind_visit = [[0]*N for _ in range(N)]
blind_cnt = 1
directy = [1,-1,0,0]
directx = [0,0,1,-1]

for i in range(N):
    for j in range(N):
        if none_visit[i][j] == 0:
            none_same(i,j,none_cnt)
            none_cnt+=1
        if blind_visit[i][j] == 0:
            blind_same(i,j,blind_cnt)
            blind_cnt+=1

print(none_cnt-1, blind_cnt-1)
