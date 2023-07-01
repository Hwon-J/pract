import sys
input = sys.stdin.readline
from collections import deque

s, g = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(s)]

directy = [1, -1, 0, 0]
directx = [0, 0, 1, -1]

time = 0
cheese = 0


def bfs(i, j):
    visit = [[0] * g for _ in range(s)]
    q = deque()
    q.append((i, j))
    visit[i][j] = 1

    while q:
        y, x = q.popleft()
        for t in range(4):
            dy = directy[t] + y
            dx = directx[t] + x
            if 0 <= dy < s and 0 <= dx < g and visit[dy][dx] == 0:
                if arr[dy][dx] == 1:
                    arr[dy][dx] = 0
                else:
                    q.append((dy, dx))
                visit[dy][dx] = 1


while True:
    cnt = 0
    for i in arr:
        cnt += sum(i)
    if cnt == 0:
        break
    time += 1
    cheese = cnt

    bfs(0, 0)

print(time)
print(cheese)