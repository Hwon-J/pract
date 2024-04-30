from collections import deque

def bfs(x, y):
    q = deque([(x, y)])
    visit[x][y] = 1
    area = 1
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + directx[i], cy + directy[i]
            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0 and picture[nx][ny]:
                visit[nx][ny] = 1
                q.append((nx, ny))
                area += 1
    return area

n, m = map(int, input().split())
picture = [list(map(int, input().split())) for _ in range(n)]
visit = [[0] * m for _ in range(n)]
directy = [1, -1, 0, 0]
directx = [0, 0, -1, 1]
cnt = 0
mx = 0

for i in range(n):
    for j in range(m):
        if picture[i][j] and visit[i][j] == 0:
            cnt += 1
            area = bfs(i, j)
            mx = max(mx, area)

print(cnt)
print(mx)