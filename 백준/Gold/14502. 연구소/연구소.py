from collections import deque
from itertools import combinations
import copy

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
visit = [[0]*m for _ in range(n)]

directy = [1,-1,0,0]
directx = [0,0,1,-1]

safe = 0

def bfs(i,j, temp_visit, temp_arr):
    q = deque()
    q.append((i,j))

    while q:
        y, x = q.popleft()
        for k in range(4):
            dy = directy[k] + y
            dx = directx[k] + x
            if 0 <= dy < n and 0 <= dx < m:
                if temp_arr[dy][dx] == 0 and temp_visit[dy][dx]==0:
                    temp_arr[dy][dx] = 2
                    temp_visit[dy][dx]=1
                    q.append((dy, dx))


temp = []
for i in range(n):
    for j in range(m):
        if arr[i][j]==0:
            temp.append([i,j])

picks = list(combinations(temp,3))

for pick in picks:
    temp_arr = copy.deepcopy(arr)
    temp_visit = copy.deepcopy(visit)

    for tm in pick:
        temp_arr[tm[0]][tm[1]] = 1  # 벽으로 설정

    for i in range(n):
        for j in range(m):
            if temp_arr[i][j] == 2 and temp_visit[i][j] == 0:
                temp_visit[i][j] = 1
                bfs(i, j, temp_visit, temp_arr)

    count = 0
    for i in range(n):
        for j in range(m):
            if temp_arr[i][j] == 0:
                count += 1

    safe = max(safe, count)

print(safe)