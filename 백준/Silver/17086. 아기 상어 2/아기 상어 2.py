from collections import deque

directy = [-1, -1, -1, 0, 0, 1, 1, 1]
directx = [-1, 0, 1, -1, 1, -1, 0, 1]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def bfs():
    while q:
        y, x = q.popleft()
        for k in range(8):
            dy, dx = y + directy[k], x + directx[k]
            if 0 <= dy < n and 0 <= dx < m and arr[dy][dx] == 0:
                q.append((dy, dx))
                arr[dy][dx] = arr[y][x] + 1

# 상어 위치 저장하기
q = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append((i, j))

# BFS를 상어 위치부터 시작하도록 함수 호출
bfs()

# 최대 거리 찾기
rlt = 0
for i in arr:
    rlt = max(rlt, max(i))

print(rlt - 1)
