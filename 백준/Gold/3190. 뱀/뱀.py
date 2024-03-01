n = int(input())
maps = [[0] * (n + 1) for _ in range(n + 1)]

k = int(input())
for _ in range(k):
    x, y = map(int, input().split())
    maps[x][y] = 2

l = int(input())
turn_lst = [input().split() for _ in range(l)]

x, y = 1, 1
maps[y][x] = 1

directy = [0, -1, 0, 1]
directx = [1, 0, -1, 0]

dir = 0
time = 0
turn = 0

snake = [[y, x]]
while True:
    y += directy[dir]
    x += directx[dir]
    if 1 <= y <= n and 1 <= x <= n and maps[y][x] != 1:
        if maps[y][x] != 2:
            dy, dx = snake.pop(0)
            maps[dy][dx] = 0
        maps[y][x] = 1
        snake.append([y, x])
    else:
        time += 1
        break
    time += 1
    if turn < l and int(turn_lst[turn][0]) == time:
        if turn_lst[turn][1] == 'L':
            dir = (dir + 1) % 4
        else:
            dir = (dir - 1) % 4
        turn += 1

print(time)
