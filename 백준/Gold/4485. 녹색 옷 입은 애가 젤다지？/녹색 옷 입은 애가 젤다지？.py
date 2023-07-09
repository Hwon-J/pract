from collections import deque

t = 0
while True:
    n = int(input())
    t += 1
    if n == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(n)]
    INF = int(21e8)
    visit = [[INF]*n for _ in range(n)]

    directy = [1, -1, 0, 0]
    directx = [0, 0, 1, -1]

    def bfs(y, x):
        q = deque()
        q.append([y, x])
        visit[y][x] = arr[y][x]
        while q:
            y, x = q.popleft()
            for j in range(4):  
                dy = directy[j] + y  
                dx = directx[j] + x 
                if dy in range(n):
                    if dx in range(n):
                        if visit[dy][dx] > visit[y][x] + arr[dy][dx]:
                            visit[dy][dx] = visit[y][x] + arr[dy][dx]
                            q.append([dy, dx])


    bfs(0, 0)
    cost = visit[-1][-1]
    print(f'Problem {t}: {cost}')
