from collections import deque

m, n, k = map(int, input().split())
rectangles = [list(map(int, input().split())) for _ in range(k)]
graph = [[0]*m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for rect in rectangles:
    x1, y1, x2, y2 = rect
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j] = 1

def bfs(x, y):
    cnt = 1
    q = deque([(x, y)])
    graph[x][y] = 1
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                q.append((nx, ny))
                graph[nx][ny] = 1
                cnt += 1
    return cnt

areas = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            areas.append(bfs(i, j))

print(len(areas))
print(*sorted(areas))
