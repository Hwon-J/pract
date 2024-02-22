from collections import deque
def solution(maps):
    row = len(maps[0])
    col = len(maps)
    visit = [[0]*row for _ in range(col)]
    visit[0][0] = 1
    q = deque()
    q.append([0,0,1])
    while q:
        y, x, cnt = q.popleft()
        if y == col-1 and x == row-1:
            return cnt
        for dy, dx in [(0,1), (1,0), (0,-1), (-1,0)]:
            ny, nx = y+dy, x+dx
            if 0 <= ny < col and 0 <= nx < row and maps[ny][nx]==1 and visit[ny][nx]==0:
                visit[ny][nx] = 1
                q.append([ny, nx, cnt +1])
    return -1