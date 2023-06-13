import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# r,c: 로봇청소기의 시작 좌표, d:로봇청소기의 방향
r, c, d = map(int, input().split())
# 방 (0:청소안됨, 1:벽) 2: 청소끝
room = [list(map(int, input().split())) for _ in range(N)]

# 북, 동, 남, 서
directy = [-1, 0, 1, 0]
directx = [0, 1, 0, -1]

cnt = 0

while 1:
    # 현재 청소가 안된 곳이라면 청소하고 +1
    if room[r][c] == 0:
        room[r][c] = 2
        cnt += 1

    # 청소할 위치를 찾았는지 확인하기
    cleaned = False
    for i in range(4):
        # 반시계 방향으로 90도 회전 (왼쪽으로 이동)
        dr = (d + 3) % 4
        dy, dx = r + directy[dr], c + directx[dr]
        # 범위 내이고 청소 안된곳이라면 r,c,dr 업데이트
        if 0 <= dy < N and 0 <= dx < M and room[dy][dx] == 0:
            r, c = dy, dx
            d = dr
            # 찾았음을 표시 break (계속 찾지않게 하기 위해)
            cleaned = True
            break
        d = dr

    # 천소할 곳을 찾지 못한 경우 (벽이거나 청소된 경우)
    if not cleaned:
        # 후진 하기
        dr = (d + 2) % 4
        dy, dx = r + directy[dr], c + directx[dr]
        # 벽을 만났을 경우 break
        if room[dy][dx] == 1:
            break
        r, c = dy, dx

print(cnt)