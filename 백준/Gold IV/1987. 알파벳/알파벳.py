import sys
input=sys.stdin.readline

r,c = map(int, input().split())
arr = [list(input()) for _ in range(r)]


def dfs(y, x, dist):
    global cnt

    cnt = max(cnt, dist)

    for i in range(4):
        dy = directy[i] + y
        dx = directx[i] + x
        if 0<=dy<r and 0<=dx<c:
            tm = ord(arr[dy][dx]) - ord('A')
            if not check[tm]:
                check[tm] = 1
                dfs(dy, dx, dist + 1)
                check[tm] = 0


check = [0]*26
directy = [0,0,1,-1]
directx = [1,-1,0,0]

cnt = 0

check[ord(arr[0][0]) - ord('A')] = 1
dfs(0,0,1)


print(cnt)