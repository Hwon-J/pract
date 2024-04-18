from collections import deque

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

T = int(input())
for _ in range(T):
    l = int(input())
    now_x, now_y = map(int, input().split())
    move_x, move_y = map(int, input().split())

    q = deque([(now_x, now_y, 0)])
    visit = [[False] * l for _ in range(l)]
    visit[now_x][now_y] = True

    while q:
        x, y, cnt = q.popleft()
        if x == move_x and y == move_y:
            print(cnt)
            break
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and not visit[nx][ny]:
                visit[nx][ny] = True
                q.append((nx, ny, cnt + 1))
