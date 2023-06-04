import sys
from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

directy = [1, -1, 0, 0]
directx = [0, 0, 1, -1]
year = 0

def bfs(i, j):
    visit[i][j] = 1
    q2 = deque()
    q2.append((i, j))
    while q2:
        y, x = q2.popleft()
        for k in range(4):
            dy, dx = y + directy[k], x + directx[k]
            if 0 <= dy < N and 0 <= dx < M:
                if arr[dy][dx] != 0 and visit[dy][dx] == 0:
                    visit[dy][dx] = 1
                    q2.append((dy, dx))


while True:
    year += 1
    zero = [[0] * M for _ in range(N)]
    visit = [[0] * M for _ in range(N)]
    # 배열에 0이 아닌 수가 있다면 0의 개수를 카운트
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                for k in range(4):
                    dy, dx = i + directy[k], j + directx[k]
                    if 0 <= dy < N and 0 <= dx < M:
                        if arr[dy][dx] == 0:
                            zero[i][j] += 1

    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0:
                arr[i][j] -= zero[i][j]
                if arr[i][j] < 0:
                    arr[i][j] = 0

    ice = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0 and visit[i][j] == 0:
                ice += 1
                bfs(i, j)

    if ice >= 2:
        break

    summ = 0
    for i in arr:
        summ += sum(i)

    if summ == 0:
        year = 0
        break

print(year)
