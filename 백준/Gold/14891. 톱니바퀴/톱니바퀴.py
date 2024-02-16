def rotate(gear, dir):
    if dir == 1:
        return [gear[7]] + gear[:7]
    else:
        return gear[1:] + [gear[0]]

gears = [list(map(int, input())) for _ in range(4)]
K = int(input())

for _ in range(K):
    num, dir = map(int, input().split())
    num -= 1
    dirs = [0] * 4
    dirs[num] = dir

    for i in range(num, 0, -1):
        if gears[i][6] != gears[i-1][2]:
            dirs[i-1] = -dirs[i]
        else:
            break

    for i in range(num, 3):
        if gears[i][2] != gears[i+1][6]:
            dirs[i+1] = -dirs[i]
        else:
            break

    for i in range(4):
        if dirs[i] != 0:
            gears[i] = rotate(gears[i], dirs[i])

score = 0
for i in range(4):
    if gears[i][0]:
        score += 2**i
print(score)
